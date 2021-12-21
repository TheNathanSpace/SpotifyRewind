import json
from pathlib import Path


def get_top_ten(dictionary, count = 10):
    top_ten_list = {}
    for index, key in enumerate(dictionary.keys()):
        if index >= count:
            break

        top_ten_list[key] = dictionary[key]
    return top_ten_list


def sort_dict(dictionary, reverse = False):
    return {key: val for key, val in sorted(dictionary.items(), key = lambda ele: ele[1], reverse = not reverse)}


my_data_folder = Path.cwd() / "my_spotify_data" / "MyData"
file_list = []
streaming_history_file = my_data_folder / "StreamingHistory0.json"
file_list.append(streaming_history_file)
streaming_history_file = my_data_folder / "StreamingHistory1.json"
file_list.append(streaming_history_file)

output_file = Path.cwd() / "data.json"

most_skipped_track_dict = {}

most_played_track_dict_adjusted = {}
most_played_track_dict_raw = {}

most_played_artists_dict_adjusted = {}
most_played_artists_dict_raw = {}

streaming_history_json = []
for file in file_list:
    streaming_history_file_contents = streaming_history_file.read_text(encoding = "utf8")
    streaming_history_json += json.loads(streaming_history_file_contents)

for track_object in streaming_history_json:
    end_time = track_object["endTime"]
    artist_name = track_object["artistName"]
    track_name = track_object["trackName"]
    ms_played = track_object["msPlayed"]

    track_key = track_name + " - " + artist_name

    # Adjust skipped tracks
    if ms_played < 10000:
        # Most skipped tracks
        if track_key in most_skipped_track_dict:
            most_skipped_track_dict[track_key] += 1
        else:
            most_skipped_track_dict[track_key] = 1
    else:
        # Adjusted track counts
        if track_key in most_played_track_dict_adjusted:
            most_played_track_dict_adjusted[track_key] += 1
        else:
            most_played_track_dict_adjusted[track_key] = 1

        # Adjusted artist counts
        if artist_name in most_played_artists_dict_adjusted:
            most_played_artists_dict_adjusted[artist_name] += 1
        else:
            most_played_artists_dict_adjusted[artist_name] = 1

    # Raw track counts
    if track_key in most_played_track_dict_raw:
        most_played_track_dict_raw[track_key] += 1
    else:
        most_played_track_dict_raw[track_key] = 1

    # Raw artist counts
    if artist_name in most_played_artists_dict_raw:
        most_played_artists_dict_raw[artist_name] += 1
    else:
        most_played_artists_dict_raw[artist_name] = 1

most_skipped_track_dict = sort_dict(most_skipped_track_dict)

output_dict = {}

never_played_tracks_dict = {}
for track in most_skipped_track_dict:
    if most_played_track_dict_raw[track] == most_skipped_track_dict[track]:
        never_played_tracks_dict[track] = most_played_track_dict_raw[track]

most_played_track_dict_raw = sort_dict(most_played_track_dict_raw)
never_skipped_tracks_dict = {}
for track in most_played_track_dict_raw:
    if track not in most_skipped_track_dict:
        never_skipped_tracks_dict[track] = most_played_track_dict_raw[track]
most_never_skipped = get_top_ten(never_skipped_tracks_dict, count = 25)

play_to_skip_ratio = {}
for track in most_played_track_dict_raw:
    if track in most_skipped_track_dict:
        play_to_skip_ratio[track] = most_played_track_dict_raw[track] / most_skipped_track_dict[track]

play_to_skip_ratio = sort_dict(play_to_skip_ratio)
highest_play_to_skip_ratio = get_top_ten(play_to_skip_ratio, count = 35)

best_songs = {**most_never_skipped, **highest_play_to_skip_ratio}
best_songs = sort_dict(best_songs)

most_played_track_dict_adjusted = sort_dict(most_played_track_dict_adjusted)

# Trying to find my favorite songs... I just can't figure out the proper logic for this. It's not very good.

# best_songs = {}
# fake_ratio = {}
# for track in most_played_track_dict_raw:
#     fake_ratio[track] = most_played_track_dict_raw[track] / 1
#
# combined = play_to_skip_ratio.copy()
# for track in combined:
#     if fake_ratio[track] > combined[track]:
#         combined[track] = fake_ratio[track]
#
# combined = sort_dict(combined)
# for index, key in enumerate(combined.keys()):
#     if index >= 25:
#         break
#     best_songs[key] = most_played_track_dict_adjusted[key]
#
# best_songs = sort_dict(best_songs)

most_played_raw_list = get_top_ten(most_played_track_dict_raw)
most_played_adjusted_list = get_top_ten(most_played_track_dict_adjusted)
output_played = {"most_played_raw": most_played_raw_list, "most_played_adjusted": most_played_adjusted_list, "played_raw": most_played_track_dict_raw, "played_adjusted": most_played_track_dict_adjusted}
output_dict["played"] = output_played

most_played_artists_dict_raw = sort_dict(most_played_artists_dict_raw)
most_played_artists_dict_adjusted = sort_dict(most_played_artists_dict_adjusted)
most_played_artists_raw_list = get_top_ten(most_played_artists_dict_raw)
most_played_artists_adjusted_list = get_top_ten(most_played_artists_dict_adjusted)

output_artists = {"most_played_artists_raw": most_played_artists_raw_list, "most_played_artists_adjusted": most_played_artists_adjusted_list, "artists_raw": most_played_artists_dict_raw, "artists_adjusted": most_played_artists_dict_adjusted}
output_dict["artists"] = output_artists

most_skipped_list = get_top_ten(most_skipped_track_dict)
output_skipped = {"most_skipped": most_skipped_list, "most_never_skipped": most_never_skipped, "highest_play_to_skip_ratio": highest_play_to_skip_ratio, "skipped_tracks": most_skipped_track_dict, "never_skipped": never_skipped_tracks_dict,
                  "never_played": never_played_tracks_dict, "play_to_skip_ratio": play_to_skip_ratio}
output_dict["skipped"] = output_skipped

highlights = {}
highlights["most_played_adjusted"] = most_played_adjusted_list
highlights["most_played_artists_adjusted"] = most_played_artists_adjusted_list

highlights["most_skipped"] = most_skipped_list
highlights["most_never_skipped"] = most_never_skipped
highlights["highest_play_to_skip_ratio"] = highest_play_to_skip_ratio

highlights["top_songs"] = best_songs

highlights["most_played_raw"] = most_played_raw_list
highlights["most_played_artists_raw"] = most_played_artists_raw_list

highlights_file = Path.cwd() / "highlights.json"
highlights_file.write_text(json.dumps(highlights, indent = 4, ensure_ascii = False), encoding = "utf8")

output_file.write_text(json.dumps(output_dict, indent = 4, ensure_ascii = False), encoding = "utf8")
