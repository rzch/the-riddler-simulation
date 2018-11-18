#The Riddler Express 2018-02-23: Battle for Tokens
#Monte-Carlo simulation

import random

Nsim = 10000 #number of simulations
count = 0

for N in range(Nsim):
    tokens1 = 1
    tokens2 = 2

    while(tokens1 > 0 and tokens2 > 0):
        win = random.random() < 2/3

        if (win):
            tokens1 += 1
            tokens2 -= 1
        else:
            tokens2 += 1
            tokens1 -= 1

    if (tokens2 == 0):
        count += 1

print(count/Nsim)
