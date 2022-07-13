import spotipy
import requests
import json
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID="***REMOVED***"
SPOTIPY_CLIENT_SECRET="***REMOVED***"
SPOTIPY_REDIRECT_URI="http://127.0.0.1:9090"
SCOPE = "user-top-read"
sp = spotipy.Spotify(auth_manager = SpotifyOAuth(client_id = SPOTIPY_CLIENT_ID, client_secret= SPOTIPY_CLIENT_SECRET, redirect_uri =SPOTIPY_REDIRECT_URI, scope = SCOPE))
def get_top_artists_from_api():
	return sp.current_user_top_artists(time_range = "short_term", limit = 50)
def get_ids(artists_dict):
	ids=[]
	for artist in artists_dict["items"]:
		ids.append(artist["id"])
	return ids
class Artist:
	def __init__(self, artist_id, artist_rank):
		artistJSON = sp.artist(artist_id) 
		self.id = artist_id 
		self.rank = artist_rank 
		self.name = artistJSON["name"]
		self.genres = artistJSON["genres"]
		self.image = artistJSON["images"][0]["url"]
def init_artists(artist_ids):
		artists = [] 
		for i, id in enumerate(artist_ids):
			artists.append(Artist(id, i))
		return artists
def get_top_artists():
	#get ids of top 50 tracks in last month
	results = get_top_artists_from_api()
	ids = get_ids(results)
	#print(ids)
	artists = init_artists(ids)
	return artists
