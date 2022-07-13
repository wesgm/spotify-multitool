import spotipy
import requests
import json
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

SPOTIPY_CLIENT_ID="***REMOVED***"
SPOTIPY_CLIENT_SECRET="***REMOVED***"
SPOTIPY_REDIRECT_URI="http://127.0.0.1:9090"
SCOPE = "user-top-read"

sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = SPOTIPY_CLIENT_ID, client_secret= SPOTIPY_CLIENT_SECRET, redirect_uri =SPOTIPY_REDIRECT_URI, scope = SCOPE))
def get_ids(results_dict):
		ids=[]
		for item in results["items"]:
			ids.append(item["id"])
		return ids
#class for tracks to store data about them
class Track:
	def __init__(self, track_id, i):
		trackJSONEntry = sp.track(track_id)
		#the id of the track in spotify system
		self.id=track_id
		#name of the track
		self.name = trackJSONEntry["name"]
		#cover art for the album 
		self.coverArt = trackJSONEntry["album"]["images"][0]["url"]
		#artist name 
		self.artist = trackJSONEntry["album"]["artists"][0]["name"]
		#name of album the track is on
		self.album = trackJSONEntry["album"]["name"]
		#rank of track in the last month
		self.rank=i
def initTracks(track_ids):
		tracks = [] 
		for i, id in enumerate(track_ids):
			tracks.append(Track(id, i))
		return tracks

#get ids of top 50 tracks in last month
results = sp.current_user_top_tracks(time_range = "short_term", limit = 50)
ids = get_ids(results_dict = results)
print(ids)
tracks = initTracks(ids)
for track in tracks:
	print(track.name + " " + track.artist + " " + str(track.rank))