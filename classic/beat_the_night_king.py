# The Riddler Classic 2019-05-17: Beat the Night King
# https://fivethirtyeight.com/features/how-many-soldiers-do-you-need-to-beat-the-night-king/
# Monte-Carlo simulation
from random import getrandbits

Nsim = 500000

n0 = 17 #living army size
m0 = 4 #dead army size

count = 0

for N in range(Nsim):

    n = n0
    m = m0
    
    while (n > 0 and m > 0):
        
        if (getrandbits(1)): #dead soldier defeated
            m -= 1
        else: #living soldier defeated
            n -= 1
            m += 1

    #check if living army won
    if (n > 0):
        count += 1

print(count/Nsim)

        
