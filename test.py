from random import randint


class Sodur:
    tervis = 100


sodur_1 = Sodur()
sodur_2 = Sodur()


def kaklus(esimene, teine):
    a = randint(0, 100)
    b = randint(0, 100)
    if a > b:
        teine.tervis -= 20
        print("sodur 2 sai haiget, tal on alles jäänud " + str(teine.tervis) + " tervist")
    elif b > a:
        esimene.tervis -= 20
        print("sodur 1 sai haiget, tal on alles jäänud " + str(esimene.tervis) + " tervist")
    else:
        esimene.tervis -= 20
        teine.tervis -= 20
        print("sodurid said mõlemad haiget,1 elud " + str(esimene.tervis) + "ja 2 " + str(teine.tervis))


while sodur_1.tervis and sodur_2.tervis > 0:
    kaklus(sodur_1, sodur_2)

if sodur_1.tervis == 0:
    print("Võitja on sodur 2, tal on alles " + str(sodur_2.tervis) + " tervist")
else:
    print("Võitja on sodur 1, tal on alles " + str(sodur_1.tervis) + " tervist")
