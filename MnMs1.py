import random
kleuren = ["oranje","blauw","groen","bruin"]

HoeveelMnMs = int(input("Hoeveel verschillende m&m's zou u in de zak willen? "))

def ZakMetMnMs(Hoeveelheid):
    ZakMnM = []
    for i in range(Hoeveelheid):
        kleur = random.choice(kleuren)
        ZakMnM.append(kleur)
    print(ZakMnM)


ZakMetMnMs(HoeveelMnMs)