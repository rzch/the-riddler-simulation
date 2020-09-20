# The Riddler Classic 2020-09-11: Reach the Summit
# https://fivethirtyeight.com/features/can-you-reach-the-summit-first/
# Monte-Carlo simulation

import random

Nsim = 10000000 #number of simulations
n = 4 #number of riders

points = 0
for N in range(Nsim):

    #generate random times
    times = [random.random() for i in range(n)]

    #boost time for team
    times[-1] = min(times[-1], times[-2])
    times[-2] = times[-1]

    #determine position
    place = sum([t <= times[0] for t in times])

    #award points
    if (place == 1):
        points += 5
    elif (place == 2):
        points += 3
    elif (place == 3):
        points += 2
    elif (place == 4):
        points += 1

print('Empirical expectation:')
print(points/Nsim)
print('Theoretical expectation:')
print(29/12)
