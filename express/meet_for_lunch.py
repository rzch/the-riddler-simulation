#The Riddler Express 2017-03-31: Meet for Lunch
#Monte Carlo simulation

import random

Nsim = 4000000 #Number of simulations

count = 0

for x in range(0, Nsim):
    #Generate arrival times
    r1 = 60*random.random();
    r2 = 60*random.random();

    #Compare closeness
    if (abs(r1 - r2) <= 15):
        count += 1

print('Probability of meeting for lunch:')
print(count/Nsim)
