# The Riddler Classic 2019-06-07: Uberpanzer
# https://fivethirtyeight.com/features/youve-been-marooned-by-kidnappers-can-you-escape-at-dawn/
# Monte-Carlo simulation of unbiased estimator and computation of maximum likelihood estimator

import random
import math

#----------
#Monte-Carlo simulation

N = 135 #number of Uberpanzers

Nsim = 10000 #number of simulations
N_ests = [0]*Nsim #store estimates

#tank serial numbers
tanks = [i+1 for i in range(N)]

for i in range(Nsim):

    #random sample size
    n = random.randint(2, N)

    sample = random.sample(tanks, n)

    X = min(sample)
    Y = max(sample)

    N_ests[i] = X + Y - 1

print('Actual number of Uberpanzers: ' + str(N))
print('Average of unbiased estimator: ' + str(sum(N_ests)/Nsim))

#--------
#Maximum likelihood

def likelihood(N):
    #likelihood of min 22 max 114 given total number of uberpanzers N
    #averaged over uniform prior of sample size n
    
    L = 0
    for n in range(2, 94):

        x = 1
        for i in range(3, n + 1):
            x *= (93 - i + 1)/(N - i + 1)

        L += x

    L = L/(92*N*(N - 1))

    return L

def likelihood2(N, n):
    #likelihood of min 22 max 114 given total number of uberpanzers N
    #and sample size n
    
    L = 1
    for i in range(3, n + 1):
        L *= (93 - i + 1)/(N - i + 1)

    L = L/(N*(N - 1))

    return L

def loglikelihood2(N, n):
    #log likelihood of min 22 max 114 given total number of uberpanzers N
    #and sample size n
    
    logL = 0
    for i in range(3, n + 1):
        logL += math.log((93 - i + 1)/(N - i + 1))

    logL += math.log(1/(N*(N - 1)))

    return logL

#demonstrate 114 is the maximum likelihood estimate
print(likelihood(114), likelihood(115), likelihood(116))

print(likelihood2(114, 3), likelihood2(115, 3))

print(loglikelihood2(114, 3), loglikelihood2(115, 3))
print(loglikelihood2(114, 2), loglikelihood2(115, 2))
