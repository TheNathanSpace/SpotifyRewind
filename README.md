# Spotify Rewind

Spotify Wrapped was good, but I felt like I lacked the *real* data. I saw so many places where it fell short, and a lot of them were specific to my habits, so I felt I could make a better summary of the year by analyzing the data myself.

You can see my Spotify Rewind highlights in `highlights.json`! If you want to try it yourself, follow the instructions below.

## Instructions

### Request Spotify Data

You can request to download your Spotify data from your account's [privacy page](https://www.spotify.com/ca-en/account/privacy/). Once you get the download link, it'll download it as the file `my_spotify_data.zip`. Extract `my_spotify_data.zip`, and you should have a folder named `my_spotify_data/MyData`, then a bunch of `.json` files.

### Download the Program

1. Open `spotify_rewind.py` by clicking it above.

2. Click "Raw".

3. Save the page to your computer using the method below (Windows):

    a. Right click  / `Ctrl+S`
   
    b. "Save page as"
    
    c. Save the file:
   
        i. "Save type as"
   
        ii. "Text file (\*.txt, \*.text)" (near the bottom)
   
        iii. "All files (\*.\*)"
   
        iv. "Save"

### Setup / Execution
Place `spotify_rewind.py` in the same directory level as the folder `my_spotify_data`. You'll need at least [Python 3.0](https://www.python.org/downloads/). Then, run `spotify_rewind.py`, and it'll generate two files:

 - `data.json` (corresponds to "Full data on")
 
 - `highlights.json` (corresponds to "Highlights (top ten) on")
 
These files correspond to sections described below.

### Terminology

For the purpose of this description, an *instance* is a time that the track was played. Each time a track is played, Spotify stores it, and you can download it as `StreamingHistory0.json`.

When a value is *adjusted*, that means instances that are played for less than 10 seconds aren't counted.

### Data

All data is sorted by the number of instances applicable to it.

#### Full data on:

 - Played tracks
 
 - Played tracks (adjusted for skipped songs)
 
 - Played artists
 
 - Played artists (adjusted for skipped songs)
 
 - Skipped tracks
 
 - Never skipped tracks
 
 - *Always* skipped tracks
 

#### Highlights (top ten) on:

 - Most played tracks (adjusted for skipped songs)
 
 - Most played artists (adjusted for skipped songs)
 
 - Most skipped tracks
 
 - Most played while never being skipped
 
 - Most played tracks
 
 - Most played artists