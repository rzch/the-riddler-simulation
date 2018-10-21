#The Riddler 2016-12-02 Secret Santas
#Monte Carlo simulation

import random

Nsim = 10000 #number of simulations
count = 0

n = 41 #number of staffers

for x in range(0, Nsim):

    #simulate assignments
    staffers = list(range(0, n))
    assigned = staffers.copy()

    #sample a derangement using simple rejection sampling
    random.shuffle(assigned)
    while (sum([staffers[i] == assigned[i] for i in assigned]) > 0):
        random.shuffle(assigned)

    #count all the cycles in the assignments and find the max length
    maxloop = 0
    currloop = 0

    #flag to see if staffer has been 'visited' during counting
    visited = [False]*n
    #starting point
    start = 0
    visit = start
    visited[visit] = True
    while (sum(visited) <= n):
        visit = assigned[visit]
        currloop += 1

        if (visited[visit] == False):
            #update flag
            visited[visit] = True
        else:
            #cycle finished, update counts
            maxloop = max(currloop, maxloop)
            currloop = 0
            #pick the next loop to count out of those not visited
            if (sum(visited) < n):
                start = visited.index(False)
                visit = start
                visited[visit] = True
            else:
                #terminates the while loop (otherwise infinite)
                break          

    #not everyone will find their secret santa if there are cycles longer than 21
    if (maxloop <= 21):
        count += 1

#compute proportion
print(count/Nsim)
