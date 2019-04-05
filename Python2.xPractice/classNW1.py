
class Song(object):

    self.lyric = Song()
    
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    
    def sing_a_song():
        for line in lyric:
            print line

    lyric1 = ["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"]
    
    lyric2 = ["They rally around the family",
                        "With pockets full of shells"]
    
    
birthday_song = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

paradey_song = Song(["They rally around the family",
                        "With pockets full of shells"])

birthday_song.sing_me_a_song()

paradey_song.sing_me_a_song()

lyric1.sing_a_song()
lyric2.sing_a_song()


