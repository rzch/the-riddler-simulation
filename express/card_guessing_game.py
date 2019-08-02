#The Riddler Express 2018-08-17: Card Guessing Game
#Monte-Carlo simulation of optimal strategy

import random

Nsim = 1000000 #Number of simulations
count = 0

#generate cards
low_card = 2
high_card = 10
cards = list(range(low_card, high_card + 1))

for n in range(Nsim):
    random.shuffle(cards)

    #draw the first card and determine the remaining cards
    seen_cards = cards[0:1]
    remaining_cards = list.copy(cards)
    remaining_cards.remove(seen_cards[0])

    #draw the remaining cards
    for i in range(len(cards) - 1):

        #compare with the most recently seen card
        s = seen_cards[-1]

        #calculate how many remaining cards are lower/higher than this
        nless = sum([c < s for c in remaining_cards])
        nmore = len(remaining_cards) - nless

        #determine optimal decision
        if (nmore >= nless):
            guess_bigger = True
        else:
            guess_bigger = False

        #draw the next card
        d = cards[i + 1]
        #determine if keep going
        if (guess_bigger and d > s) or (not guess_bigger and d < s):
            #update seen and remaining cards
            seen_cards.append(d)
            remaining_cards.remove(d)
        else:
            break

    #check if got to the end
    if (len(seen_cards) == len(cards)):
        count += 1

#print empirical probability and compare with theoretical
print('Monte-Carlo probability:')
print(count/Nsim)
print('Theoretical probability:')
print(62000/362880)
