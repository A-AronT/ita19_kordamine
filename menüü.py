from laul import Laul
from album import Album
from laulja import Laulja
tabel = []
fail=open("albumid.txt")
for rida in fail:
    tabel.append(rida.split("/t"))
for i in tabel:
    print(i)
