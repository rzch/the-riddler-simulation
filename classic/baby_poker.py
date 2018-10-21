#The Riddler: Baby Poker 2016-12-30
#Monte Carlo simulation with optimal strategies

import random

Nsim = 2000000 #number of simulations

winningsA = 0
winningsB = 0

for n in range(0, Nsim):
    #roll die
    diceA = random.randint(1, 6)
    diceB = random.randint(1, 6)

    #Determine A's action using optimal strategy
    if (diceA >= 5):
        callA = False
    elif (diceA >= 2):
        callA = True
    else:
        if (random.random() <= 2/3):
            callA = False
        else:
            callA = True

    #Determine B's action using optimal strategy
    if (diceB >= 5):
        callB = True
    elif (diceB >= 2):
        if (random.random() <= 5/9):
            callB = True
        else:
            callB = False
    else:
        callB = False

    #Determine winnings
    if (callA): #A calls
        if (diceA > diceB):
            winningsA += 1
            winningsB += -1
        elif (diceA < diceB):
            winningsA += -1
            winningsB += 1
    else: #A raises
        if (callB): #B calls
            if (diceA > diceB):
                winningsA += 2
                winningsB += -2
            elif (diceA < diceB):
                winningsA += -2
                winningsB += 2
        else: #B Folds
            winningsA += 1
            winningsB += -1

#Compute and print expectations
print('Expected winnings of A')
print(winningsA/Nsim)
print('Expected winnings of B')
print(winningsB/Nsim)
