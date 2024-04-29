import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth


def initialize_spotify():
    load_dotenv()
    client_id = os.getenv("CLIENT_ID")
    client_secret = os.getenv("CLIENT_SECRET")

    scope = "user-library-read, user-read-currently-playing, user-read-playback-state, user-modify-playback-state"

    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret,
                                                   redirect_uri="http://localhost:3000"))
    return sp


def get_current_track(sp):
    current_track = sp.current_playback()
    track_id = current_track['item']['id']
    return track_id


def get_track_info(track_id, sp):
    info = sp.track(track_id)
    track_info = {'artist': info['artists'][0]['name'],
                  'track': info['name'],
                  'album': info['album']['name'],
                  'album_image': info['album']['images'][0]['url']}
    return track_info

