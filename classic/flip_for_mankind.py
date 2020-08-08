# The Riddler Classic 2019-05-24: Flip for Mankind
# https://fivethirtyeight.com/features/one-small-step-for-man-one-giant-coin-flip-for-mankind/
# Monte-Carlo simulation

from random import random

Nsim = 5000000 #number of simulations

p = 0.24213 #probability of coin landing on heads

#divisions of probability space (True indicates heads)
d1 = [[True, True, True, True], [False, False, False, False]]
d2 = [[True, True, True, False], [True, True, False, True],
      [True, True, False, False], [True, False, True, False], [True, False, False, True],
      [False, False, True, False], [False, False, False, True]]

count1 = 0
count2 = 0
count3 = 0
for N in range(Nsim):

    #perform 4 flips
    flip = [random() < p for i in range(4)]

    #check if matches 1
    if any([all([d[j] == flip[j] for j in range(4)]) for d in d1]):
        count1 += 1
    #check if matches 2
    elif any([all([d[j] == flip[j] for j in range(4)]) for d in d2]):
        count2 += 1
    #else matches 3
    else:
        count3 += 1

print(count1/Nsim)
print(count2/Nsim)
print(count3/Nsim)
