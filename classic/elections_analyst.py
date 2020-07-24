# The Riddler Classic 2018-11-02: Elections Analyst
# https://fivethirtyeight.com/features/how-far-would-you-go-to-rig-a-coin-flip/
# Monte-Carlo simulation

import math
from random import getrandbits
from random import random

Nsim = 100000

n = 100 #number of seats

n1 = math.ceil((n + 1)/2) #threshold for winning
n2 = 0.6*n #threshold for supermajority

#----Q1---------------------------------------

count1 = 0
count2 = 0
for N in range(Nsim):

    #simulate coin flips
    seats = [not getrandbits(1) for i in range(n)]

    if (sum(seats) >= n1):
        count1 += 1

    if (sum(seats) >= n2):
        count2 += 1
        
print('Q1-------------')
print('Empirical probability of winning:')
print(count1/Nsim)
print('Empirical probability of supermajority:')
print(count2/Nsim)

#----Q2---------------------------------------

count = 0
t = 0.5947 #coin weighting
for N in range(Nsim):

    #simulate coin flips
    seats = [random() < t for i in range(n)]

    if (sum(seats) >= n2):
        count += 1

print('Q2-------------')
print('Empirical probability of supermajority:')
print(count/Nsim)
        
