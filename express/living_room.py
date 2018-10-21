#The Riddler Express 2017-03-24: Living Room Puzzle
#Monte Carlo simulation

import random

Tsim = 10000000 #Number of time steps to simulate
count = 0
state = 0

for t in range(0, Tsim):
    #simulate a time step
    r = random.random()
    if (r < 0.25):
        state += 1
    elif (r < 0.75):
        state = max(0, state - 1)

    #check if clutching the couch
    if (state == 0):
        count += 1

print('Proportion of time clutching the couch:')
print(count/Tsim)
