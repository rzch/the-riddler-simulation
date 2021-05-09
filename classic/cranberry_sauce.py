# The Riddler Classic 2020-11-20: Cranberry Sauch
# https://fivethirtyeight.com/features/can-you-pass-the-cranberry-sauce/
# Monte-Carlo simulation

import random

Nsim = 1000000 #number of simulation replications

n = 20 #number of people in the circle
counts = [0]*n

for N in range(Nsim):

    received = [False]*n
    x = 0
    received[0] = True

    while (not all(received)):
        #randomly pass left or right
        if (bool(random.getrandbits(1))):
            x = (x + 1)%n
        else:
            x = (x - 1)%n

        received[x] = True

    counts[x] += 1

print([c/Nsim for c in counts])
