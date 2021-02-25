# The Riddler Classic 2020-02-21: Coin Flipping Madness
# https://fivethirtyeight.com/features/can-you-flip-your-way-to-victory/
# Monte-Carlo simulation of optimal strategy and computation of analytical solution

import random

def flipA():
    #generates the outcome from flipping coin A
    return 2*random.getrandbits(1) - 1

def flipB():
    #generates the outcome from flipping coin B
    return 4*random.getrandbits(1) - 2

n = 100 #number of flips

Nsim = 100000 #number of simulations
count = 0

for N in range(Nsim):

    score = 0

    #simulate flips
    for i in range(n):
        if (score >= 0):
            score += flipA()
        else:
            score += flipB()

    if (score > 0):
        count += 1

print('Monte-Carlo Probability:')
print(count/Nsim)

VA = [0]*(2*n) + [0] + [1]*(2*n) #probability of winning by flipping coin A
VB = [0]*(2*n) + [0] + [1]*(2*n) #probability of winning by flipping coin B

#dynamic programming backwards recursion
for i in range(n):
    VA0 = VA.copy()
    VB0 = VB.copy()

    #iterate through states
    for j in range(4*n+1):

        #coin A
        if (j == 0):
            VA[j] = 0.5*max(VA0[j+1], VB0[j+1])
        elif (j == 4*n):
            VA[j] = 0.5*1 + 0.5*max(VA0[j-1], VB0[j-1])
        else:
            VA[j] = 0.5*max(VA0[j+1], VB0[j+1]) + 0.5*max(VA0[j-1], VB0[j-1])

        #coin B
        if (j <= 1):
            VB[j] = 0.5*max(VA0[j+2], VB0[j+2])
        elif (j >= 4*n-1):
            VB[j] = 0.5*1 + 0.5*max(VA0[j-2], VB0[j-2])
        else:
            VB[j] = 0.5*max(VA0[j+2], VB0[j+2]) + 0.5*max(VA0[j-2], VB0[j-2])

print('Analytical Probability:')
print(max(VA[2*n], VB[2*n]))
    
