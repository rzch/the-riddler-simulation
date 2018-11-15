#The Riddler Express 2018-02-02: Daily Dose
#Monte-Carlo simulation

import random

Nsim = 10000 #number of simulations
total = 0 #total number of preferred vitamins taken

n = 60 #starting number of vitamins, must be divisible by 4

for N in range(Nsim):

    #bottle of vitamins, containing either 0 or 1
    bottle = [int(i//(n/2))for i in range(n)]

    #mix bottle
    random.shuffle(bottle)

    #loop through the days
    for i in range(int(n/4)):
        #draw vitamins
        vitamins = bottle[0:4]
        bottle[0:4] = []

        #tally preferred vitamins taken that day
        total += min(2, sum(vitamins))

print('Proportion of preferred vitamins taken:')
print(total/(Nsim*n/2))
