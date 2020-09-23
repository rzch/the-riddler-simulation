# The Riddler Classic 2019-08-02: Circular Train
# https://fivethirtyeight.com/features/how-many-cars-are-on-this-circular-train/
# Monte-Carlo Simulation

import random

Nsim = 1000 #number of simulations
n = 100 #number of carriages
total_steps = 0

def check_carriages(carriages, n, i=0):
    #checks if there are n carriages or if 
    #n is a multiple of the number of carriages
    
    #turn first carriage light on
    carriages[i] = True

    x = (i + n)%len(carriages)
    steps = n #walk forward n carriages
    if (carriages[x] == False):
        #if light is off, it means there cannot be n carriages
        return False, steps, x
    else:
        #turn of carriage light
        carriages[x] = False

    steps += n #walk back n carriages
    if (carriages[i] == False):
        #if first carriage light is off, it means there are n carriages
        return True, steps, i
    else:
        return False, steps, i

for N in range(Nsim):
    #generate random carriage
    carriages = [bool(random.getrandbits(1)) for i in range(n)]

    #check for each n = 1, 2, ...
    determined = False
    ntry = 1
    i = 0
    while (not determined):
        determined, steps, i = check_carriages(carriages, ntry, i)
        total_steps += steps
        ntry += 1

#Takes less on average than naive approach
print('Average number of steps:')
print(total_steps/Nsim)
