#The Riddler Express 2018-11-09: Telephonic Coincidence
#Monte-Carlo simulation

import random

Nsim = 10000000 #number of simulations
count = 0

n = 7 #number of digits

for N in range(Nsim):

    #generate random cell number
    cell = random.randint(0, 10**n - 1)
    #convert to string and pad with zeros
    cell_str = ('%0' + str(n) + 'd') % cell

    #generate random landline number
    land = random.randint(0, 10**n - 1)
    #convert to string and pad with zeros
    land_str = ('%0' + str(n) + 'd') % land

    #for each digit check if phone numbers contain the same amount
    is_scramble = True
    for i in range(0, 10):
        d1 = sum([char == str(i) for char in cell_str])
        d2 = sum([char == str(i) for char in land_str])
        if (d1 != d2):
            is_scramble = False
            break

    count += is_scramble

#print empirical probability
print(count/Nsim)
