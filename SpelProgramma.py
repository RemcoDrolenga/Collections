import random
spelletjes = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet','Cluedo']
def spelProgramma(Spellen):
    randomGetal = random.randint(3,10000)
    for i in range(randomGetal):
        randomspel = random.choice(Spellen)
        print(randomspel)


spelProgramma(spelletjes)