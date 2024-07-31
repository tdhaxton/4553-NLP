import pandas as pd

spotify = pd.read_csv("spotify.csv", sep = ",")

#print(spotify.info())

# explicit = spotify.query("`Explicit Track` == 1")
# print(len(explicit))

# most_viewed = spotify.sort_values(by = "YouTube Views", ascending = False)
# print(most_viewed.head(3))

# spotify_streams = spotify.sort_values(by = "Spotify Streams", ascending = False)
# print(spotify_streams.max("Spotify Streams"))

tiktok = spotify.query("`TikTok Posts` == 0")
print(len(tiktok))

# taytay = spotify.
# print(len(taytay))