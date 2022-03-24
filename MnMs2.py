import random
kleuren = ["oranje","blauw","groen","bruin"]

HoeveelMnMs = int(input("Hoeveel verschillende m&m's zou u in de zak willen? "))

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
    print(MnMZak1)


MnMZak(HoeveelMnMs)