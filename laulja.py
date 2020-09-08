class Laulja:

    def __init__(self, nimi):
        self.nimi = nimi
        self.laulud = []
        self.albumid = []

    def lisa_album(self, album):
        self.albumid.append(album)
        for i in album.laulud:
            self.laulud.append(i)
