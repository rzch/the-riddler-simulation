#The Riddler Classic 2017-05-05: The Lucky Derby
#Monte Carlo simulation

import random

Nsim = 10000 #Number of simulations

n = 20 #Number of horses

counts = n*[0] #Store number of times won

for N in range(Nsim):

    x = n*[0] #Keep track of position

    while(max(x) < 200):

        #Update positions
        for i in range(n):
            r = random.random()

            if (r <= 0.52 + i*0.02):
                x[i] += 1
            else:
                x[i] += -1

    #Find all horses that have crossed the line (to account for ties)
    indices = [i for i, y in enumerate(x) if y == 200]

    #Only count a win if outright
    if (len(indices) == 1):
        counts[indices[0]] += 1

#Print empirical probabilities
print([i/Nsim for i in counts])
