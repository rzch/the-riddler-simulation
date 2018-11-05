#The Riddler Classic 2017-10-06: Beat the Game Show
#Monte-Carlo simulation of optimal strategy

import random

Nsim = 10000 #Number of simulations
count = 0

n = 100 #number of players
g = 50 #number of guesses

for N in range(Nsim):
    #generate boxes randomly
    boxes = list(range(n))
    random.shuffle(boxes)

    found_box = [False]*n

    #simulate each player going into the room
    for i in range(n):
        next_box = i
        #simulate following the optimal strategy
        for j in range(g):
            number_in_box = boxes[next_box]
            if (number_in_box == i):
                found_box[i] = True
                break

            next_box = number_in_box

    if (all(found_box)):
        count += 1

#print empirical probability
print(count/Nsim)
