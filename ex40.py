class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                   "I dont want to get sued",
                   "So Ill stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

class Pesma(object):

    def __init__(self, reci):
        self.reci = reci

    def otpevaj_mi_pesmu(self):
        for line in self.reci:
            print(line)

pesmica = Pesma(["Ovako zvuci",
                 "Pesma ova",
                 "Zanemari sto je ruzna"])

pesmica.otpevaj_mi_pesmu()