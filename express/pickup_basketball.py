# The Riddler Express 2020-09-11: Pickup Basketball
# https://fivethirtyeight.com/features/can-you-reach-the-summit-first/
# Monte-Carlo simulation

import random

Nsim = 1000000 #number of simulation
n = 5 #maximum number of players that can show up
count = 0

for N in range(Nsim):

    x = random.randint(1, n)
    y = random.randint(1, n)
    z = random.randint(1, n)

    if (x == y + z or y == x + z or z == x + y):
        count += 1

print('Empirical probability:')
print(count/Nsim)
print('Theoretical probability:')
print(1.5*n*(n-1)/n**3)
