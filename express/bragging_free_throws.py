#The Riddler Express: 2017-09-01 Bragging Free Throws
#Monte-carlo solution

import random

#Number of simulations
N = 400000
#Required streak length. A lot slower and more inaccurate for higher n.
#n = 10 with N = 100000 is still possible
#n = 4 with N = 400000 is quite fast
n = 4
#Probability of getting a free throw
p = 0.7

count = 0 #Count total throws


for i in range(0, N):
    streak = 0
    while streak < n:
        count += 1
        if random.random() < p:
            streak += 1 #Increment streak counter
        else:
            streak = 0 #Reset streak

#Print average number of throws to achieve streak
print(count/N)
