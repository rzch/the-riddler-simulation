# The Riddler Classic 2021-02-19: Riddler Jenga
# https://fivethirtyeight.com/features/can-you-win-riddler-jenga/
# Monte-Carlo simulation

import random

def isUnstable(tower):
    #check whether a tower or subtower is unstable
    
    if (len(tower) < 2):
        return False

    base = tower[0]
    top = tower[1:-1]
    top.append(tower[-1])

    #check whether the top is balanced on the base
    com = sum(top)/len(top) #centre of mass
    if (com < base - 0.5):
        return True
    elif (com > base + 0.5):
        return True
    else:
        return False

Nsim = 1000000 #number of simulation replications
counts = [0]*Nsim

for N in range(Nsim):

    #initial block
    tower = [random.random() - 0.5]
    c = 1

    unstable = False

    while(not unstable):

        #add a block centered at the previous block
        tower.append(tower[-1] + random.random() - 0.5)
        c += 1

        #check if tower or any subtower above each block is unstable
        for i in range(0, len(tower)):

            subtower = tower[i:-1]
            subtower.append(tower[-1])
            
            unstable = isUnstable(subtower)

            if (unstable):
                break

    counts[N] = c

print(sum(counts)/Nsim)
