import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

scope = "user-library-read, user-read-currently-playing, user-read-playback-state, user-modify-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret,
                                               redirect_uri="http://localhost:3000"))


def get_current_track():
    current_track = sp.current_playback()
    track_id = current_track['item']['id']
    return track_id


def get_track_info(track_id):
    info = sp.track(track_id)
    track_info = {'artist': info['artists'][0]['name'],
                  'track': info['name'],
                  'album': info['album']['name'],
                  'album_image': info['album']['images'][0]['url']}
    return track_info


#curr_track = get_current_track()
#track_information = get_track_info(curr_track)
#print(track_information)
#resized_image = resize_image_and_get_pixel_values(track_information['album_image'], (30, 30))
#print(resized_image)




