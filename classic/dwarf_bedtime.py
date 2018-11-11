#The Riddler Classic 2018-01-05: Dwarf Bedtime
#Monte-Carlo simulation

import random

Nsim = 1000000 #number of simulations
count = 0
displaced = 0

n = 7 #number of dwarves

for N in range(Nsim):

    beds = list(range(n))
    dwarves = [-1]*n

    #first dwarf
    bed = random.sample(beds[1:n], 1)[0]
    dwarves[0] = bed
    beds.remove(bed)

    #subsequent dwarves
    for i in range(1, n):
        #check if own bed free
        if (i in beds):
            bed = i
        else:
            bed = random.sample(beds, 1)[0]
        
        dwarves[i] = bed
        beds.remove(bed)

    #if oldest dwarf gets its own bed
    if (dwarves[n - 1] == n - 1):
        count += 1

    #count displaced dwarves
    displaced += sum([dwarves[i] != i for i in range(n)])

print(count/Nsim)
print(displaced/Nsim)
