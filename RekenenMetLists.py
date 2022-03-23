ListOne = [1,2,3,4,5,6,7,8,9,10]
ListTwo = [2,4,6,8,10,12,14,16,18,20]
Uitkomst = []

def addAndDisplayLists():
    for i1,i2 in zip(ListOne,ListTwo):
        Uitkomst.append(i1+i2)
    for i in range(len(Uitkomst)):
        print(ListOne[i],"+",ListTwo[i],"=",Uitkomst[i])
# addAndDisplayLists()

def substractAndDisplayLists():
    for i1,i2 in zip(ListOne,ListTwo):
        Uitkomst.append(i1-i2)
    for i in range(len(Uitkomst)):
        print(ListOne[i],"-",ListTwo[i],"=",Uitkomst[i])
# substractAndDisplayLists()

def multiplyAndDisplayLists():
    for i1,i2 in zip(ListOne,ListTwo):
        Uitkomst.append(i1*i2)
    for i in range(len(Uitkomst)):
        print(ListOne[i],"*",ListTwo[i],"=",Uitkomst[i])
# multiplyAndDisplayLists()

def divideAndDisplayLists():
    for i1,i2 in zip(ListOne,ListTwo):
        Uitkomst.append(i1/i2)
    for i in range(len(Uitkomst)):
        print(ListOne[i],"/",ListTwo[i],"=",Uitkomst[i])
divideAndDisplayLists()