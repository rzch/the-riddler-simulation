#The Riddler Express 2018-12-07: Precipitation Permutations
#Monte-Carlo simulation and calculation of analytical probability

import random

#--------------Analytical Probability

def matmult55x51(A, x):
    #Method to multiply 5x5 matrix with 5x1 vector
    b = [0]*5

    for i in range(5):
        for j in range(5):
            b[i] += x[j]*A[i][j]

    return b

T = [[0.5, 0.2, 0.0, 0.0, 0.0], \
     [0.3, 0.5, 0.2, 0.0, 0.0], \
     [0.0, 0.3, 0.5, 0.2, 0.0], \
     [0.0, 0.0, 0.3, 0.3, 0.0], \
     [0.2, 0.0, 0.0, 0.5, 1.0]] #Left stochastic matrix

x = [0, 1, 0, 0, 0] #Initial state distribution

#Obtain probability distribution after 5 days
for n in range(5):
    x = matmult55x51(T, x)

#probability of not getting wet
print(1 - x[4])

#---------------Monte-Carlo

Nsim = 1000000 #Number of simulations
count = 0

for N in range(Nsim):
    #number of umbrellas at each location
    home = 2
    work = 1
    got_wet = False

    #simulate work week
    for n in range(5):
        
        if (random.random() < 0.5): #rain in morning
            if (home > 0):
                home -= 1
                work += 1
            else:
                got_wet = True
                break
            
        if (random.random() < 0.4): #rain in evening
            if (work > 0):
                work -= 1
                home += 1
            else:
                got_wet = True
                break

    if (got_wet == False):
        count += 1

#Empirical probability
print(count/Nsim)
