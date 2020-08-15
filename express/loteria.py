# The Riddler Classic 2019-05-31: Loteria
# https://fivethirtyeight.com/features/can-you-win-the-loteria/
# Monte-Carlo simulation

import random

Nsim = 1000000 #number of simulations

D = 20 #size of deck
deck = list(range(D))

G = 3 #number of images on the grid

count = 0
for N in range(Nsim):

    #generate random grid
    grid1 = random.sample(deck, G)
    grid2 = random.sample(deck, G)

    #play game until winner
    while (len(grid1) > 0 and len(grid2) > 0):

        c = random.randint(0, D - 1)

        grid1 = [i for i in hand1 if i != c]
        grid2 = [i for i in hand2 if i != c]

    #check if grid untouched
    if (len(grid1) == G or len(grid2) == G):
        count += 1


print(count/Nsim)
