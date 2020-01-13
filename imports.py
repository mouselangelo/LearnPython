from song import Song

songEagles = Song("Hotel California", "Eagles")
songBeatles = Song(title = "Can't buy me love" , artist = "The Beatles")

for number in range(5):
    songEagles.play()

    if number == 3:
        songBeatles.play()

songEagles.describe()
songBeatles.describe()

print("")
print(".type:")
print("songEagles.type: %s" % songEagles.type)
print("Song.type: %s" % Song.type)

print("")
print("Documentation:")
print("class Song: %s" % Song.__doc__)
print("Song.__init__: %s" % Song.__init__.__doc__)
print("Song.play: %s" % Song.play.__doc__)
print("Song.describe: %s" % Song.describe.__doc__)