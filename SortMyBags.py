import random
kleuren = ["oranje","blauw","groen","bruin"]

HoeveelMnMs = int(input("Hoeveel verschillende m&m's zou u in de zak willen? "))

def ZakMetMnMs(Hoeveelheid):
    ZakMnM = []
    for i in range(Hoeveelheid):
        kleur = random.choice(kleuren)
        ZakMnM.append(kleur)
    ZakMnM.sort()
    print(ZakMnM)


ZakMetMnMs(HoeveelMnMs)


def MnMZak(Hoeveelheid):
    MnMZak1 = {
        "oranje": 0,
        "blauw": 0,
        "groen": 0,
        "bruin": 0
    }
    for i in range(Hoeveelheid):
        kleur = random.choice(kleuren)
        MnMZak1[kleur] +=1
    MnMZak2 = dict(sorted(MnMZak1.items(),key=lambda x:x[0],reverse = True))
    print(MnMZak2)


MnMZak(HoeveelMnMs)