from laul import Laul
from album import Album
from laulja import Laulja
tabel = []
albumid = []
lauljad = []
albumid_olemas = []
lauljad_olemas = []
#tekitan 2 listi kuhu panna muutujaid ja 2 listi, millega jälgida olemasolevaid muutujaid.
fail=open("albumid.txt", encoding="UTF-8")
for rida in fail:
    tabel.append(rida.strip().split("\t")) #lisan albumid.txt sisu tabelisse lihtsamaks kasutamiseks
fail.close()
for i in tabel:
    if i[1] not in albumid_olemas: #kontrollin kas see album on juba objektina tekitatud
        temp = Album(i[1],i[2],i[0]) #teen albumist objekti
        albumid.append(temp)
        albumid_olemas.append(i[1]) #lisan objekti päris ja kontrollimise listi
    if i[0] not in lauljad_olemas:#sama asi mis albumitega nüüd lauljatega.
        temp = Laulja(i[0])
        lauljad.append(temp)
        lauljad_olemas.append(i[0])
    teemp = Laul(i[3], i[0], i[1])#siin muudan laulu objektiks
    for i in albumid:
        if i.pealkiri == teemp.album:#kontrollin kas laulu album ja albumi pealkiri on samad
            i.lisa_laul(teemp)#kui on siis lisan laulu albumisse
for i in albumid:
    for j in lauljad:
        if i.laulja == j.nimi:#kontrollin kõikide albumitega läbi kõik lauljad ja lisan sobivuse korral albumi listi
            j.lisa_album(i)
print(" 1 - Väljasta failist kõik asjad \n 2 - Otsida faile albumi pealkirja või aasta järgi "
      "\n 3 - Otsida laule nime järgi \n 4 - Otsida failist albumid laulja järgi")
choice = input("Vali 1-4: ")#lasen kasutajal valida mida ta teha tahab
if choice == "1":#võtan ette albumite nimekirja ja prindin julmalt informatsiooni
    for i in albumid:
        print(" Albumi pealkiri: " + i.pealkiri)
        for j in i.laulud:
            print(j.pealkiri)
        print(" Laulja: " + i.laulja)
        print(" Aasta: " + i.aasta)
        print("--------")
elif choice == "2":
    otsing = input(" Sisesta kas albumi pealkiri või aasta: ").lower()
    for i in albumid:
        if otsing in i.pealkiri.lower() or otsing in i.aasta:
            print(" Otsingu tulemus (väljastatakse leitud albumite nimed): ")
            print(i.pealkiri)
elif choice == "3":
    otsing = input(" Sisesta laulu nimi: ").lower()
    for i in albumid:
        for j in i.laulud:
            if otsing in j.pealkiri.lower():#teen topelt tsükli et kasutada laulu ja albumi infot
                print(" Laul nimega - " + j.pealkiri + " - Leidub albumis: " + i.pealkiri + "\n Laulja on: " + i.laulja + "\n Aasta on: " + i.aasta)
elif choice == "4":
    otsing = input(" Sisesta laulja nimi: ").lower()
    for i in lauljad:
        if otsing in i.nimi.lower():
            print(" Laulja nimega - " + i.nimi + " - on välja andnud albumid: ")
            for j in i.albumid:
                print(j.pealkiri + " - Aastal " + j.aasta)