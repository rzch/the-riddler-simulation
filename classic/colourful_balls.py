#The Riddler Classic 2017-04-28: Colourful Balls
#Monte Carlo simulation

import random

Nsim = 100000 #number of simulations

num_picks = Nsim*[0] #store results

for N in range(Nsim):
    
    balls = list(range(4)) #keep track of ball colours
    indices = list(range(4)) #index the balls

    #converting into a set makes the set unique
    unique_colours = set(balls)

    while(len(unique_colours) > 1):
        pick = random.sample(indices, 2)

        #change the colour
        balls[pick[0]] = balls[pick[1]]
        
        unique_colours = set(balls)
        num_picks[N] += 1

#print empirical average
print(sum(num_picks)/Nsim)
