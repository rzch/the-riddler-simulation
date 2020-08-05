# The Riddler Classic 2019-05-10: Hitting Streak
# Monte-Carlo simulation
# https://fivethirtyeight.com/features/can-the-riddler-bros-beat-joe-dimaggios-hitting-streak/

import random

Nsim = 10000 #number of simulations

b = 0.4 #batting average

n = 20 #number of seasons
g = 160 #games per seasons
h = 4 #hits per game

t = 56 #target hitting streak to beat

count = 0
for N in range(Nsim):

    s = 0 #initialise streak

    for i in range(n*g):

        if (n*g - i < t - s + 1): #if cannot beat streak
            break

        #simulate hits in a game
        if (any([random.random() < b for j in range(h)])):
            s += 1
        else:
            s = 0

        if s > t: #if beaten streak
            count += 1
            break

print(count/Nsim)
