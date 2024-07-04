from flask import Flask, render_template, request, redirect
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
grooveguide = Flask(__name__)
SPOTIPY_CLIENT_ID = 'your_client_id'
SPOTIPY_CLIENT_SECRET = 'your_client_secret'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))
mood_playlists = {
    "happy": "hhttps://open.spotify.com/search/happy/playlists",
    "sad": "https://open.spotify.com/search/sad/playlists",
    "angry": "https://open.spotify.com/search/angry/playlists",
    "relaxed": "https://open.spotify.com/search/relaxed/playlists",
    "soft": "https://open.spotify.com/search/soft/playlists",
    "romance": "https://open.spotify.com/search/romance/playlists",
    "workout": "https://open.spotify.com/search/workout/playlists",
    "emotional": "https://open.spotify.com/search/emotional/playlists",
    "rainy":  "https://open.spotify.com/search/rainy/playlists",
    "nostalgia": "https://open.spotify.com/search/nostalgia/playlists",
    "driving": "https://open.spotify.com/search/driving/playlists",
    "breakup": "https://open.spotify.com/search/breakup/playlists",
    "shower": "https://open.spotify.com/search/shower/playlists",
    "crying": "https://open.spotify.com/search/crying/playlists",
    "bollywood": "https://open.spotify.com/search/bollywood/playlists",
    "dance": "https://open.spotify.com/search/dance/playlists",
    "party": "https://open.spotify.com/search/party/playlists",
    "lonely": "https://open.spotify.com/search/lonely/playlists",
    "rage": "https://open.spotify.com/search/rage/playlists",
    "fun": "https://open.spotify.com/search/fun/playlists",
}

@grooveguide.route("/", methods=["GET", "POST"])
def index():
    song = None

    if request.method == "POST":
        user_input = request.form["user_input"].lower()
        if user_input in mood_playlists:
            mood = user_input            
            return redirect(f"/mood/{mood}")

    return render_template("index.html", song=song)

@grooveguide.route("/mood/<mood>", methods=["GET"])
def redirect_to_spotify(mood):
    playlist_url = mood_playlists.get(mood)

    if playlist_url:
        return redirect(playlist_url)
    else:
        return "Playlist not found"

if __name__ == "__main__":
    grooveguide.run(debug=True)
