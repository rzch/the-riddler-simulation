# The Riddler Express 2019-03-22: Ticket to Ride
# https://fivethirtyeight.com/features/can-you-win-a-spelling-bee-if-you-know-99-percent-of-the-words/
# Monte-Carlo simulation

import random

Nsim = 1000000 #number of simulations

n = 30 #number of tickets
m = 6 #number picked up in first game

s = 3 #number selected the second time 

count = 0
for N in range(Nsim):

    #first game
    selection = random.sample(list(range(n)), m)

    #second game
    selection2 = random.sample(list(range(n)), s)

    #check whether at least one has been seen before
    count += any([any([selection[i] == selection2[j] for j in range(s)]) for i in range(m)])


print('Empirical probability at least one ticket seen before:')
print(count/Nsim)
print('Empirical probability all tickets new:')
print(1 - count/Nsim)
