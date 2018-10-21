#The Riddler: Toddler Poker 2017-02-10
#Monte Carlo simulation with optimal strategies

import random

Nsim = 10000000 #number of simulations

winningsA = 0
winningsB = 0

for n in range(0, Nsim):
    #roll die
    cardA = random.random()
    cardB = random.random()

    #Determine A's action using optimal strategy
    if (cardA >= 0.7 or cardA < 0.1):
        callA = False
    else:
        callA = True

    #Determine B's action using optimal strategy
    if (cardB >= 0.4):
        callB = True
    else:
        callB = False

    #Determine winnings
    if (callA): #A calls
        if (cardA > cardB):
            winningsA += 1
            winningsB += -1
        elif (cardA < cardB):
            winningsA += -1
            winningsB += 1
    else: #A raises
        if (callB): #B calls
            if (cardA > cardB):
                winningsA += 2
                winningsB += -2
            elif (cardA < cardB):
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
