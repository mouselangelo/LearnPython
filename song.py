class Song(object):
    ## docstring i.e. __doc__
    "'Song' is a custom class representing a song"
    
    type = "song"

    def __init__(self, title = "untitled", artist = "unknown", playCount = 0):
        """Initialize a 'Song' with (optional) 'title', 'artist' and/or 'playCount'
default values: title = "untitled", artist = "unknown", playCount = 0. """
        self.title = title
        self.artist = artist
        self.playCount = playCount

    def play(self):
        "\"plays\" a song and increments it's 'playCount'"
        self.playCount+=1

    def describe(self):
        "prints the description of a song"
        print("Song '%(title)s' by '%(artist)s', played %(playCount)s time(s)'" % ({"title": self.title, "artist": self.artist, "playCount": self.playCount}))