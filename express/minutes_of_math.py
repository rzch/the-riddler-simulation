#The Riddler Express 2019-02-08: Minutes of Math
#Monte-Carlo simulation

import random

Nsim = 10000000 #number of simulations

count = 0 #count number of occurences

intmax = 99999 #maximum integer to sample

for N in range(Nsim):

    a = random.randint(0, intmax)
    b = random.randint(0, intmax)
    c = random.randint(0, intmax)

    if ((a*b*c)%100 == 0):
        count += 1

        #print([a, b, c, a*b*c])

print(1.0*count/Nsim)
