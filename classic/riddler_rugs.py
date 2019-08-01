#The Riddler Classic 2018-08-03: Riddler Rugs
#Monte-Carlo simulation

import random
import time

#Note 2.5 million simulations can take in the ballpark of 20 hours on a modern desktop
Nsim = 2500000 #Number of simulations

count = 0

n_colours = 3 #Number of different colours
rug_size = 100 #Rug size (side length)
kernel_size = 4 #Size of tile that should not be all the same

def allsame(slice):
    #This function takes as input a tile and returns True if they are all the same colour
    prev_number = -1
    for i in range(len(slice)):
        for j in range(len(slice[0])):
            if (not prev_number == -1):
                if (not prev_number == slice[i][j]):
                    return False

            prev_number = slice[i][j]

    return True


start = time.time()
for n in range(Nsim):

    #generate random rug
    rug = [[random.randint(1 , n_colours) for j in range(rug_size)] for i in range(rug_size)]

    look_random = True

    #go through every tile and check if they are all the same
    for i in range(rug_size - kernel_size + 1):
        for j in range(rug_size - kernel_size + 1):
            slice = [rug[k][j:(j + kernel_size)] for k in range(i, i + kernel_size)]

            if (allsame(slice)):
                look_random = False
                print(slice)
                print(rug)
                
            if (not look_random):
                break

        if (not look_random):
            break

    if (not look_random):
        count += 1

end = time.time()

#Compute and print statistics, including 95% confidence bounds
p = count/Nsim
se = (p*(1 - p)/Nsim)**0.5
p_ub = p + 1.96*se
p_lb = p - 1.96*se
print('Estimated probability:')
print("{:.6f}".format(p))
print('Upper 95% confidence bound:')
print("{:.6f}".format(p_ub))
print('Lower 95% confidence bound:')
print("{:.6f}".format(p_lb))
print('Simulation time (seconds):')
print("{:.0f}".format(end - start))

            
