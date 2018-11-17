#The Riddler Express 2018-02-16: Dodgeball Duel
#Monte-Carlo simulation of optimal strategies

import random

Nsim = 1000000 #number of simulations
counts = [0]*3 #count wins for each player

for N in range(Nsim):

    #[fast, fast, slow]
    players = [True]*3

    #round 1
    players[random.randint(0, 1)] = False #fast attack each other
    players[random.randint(0, 1)] = False #slow attack a random fast

    #if a fast player is alive they win, otherwise slow wins
    counts[players.index(True)] += 1

print('Win probabilities of [fast, fast, slow]')
print([i/Nsim for i in counts])
