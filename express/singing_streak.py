#The Riddler Express 2018-10-12: Singing Streak
#Monte-Carlo simulation

import random
import statistics

Nsim = 100000 #number of simulations
streaks = [0]*Nsim

for n in range(Nsim):

    streak = 0
    #sing until the streak is broken
    while (random.random() < 364/365):
        streak += 1

    streaks[n] = streak

#compute the median of the singing streaks
print(statistics.median(streaks))
