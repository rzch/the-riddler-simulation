# The Riddler Classic 2019-03-29: Ordinal Spelling Bee
# https://fivethirtyeight.com/features/can-you-win-a-spelling-bee-if-you-know-99-percent-of-the-words/
# Monte-Carlo simulation

import random

Nsim = 100000 #number of simulations
n = 10 #number of contestants

#probabilities of correctly answering in decreasing order
probs = [1 - 0.01*(i + 1) for i in range(n)]

count = 0
for N in range(Nsim):

    alive = [True for i in range(n)];

    turn = 0
    while(sum(alive) > 1):

        #spell a word and determine if correct
        if (alive[turn]):
            alive[turn] = random.random() < probs[turn]

        #next contestant
        turn = (turn + 1)%n

    #check if won
    if (alive[0]):
        count += 1

#empirical probability of winning
print(count/Nsim)

#probabilities of correctly answering in increasing order
probs = [1 - n*0.01 + i*0.01 for i in range(n)]

count = 0
for N in range(Nsim):

    alive = [True for i in range(n)];

    turn = 0
    while(sum(alive) > 1):

        #spell a word and determine if correct
        if (alive[turn]):
            alive[turn] = random.random() < probs[turn]

        #next contestant
        turn = (turn + 1)%n

    #check if won
    if (alive[-1]):
        count += 1

#empirical probability of winning
print(count/Nsim)
