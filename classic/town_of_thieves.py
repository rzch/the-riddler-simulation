#Monte carlo simulation for The Riddler Town of thieves
import random
from operator import add

n = 100 #Number of houses (note: 1000 is quite slow)
w = 100 #Initial starting wealth

N = 20000 #Number of simulations

totals = [0]*n #Store the total wealth in each position

for x in range(0, N):
    town = [w]*n #Initialise town wealth

    #Go through each house
    for i in range(0, n):
        #Generate a list of all houses excluding the house doing the robbery and sample 1 randomly
        houses = list(range(0, n))
        houses.remove(i)
        j = random.sample(houses, 1)
        j = j[0] #Convert list of length 1 into a numeric

        #Steal from the randomly selected house
        town[i] = town[i] + town[j]
        town[j] = 0

    #Update totals at the end
    totals = map(add, totals, town)

#Calculate and print the average wealth in each position    
print([x/N for x in totals])
