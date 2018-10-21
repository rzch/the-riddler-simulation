#The Riddler Express 2017-05-19: Careening Carpooling
#Monte Carlo Simulation

import random

Nsim = 100000 #Number of trips

trips = 0 #Count total number of trips

#Chance of each driver getting a ticket
ticket_chance = [0.1, 0.15, 0.2, 0.25]

for N in range(Nsim):

    tickets = 4*[0]

    #while there is still an eligible driver
    while (any([i < 3 for i in tickets])):
        #determine eligible driver
        eligible_drivers = [i for i, t in enumerate(tickets) if t < 3]

        #randomly select driver
        driver = random.sample(eligible_drivers, 1)

        #simulate a ticket
        if (random.random() <= ticket_chance[driver[0]]):
            tickets[driver[0]] += 1
            
        trips += 1
        

print(trips/Nsim)
