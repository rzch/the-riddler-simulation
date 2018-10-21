#The Riddler Express 2017-01-20: First Flipper Advantage
#Monte-Carlo simulation

import random

Nsim = 1000000 #number of simulations

winsA = 0

x = 10 #number of heads required in a row to win

for n in range(0, Nsim):

    countA = 0
    countB = 0

    while(countA < x and countB < x):
        #simulate a coin flip and add to tally of heads
        countA += random.getrandbits(1)

        if (countA == x): #stop game if A wins
            winsA += 1
            break

        countB +=  random.getrandbits(1)


print('Proportion of first player winning:')
print(winsA/Nsim)
