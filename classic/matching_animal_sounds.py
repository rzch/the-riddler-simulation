#The Riddler Classic 2018-06-15: Matching Animal Sounds
#Monte-Carlo solution

import random

n_cards = 10 #number of pair of cards

Nsim = 10000 #number of simulations

times = [0]*Nsim

for n in range(Nsim):

    #initialise cards
    cards = list(range(n_cards)) + list(range(n_cards))

    time = 0

    #play the game
    while (len(cards) > 0):
        #randomly sample a pair
        pick = random.sample(cards, 2)

        #determine if match or not
        if (pick[0] == pick[1]):
            cards.remove(pick[0])
            cards.remove(pick[1])

        #count the time
        time += 2

    #store the total time
    times[n] = time

#compute the average time
print(sum(times)/Nsim)
