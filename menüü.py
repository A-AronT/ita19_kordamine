from laul import Laul
from album import Album
from laulja import Laulja
tabel = []
albumid = []
lauljad = []
albumid_olemas = []
lauljad_olemas = []
fail=open("albumid.txt", encoding="UTF-8")
for rida in fail:
    tabel.append(rida.strip().split("\t"))
fail.close()
for i in tabel:
    if i[1] not in albumid_olemas:
        temp = Album(i[1],i[2],i[0])
        albumid.append(temp)
        albumid_olemas.append(i[1])
    if i[0] not in lauljad_olemas:
        temp = Laulja(i[0])
        lauljad.append(temp)
        lauljad_olemas.append(i[0])
    teemp = Laul(i[3], i[0])
    for i in albumid:
        if i.laulja == teemp.laulja:
            i.lisa_laul(teemp)
for i in albumid:
    for j in lauljad:
        if i.laulja == j.nimi:
            j.lisa_album(i)