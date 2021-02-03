# The Riddler Classic 2019-12-06: Favourite Song
# https://fivethirtyeight.com/features/how-fast-can-you-skip-to-your-favorite-song/
# Monte-Carlo simulation of optimal strategy

import random

Nsim = 1000000 #number of simulations

presses = [0]*Nsim

for N in range(Nsim):
    
    c = 0
    #initial song
    r = random.randint(1, 100)

    while(r != 42):

        if (r >= 29 and r <= 41): #next button
            r += 1
            c += 1
        else: #random button
            r = random.randint(1, 100)
            c += 1

    presses[N] = c

print(sum(presses)/Nsim)
