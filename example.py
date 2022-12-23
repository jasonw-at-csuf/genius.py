import os
from genius_builder import *
from dotenv import load_dotenv

# Example uses dotenv to load environment variables from .env file
# See https://pypi.org/project/python-dotenv/
load_dotenv()

# Get environment variables
client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')
client_access_token = os.getenv('CLIENT_ACCESS_TOKEN')

# Create a GeniusBuilder object
genius = GeniusBuilder(client_id=client_id, client_secret=client_secret, client_access_token=client_access_token)

# Returns a list of songs containing query
print(genius.search(query='Kendrick Lamar')[0])

# Returns song matching song ID
print(genius.search_by_id(378195))

# Returns an Artist object containing all songs by artist
artist = genius.search_artist(artist_id=16775)
for song in artist.list_tracks():
    print(song)