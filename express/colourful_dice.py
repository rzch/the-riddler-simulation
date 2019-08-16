#The Riddler Express 2018-09-14: Colourful Dice
#Monte-Carlo simulation

import random

Nsim = 100000 #number of simulations
count = 0

#Colours on dice: True = Red, False = Blue
dice1 = [True, False, False, False, False, False]
dice2 = [True, True, True, False, False, False]

for n in range(Nsim):

    #simulate the dice rolls
    roll1 = random.choice(dice1)
    roll2 = random.choice(dice2)

    #count the number of times A wins
    count += (roll1 == roll2)

#compute empirical probability
print(count/Nsim)
