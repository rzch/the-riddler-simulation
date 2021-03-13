# The Riddler Classic 2020-08-14: Riddler Manufacturing Company
# https://fivethirtyeight.com/features/are-you-hip-enough-to-be-square/
# Monte-Carlo simulation and comparison to analytical solution

import random

def split_ruler():
    #returns the locations of the three splits, in order

    r = [random.random() for i in range(3)]

    x1 = min(r)
    x3 = max(r)
    r.remove(x1)
    r.remove(x3)
    x2 = r[0]

    return x1, x2, x3


Nsim = 1000000 #number of replications
lengths = [0]*Nsim
l1s = [0]*Nsim

for N in range(Nsim):
    
    x1, x2, x3 = split_ruler()

    #determine piece lengths
    l1 = x1
    l2 = x2 - x1
    l3 = x3 - x2
    l4 = 1 - x3

    #find the length of the piece containing the half mark
    if (x1 > 0.5):
        lengths[N] = l1
    elif (x1 <= 0.5 and x2 > 0.5):
        lengths[N] = l2
    elif (x2 <= 0.5 and x3 > 0.5):
        lengths[N] = l3
    else:
        lengths[N] = l4

    l1s[N] = l1

print('Empirical probability:')
print(sum(lengths)/Nsim)
print('Analytical probability:')
print(15/32)
