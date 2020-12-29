# The Riddler Express 2019-08-23: Counterfeit Bills
# fivethirtyeight.com/features/a-peaceful-but-not-peaceful-transition-of-power-in-riddler-nation/
# Monte-Carlo simulation and computation of solution

import random
import math

n = 55 #number of fake bills

m = math.floor((25 + n)/20) #number inspected by bank

#---------------------------------------------------------
# Computation of analytical expectation

def binomial(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke.
    See http://stackoverflow.com/questions/3025162/statistics-combinations-in-python
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0
    
def pr_s(s, n, m):

    return 1.0*binomial(n, s)*binomial(25, m-s)/binomial(25+n, m)


prob_accept = 0

for s in range(0, m+1):
    prob_accept += pr_s(s, n, m)*(3/4)**s

E = 100*((n + 25)*prob_accept - 25)
print('Analytical: ' + str(E))

#---------------------------------------------------------
# Monte-Carlo simulation of expectation

Nsim = 1000000 #number of simulations

fakes = [0]*25 + [1]*n
profits = [0]*Nsim

for N in range(Nsim):

    #
    selection = random.sample(fakes, m)

    #detect whether fake bills are fake
    detect = [bill*(random.random() < 0.25) for bill in selection]

    if (any(detect)):
        profits[N] = -2500
    else:
        profits[N] = 100*n

print('Monte-Carlo: ' + str(sum(profits)/Nsim))
