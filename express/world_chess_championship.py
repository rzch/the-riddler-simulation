#The Riddler Express 2018-11-16: World Chess Championship
#Monte-Carlo simulation

import random

Nsim = 100000 #number of simulations
count = 0

#cumulative distribution for win, loss, draw
cdf = [0.2, 0.35, 1]

#number of games
n = 12 #default
n = 82 #for 75 win chance
n = 248 #for 90 win chance
n = 771 #for 99 win chance

for N in range(Nsim):

    score1 = 0
    score2 = 0
    
    for i in range(n):
        r = random.random()

        if (r < cdf[0]): #better player win game
            score1 += 1
        elif (r < cdf[1]): #better player lose game
            score2 += 1
        elif (r < cdf[2]): #draw game
            score1 += 0.5
            score2 += 0.5

        if (score1 >= n/2 + 0.5): #better player wins match
            count += 1
            break

print('Better player win probability:')
print(count/Nsim)
