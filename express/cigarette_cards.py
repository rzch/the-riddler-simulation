#The Riddler Express 2019-03-01: Cigarette Cards
#https://fivethirtyeight.com/features/youre-home-alone-you-can-buy-zillions-of-video-game-cigarettes-or-beat-yourself-at-bananagrams/
#Monte-Carlo simulation

import random

Nsim = 10000 #number of simulations

n = 144 #number of cards to collect

E = [0]*Nsim

for N in range(Nsim):

    collected = [False]*n
    cash = 0
    
    while (not all(collected)):
        #collect a random card
        c = random.randint(0, n - 1)
        cash += 5
        collected[c] = True

    E[N] = cash

#print average cash spent
print(sum(E)/Nsim)
