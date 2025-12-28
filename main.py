from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
load_dotenv()
URL = "https://www.billboard.com/charts/hot-100/"

response = requests.get(URL)
code = response.text
soup = BeautifulSoup(code,'html.parser')

titles = soup.find_all(name='li' , class_="o-chart-results-list__item")
title_text=[]
for title in titles:
    heading = title.find(name='h3' ,id="title-of-a-story")
    title_text.append(heading)
tt = []
cleaned_title_text = [item for item in title_text if item is not None]
for title in cleaned_title_text:
    tt.append(title.getText().strip())


with open("Top_Songs.txt","w") as txt:
    for song_title in tt:
        txt.write(f"{song_title}\n")


import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private playlist-modify-public"
    )
)

user = sp.current_user()
user_id = user["id"]
# print("Logged in as:", user["display_name"])

playlist = sp.user_playlist_create(
    user=user_id,
    public=False,
    name="Top 100 songs of recent Times",
    description= "Made using Python API called spotipy"
)
playlist_id = playlist['id']

with open("Top_Songs.txt") as songs:
    all_songs=songs.readlines()
print(all_songs)
for song in all_songs:
    song = song.strip()
    result = sp.search(q=song,type="track",limit=1)
    tracks = result["tracks"]["items"]
    if tracks:
        track_uri = tracks[0]["uri"]

        sp.playlist_add_items(
            playlist_id=playlist_id,
            items=[track_uri]
        )
        print("Song Added")
    else:
        print("Not Found")
