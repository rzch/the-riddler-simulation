# The Riddler Classic 2020-11-13: Bad Football
# https://fivethirtyeight.com/features/can-you-snatch-defeat-from-the-jaws-of-victory/
# Monte-Carlo simulation

import random

def binomial(n, r):
    ''' Binomial coefficient, nCr, aka the "choose" function 
        n! / (r! * (n - r)!)
    '''
    #https://stackoverflow.com/questions/26560726/python-binomial-coefficient
    
    p = 1    
    for i in range(1, min(r, n - r) + 1):
        p *= n
        p //= i
        n -= 1
    return p

def binopmf(x, n, p):
    #binomial probability mass function

    return binomial(n, x)*p**x*(1-p)**(n-x)

def binocdf(x, n, p):
    #binomial cumulative distribution function
    
    s = 0
    for i in range(x+1):
        s += binopmf(i, n, p)

    return s

def prwin(x, y):
    #returns the probability of winning given the score is x-y,
    #i.e. the probability of getting the flips needed to reach 51 or more,
    #within the remaining 101-x-y flips

    return 1 - binocdf(51-x-1, 101-x-y, 0.5)

#score thresholds for 99% chance of winning for each number of flips
xthres = [101]*100
xthres[21-1] = 21; #the smallest score with at least 99% chance of winning is 21-0

#compute all the score thresholds (hot-start from previous threshold)
for t in range(22, 100+1):
    for i in range(xthres[t-2], t+1):
        if (prwin(i, t-i) >= 0.99):
            xthres[t-1] = i
            break

Nsim = 1000000 #number of simulation replications
count = 0
for N in range(Nsim):

    #generate a realisation of a binomial process
    binomprocess = [0]*101
    binomprocess[0] = random.getrandbits(1)
    for t in range(0, 100):
        binomprocess[t+1] = binomprocess[t] + random.getrandbits(1)

    #check if the process reached the threshold at any point, and then lost
    if (any([binomprocess[t] >= xthres[t] for t in range(21, 100)]) and binomprocess[-1] < 51):
        count += 1

print(count/Nsim)
