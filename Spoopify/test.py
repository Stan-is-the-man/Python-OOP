from Spoopify.album import Album
from Spoopify.band import Band
from Spoopify.song import Song

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())

second_song = Song("Around the World", 2.34, False)
album = Album("Initial D", song, second_song)
print(album.details())
print(album.publish())

band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())
