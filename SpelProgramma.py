import random
spelletjes = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet','Cluedo']
Minimaal = 3
Maximaal = 10
def spelProgramma(Spellen,Minimaal,Maximaal):
    randomGetal = random.randint(Minimaal,Maximaal)
    for i in range(randomGetal):
        randomspel = random.choice(Spellen)
        print(randomspel)
spelProgramma(spelletjes,Minimaal,Maximaal)