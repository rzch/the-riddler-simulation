# The Riddler Classic 2020-09-18: Guess My Word
# https://fivethirtyeight.com/features/can-you-break-a-very-expensive-centrifuge/
# Monte-Carlo simulation and comparison with theoretical expectations

import math
import random

def expected_guesses(n):
    #recursive function for expected number of guesses

    if (n == 0):
        return 0
    elif (n == 1):
        return 1

    n1 = math.floor((n - 1)/2)
    n2 = math.ceil((n - 1)/2)
    
    return 1 + expected_guesses(n1)*n1/n + expected_guesses(n2)*n2/n


Nsim = 1000000 #number of simulations
n = 267751 #number of possible words to guess
t = [0]*Nsim

for N in range(Nsim):

    c = 0 #count number of guesses

    #random index of word to guess
    x = random.randint(1, n)

    lb = 1 #lower bound on index of word
    ub = n #upper bound on index of word
    
    m = n #number of elements between lb and ub (inclusive)

    g = math.ceil(m/2) #initial guess
    c += 1

    while(g != x):

        if (x < g): #before guess
            ub = g - 1
            
        elif (x > g): #after guess
            lb = g + 1

        #number of elements between lb and ub (inclusive)
        m = ub - lb + 1

        #binary search guess
        g = lb + math.ceil(m/2) - 1
        c += 1

    t[N] = c

print('Simulation:')
print(sum(t)/Nsim)
print('Theoretical:')
print(expected_guesses(n))
