# The Riddler Classic 2020-03-27: Re-Rolling Die
# https://fivethirtyeight.com/features/can-you-get-the-gloves-out-of-the-box/
# Monte-Carlo simulation

import random

Nsim = 100000 #number of simulations
n = 6 #sides on die

rolls = [0]*Nsim
for N in range(Nsim):

    roll = 0
    
    die = list(range(1, n+1))

    #roll until all sides are the same
    while(not all([d == die[0] for d in die])):
        #rewrite faces
        die = [random.choice(die) for i in range(n)]
        roll += 6

    rolls[N] = roll

print(sum(rolls)/Nsim)
