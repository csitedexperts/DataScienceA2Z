class classThings():
    def test(hi):
        print "Hi"

t = classThings()
t.test()
t.test()


class Song(object):
    mysong = "Bangla Song"
    yoursong = "English Song"
    
    def __init__(self, lyric):
        self.lyric = lyric

              
        #lyric = self.lyric  # this is NOT a valid statement

    def sing_me_a_song(self):
        for line in self.lyric:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

print "\n\n"
s = Song("")
print s.mysong
print s.yoursong

s.mysong = "Bangla Old Song"
s.yoursong = "English Folk"

print s.mysong
print s.yoursong



print "\n>>How about ?? >>\n"
print Song("").mysong
print Song('').yoursong


print "\n>>How about ?? >>\n"
print Song("Kobita ").mysong
print Song('Poen.. ').yoursong

print "\n\n Ah ha....\n\n"
print s.mysong
print s.yoursong


print "\n>Also >>>\n"
print Song.mysong
print Song.yoursong


