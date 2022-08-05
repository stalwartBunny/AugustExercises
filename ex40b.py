class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_birthday = Song(["Happy Birthday to you.",
                        "You live in a zoo.",
                        "With the lions and tigers",
                        "and the fat lady too."])

bulls_on_parade = Song(["They rally round the family,",
                         "with a pocket full of shells."])

happy_birthday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
