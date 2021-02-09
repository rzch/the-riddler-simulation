# The Riddler Classic 2019-10-04: Birthday Puzzle
# https://fivethirtyeight.com/features/who-wants-to-be-a-riddler-millionaire/
# Monte-Carlo simulation of solution and comparison with analytical solution

import random
import math

def binomial(n, r):
    #https://stackoverflow.com/questions/26560726/python-binomial-coefficient
    ''' Binomial coefficient, nCr, aka the "choose" function 
        n! / (r! * (n - r)!)
    '''
    p = 1    
    for i in range(1, min(r, n - r) + 1):
        p *= n
        p //= i
        n -= 1
    return p

def prob_m_pairs(n, m):
    #computes the probability that there are exactly m pairs

    return binomial(365, m)*binomial(365-m, n-2*m)*math.factorial(n)/2**m/365**n
    
def prob_triple(n):
    #computes the probability that there is at least one triple
    
    p = 0
    for m in range(0, n//2 + 1):
        p += binomial(365, m)*binomial(365-m, n-2*m)*math.factorial(n)/2**m/365**n
    
    return 1 - p

n = 88 #number of people

print("Probability for " + str(n) + " people:")
print(prob_triple(n))

Nsim = 100000 #number of simulations
count = 0

days = list(range(365))
for N in range(Nsim):

    #sample days
    sample_bdays = random.choices(days, k=n)

    unique_days = set(sample_bdays)
    multiplicity = 1

    #determine the multiplicity of each date
    for d in unique_days:
        multiplicity = max(multiplicity, sum([i == d for i in sample_bdays]))
        if (multiplicity >= 3):
            count += 1
            break

print("Monte-Carlo probability for " + str(n) + " people:")
print(count/Nsim)

    
