# The Riddler Classic 2021-01-15: Ski the Slopes

import random

Nsim = 5000000 #number of simulation replications
count1 = 0
count2 = 0

for N in range(Nsim):

    #generate times
    X1 = random.gauss(0, 1)
    X2 = random.gauss(0, 1)
    #opponent's times
    Y1 = random.gauss(0, 1)
    Y2 = random.gauss(0, 1)

    if (X1 > Y1):
        count1 += 1
        if (X1 + X2 > Y1 + Y2):
            count2 += 1

print(count2/count1)
