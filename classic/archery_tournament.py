# The Riddler Classic 2021-01-08: Archery Tournament
# https://fivethirtyeight.com/features/can-you-cut-the-square-into-more-squares/
# Monte-Carlo simulation

import random
import math

Nsim = 5000000 #number of simulation replications

shots = [0]*Nsim

def random_shot():
	#returns the coordinates of a random shot
    while(True):
        x = random.random()
        y = random.random()

        if (x**2 + y**2 <= 1):
            return x, y

for N in range(Nsim):

    r = 1 #inital radius
    score = 0
    
    alive = True

    while(alive):

        score += 1

		#compute radius of a random shot
        x, y = random_shot()
        r2 = (x**2 + y**2)**0.5

		#check if closer to centre than previous target
        if (r2 > r):
            alive = False
        else:
            r = r2

    shots[N] = score

print("Monte-Carlo probability:")
print(sum(shots)/Nsim)
print("Analytical probability:")
print(math.exp(1))
