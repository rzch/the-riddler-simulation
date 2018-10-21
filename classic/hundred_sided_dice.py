#The Riddler: Hundred-Sided Dice 2017-01-13
#Monte Carlo Simulation

import random

Nsim = 1000000 #Number of simulations
rolls = 0

for n in range(0, Nsim):
    prevroll = random.randint(1, 100)
    rolls += 1

    newroll = random.randint(1, 100)
    rolls += 1

    #Keep rolling until game ends
    while (newroll >= prevroll):
        prevroll = newroll

        newroll = random.randint(1, 100)
        rolls += 1

print('Expected number of rolls:')
print(rolls/Nsim)
