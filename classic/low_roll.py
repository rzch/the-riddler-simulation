#The Riddler Classic 2019-11-15: Low Roll
#Monte-Carlo simulation
#Puzzle: https://fivethirtyeight.com/features/how-low-can-you-roll/

import random

Nsim = 5000000 #number of simulations

d = 10 #number of sides on dice

scores = [0]*Nsim

for N in range(Nsim):

    score = 0

    #generate first roll and add to score
    lowroll = random.randint(0, d - 1)
    score += lowroll/d
    
    n = 1
    
    while (lowroll > 0):

        newroll = random.randint(0, d - 1)
        if (newroll <= lowroll): #check if a new roll is lower than previous old roll

            #update score and new low roll
            score += newroll/d**(n + 1)
            lowroll = newroll
            #increment decimal place
            n += 1

    scores[N] = score

#print empirical probability
print('Empirical probability:')
print(sum(scores)/Nsim)

