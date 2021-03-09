# The Riddler Classic 2020-04-10: Spam Comments
# https://fivethirtyeight.com/features/can-you-catch-the-free-t-shirt/
# Monte-Carlo simulation

import random
import math

def exprnd(rate=1):
    #generate an exponentially distributed waiting time with given rate
    return -math.log(random.random())/rate

Nsim = 1000000 #number of simulations
Xs = [0]*Nsim

T = 3 #number of days

for N in range(Nsim):
    t = 0
    X = 0 #initial number of spam comments

    while (True):
        #generate a waiting time with rate equal to total number of comments
        t += exprnd(X + 1)
        if (t <= T):
            X += 1 #add a spam comment
        else:
            break
            
    Xs[N] = X

print('Empirical average:')
print(sum(Xs)/Nsim)
print('Theoretical expectation:')
print(math.exp(T) - 1)
