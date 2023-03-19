"""
Full solution to the Loudest Scream problem from the 2023 IMC x CSESoc x CPMSoc 
Coding Competition Advanced Division.

This solution was written by my teammate.
"""



KandJ = input()
KandJ = KandJ.split(" ")
k = int(KandJ[0])
j = int(KandJ[1])

countA = 0
countB = 0
loudestScream = 0
lowestScream = 0

while (countA < k):
    currScream = 0
    over100 = False
    inputScream = input()
    inputScream = inputScream.split(" ")
    while (countB < j):
        if (float(inputScream[countB]) > 100):
            over100 = True
        currScream = currScream + float(inputScream[countB])
        countB += 1
    currScream = currScream / j
    if (currScream <= 100 and currScream > loudestScream and not(over100)):
        loudestScream = round(currScream)
    if (lowestScream == 0):
        lowestScream = round(currScream)
    elif (currScream < lowestScream):
        lowestScream = round(currScream)
    countB = 0

    countA += 1

if (loudestScream == 0):
    print(lowestScream)
else:
    print(loudestScream)
