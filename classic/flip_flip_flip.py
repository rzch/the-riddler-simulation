#The Riddler Classic 2018-08-03: Flip Flip Flip
#Monte-Carlo simulation

Nsim = 100000 #Number of simulations
count = 0

import random

for n in range(Nsim):

    heads_needed = 1

    win = False

    #play game but terminate if heads needed reaches 15 (count as fail)
    while (not win and heads_needed < 16):

        if all([random.random() < 0.5 for i in range(heads_needed)]):
            count += 1
            win = True
        else:
            heads_needed += 1

#compute empirical probability
print(count/Nsim)
