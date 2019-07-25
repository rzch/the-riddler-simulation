#The Riddler Express 2018-07-13: Sudden Death Penalty Kick
#Monte-Carlo simulation

import random

Nsim = 100000 #Number of simulations
count = 0

p = 0.75 #Probability of scoring a goal

for n in range(Nsim):

    score1 = 0
    score2 = 0

    #Simulate 5 penalty kicks for each side
    for i in range(5):
        if (random.random() <= p):
            score1 += 1

        if (random.random() <= p):
            score2 += 1

    #Determine if the scores are tied
    if (score1 == score2):
        count += 1

#Compute empirical probability
print(count/Nsim)
