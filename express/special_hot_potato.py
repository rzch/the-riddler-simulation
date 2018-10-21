#The Riddler Express 2017-08-04: Special Hot Potato
#Monte Carlo simulation

import random

Nsim = 100000 #Number of simulations

n_children = 30 #Number of children

counts = [0]*(n_children) #Count how many times each child won

for x in range(Nsim):
    held_potato = [0]*(n_children + 1) #Tracker whether a child has held potato
    pos = 0 #Potato starts from teacher
    held_potato[0] = -1 #Teacher is a sentinel

    #While there is more than 1 child who hasn't held potato
    #(note that teacher counts as a -1 in the sum)
    while (sum(held_potato) < n_children - 2):
        #Simulate coin flip and potato going left or right
        #Wrap around circle using modulo arithmetic
        if (random.random() < 0.5):
            pos = (pos - 1)%(n_children + 1)
        else:
            pos = (pos + 1)%(n_children + 1)

        #Update child holding potato excluding teacher
        if (pos != 0):
            held_potato[pos] = 1

    counts[held_potato.index(0) - 1] += 1

#Print empirical probabilities
print([i/Nsim for i in counts])
