#The Riddler Classic 2018-02-16: Fast Dodgeball Duel
#Monte-Carlo simulation of optimal strategies

import random

Nsim = 1000000 #number of simulations
counts = [0]*3

#accuracies
a = 1
b = 0.8
c = 0.5

for N in range(Nsim):

    #1 if alive, 0 if eliminated
    players = [1]*3

    while(sum(players) > 1):
        #generate throw successes
        throw = [random.random() < a, \
                 random.random() < b, \
                 random.random() < c]
        
        if (sum(players) == 3):

            #resolve a and b
            if (throw[0] and throw[1]): #a or b randomly lose
                players[random.randint(0, 1)] = 0
            elif (throw[0]): #b lose
                players[1] = 0
            elif (throw[1]): #a lose
                players[0] = 0

            #resolve c
            if (throw[2]): #a lose
                players[0] = 0
                
        elif (sum(players) == 2):
            
            #indices of alive players
            indices = [i for i, x in enumerate(players) if x == 1]
            i1 = indices[0]
            i2 = indices[1]
            
            if (throw[i1] and throw[i2]): #1 or 2 randomly lose
                players[random.sample(indices, 1)[0]] = 0
            elif (throw[i1]): #2 lose
                players[i2] = 0
            elif (throw[i2]): #1 lose
                players[i1] = 0
                
    #increment winner tally
    counts[players.index(1)] += 1

print('Winning probabilities of [a, b, c]')
print([count/Nsim for count in counts])
