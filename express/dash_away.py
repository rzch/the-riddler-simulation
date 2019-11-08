# The Riddler Express 2018-12-21: Dash Away
# Monte-Carlo simulation

import random

Nsim = 10000 #number of simulations

n = 8 #number of reindeer excluding Rudolph
#proper order
reindeer = list(range(n))

time = 0

for N in range(Nsim):

    minutes = 0

    #create random list
    random_list = list.copy(reindeer)
    random.shuffle(random_list)

    #for each position in sleigh
    for i in range(n):

        j = 0
        #harness first reindeer in list
        minutes += 1
        while(random_list[j] != i): #check if reindeer grunts
            j += 1
            #harness next reindeer in list
            minutes += 1

        #scratch reindeer of list once found
        random_list.remove(i)

    #tally total time
    time += minutes

#print average time
print(time/Nsim)
