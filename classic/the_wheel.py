#The Riddler Classic 2017-10-27: The Wheel
#Monte-Carlo simulation of optimal strategies

import random

Nsim = 1000000 #number of simulations
counts = [0]*3 #count victories for each player

wheel = [(i + 1)*5 for i in range(20)]
def spin():
    return wheel[random.randint(0, 19)]

thres1 = 65
thres2 = 50

for N in range(Nsim):
    total1 = 0
    total2 = 0
    total3 = 0

    total1 += spin()
    #player 1 optimal strategy
    if (total1 <= thres1):
        total1 += spin()

    if (total1 > 100): #player 1 lost
        total1 = 0

    total2 += spin()
    #player 2 optimal strategy
    if (total2 < total1):
        total2 += spin()
    elif (total2 == total1 and total2 <= thres1):
        total2 += spin()
    elif (total2 <= thres2):
        total2 += spin()

    if (total2 > 100): #player 2 lost
        total2 = 0

    total3 += spin()
    #player 3 optimal strategy
    if (total3 < max(total1, total2)):
        total3 += spin()
    elif (total3 == max(total1, total2) and total1 == total2 and total3 <= thres1):
        total3 += spin()
    elif (total3 == max(total1, total2) and total3 <= thres2): 
        total3 += spin()

    if (total3 > 100): #player 3 lost
        total3 = 0
        
    #determine winner
    if (total1 > max(total2, total3)): #player 1 won
        counts[0] += 1
    elif (total2 > max(total1, total3)): #player 2 won
        counts[1] += 1
    elif (total3 > max(total1, total2)): #player 3 won
        counts[2] += 1
    elif (total1 == total2 and total1 > total3): #player 1 and 2 tied
        if (random.random() < 0.5):
            counts[0] += 1
        else:
            counts[1] += 1
    elif (total1 == total3 and total1 > total2): #player 1 and 3 tied
        if (random.random() < 0.5):
            counts[0] += 1
        else:
            counts[2] += 1
    elif (total2 == total3 and total2 > total1): #player 2 and 3 tied
        if (random.random() < 0.5):
            counts[1] += 1
        else:
            counts[2] += 1
    else: #all tied
        if (random.random() < 1/3):
            counts[0] += 1
        elif (random.random() < 2/3):
            counts[1] += 1
        else:
            counts[2] += 1

print('Player 1 win chance:')
print(counts[0]/Nsim)
print('Player 2 win chance:')
print(counts[1]/Nsim)
print('Player 3 win chance:')
print(counts[2]/Nsim)
