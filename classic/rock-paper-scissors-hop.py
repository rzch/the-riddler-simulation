#The Riddler 2018-08-24: Rock-Paper-Scissors-Hop
#Monte-Carlo simulation

import random

Nsim = 500000 #number of simulations
times = [0]*Nsim 

nhoops = 10 #number of hoops

for n in range(Nsim):

    time = -1
    #starting positions
    blue = -1
    red = nhoops

    game_active = True

    while (game_active):
        if (abs(blue - red) <= 1):
            #count time until someone wins the rock-paper-scissors
            while (random.random() < 1/3):                
                time += 1

            #determine outcome from rock-paper-scissors
            time += 1
            if (random.random() <= 0.5):
                red = nhoops
            else:
                blue = -1

        #each team hops forward and it takes 1 second
        blue += 1
        red -= 1
        time += 1

        #check if a team has won
        if (blue == nhoops or red == -1):
            game_active = False


    times[n] = time

#Compare empirical with theoretical average
print('Empirical average:')
print(sum(times)/Nsim)
print('Theoretical average:')
print((nhoops**2 + 7*nhoops - 3)/2)
        
