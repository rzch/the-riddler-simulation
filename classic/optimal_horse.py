# The Riddler Classic 2019-07-12: Optimal HORSE
# https://fivethirtyeight.com/features/whats-the-optimal-way-to-play-horse/
# Monte-Carlo simulation of optimal strategy

import random

Nsim = 1000000 #number of simulations
count = 0

eps = 0.15 #chance to miss

def shot_in():
    #returns the result of a shot

    return random.random() < 1 - eps

for N in range(Nsim):

    serverA = True #whether A is serving

    horseA = 0
    horseB = 0

    while (horseA < 5 and horseB < 5):

        if (shot_in()): #server shot

            if (not shot_in()): 
                #person who misses gets a letter
                if (serverA): 
                    horseB += 1
                else:
                    horseA += 1
        else:
            #switch server
            serverA = not serverA 

    if (horseA < 5):
        count += 1

print('Empirical probability')
print(count/Nsim)
print('Theoretical probability')
print((eps - 2)*(eps**8 - 20*eps**7 + 194*eps**6 - 1130*eps**5 +4421*eps**4
                 - 10245*eps**3 + 15704*eps**2 - 13870*eps + 5401)/(eps - 3)**9)
