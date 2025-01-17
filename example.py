from geniusdotpy.genius_builder import GeniusBuilder

# Get your client access token from https://genius.com/api-clients
client_access_token = "token"

# Create a GeniusBuilder object
genius = GeniusBuilder(client_access_token=client_access_token)

# Returns a list of songs containing query
print(genius.search(query="Kendrick Lamar")[0])

# Returns an Artist object containing all songs by artist
artist = genius.search_artist(artist_id=16775)
print(artist.tracks[0])

# Returns song matching song ID
track = genius.search_by_id(185931)
print(track)
if hasattr(track, "album"):
    print(f"Album: {track.album}")
if hasattr(track, "youtube_url"):
    print(f"Youtube URL: {track.youtube_url}")
if hasattr(track, "spotify_url"):
    print(f"Spotify URL: {track.spotify_url}")
if hasattr(track, "soundcloud_url"):
    print(f"Soundcloud URL: {track.soundcloud_url}")

# Prints the lyrics of the song
print(f"Lyrics:\n{track.lyrics}")

# Print track's album json
print(track.album.to_json())

# Search for an album
album = genius.search_album(album_id=378195)
print(album.name)
