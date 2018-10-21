#The Riddler Express 2017-06-02: Hoops Puzzle
#Monte Carlo simulation

import random

Nsim = 10000000 #Number of simulations

total_games = 0 #Total number of games across all simulations

p1 = 0.5 #Probability of a team winning
p2 = 1 - p1

for N in range(Nsim):

    g1 = 0
    g2 = 0

    #Simulate games while the series is not finished
    while(g1 < 4 and g2 < 4):
        if (random.random() < p1):
            g1 += 1
        else:
            g2 += 1

    total_games += g1 + g2

print(total_games/Nsim)
