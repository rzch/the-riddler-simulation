#The Riddler Classic 2017-06-09: Cash Game Show
#Monte Carlo simulation with optimal strategy

import random

Nsim = 1000000

envelopes = list(range(4))

count = [0]*4

for x in range(Nsim):

    random.shuffle(envelopes)

    #optimal strategy
    if (envelopes[1] > envelopes[0]):
        count[envelopes[1]] += 1
    elif (envelopes[2] > envelopes[1]):
        count[envelopes[2]] += 1
    else:
        count[envelopes[3]] += 1

print('Empirical probabilities:')
print([c/Nsim for c in count])
print('Theoretical probabilities:')
print([1/24, 5/24, 1/3, 5/12])
