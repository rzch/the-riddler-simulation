# The Riddler Classic 2020-08-28: War Showdown
# https://fivethirtyeight.com/features/can-you-cover-the-globe/
# Monte-Carlo simulation

import random

deck = [i//4 for i in range(52)]

#number of simulations
Nsim = 159620171 #expected number until the first; approx. 0.63 chance of happening before

count = 0

for N in range(Nsim):
    random.shuffle(deck)

    #deal hands
    hand1 = deck[0:26]
    hand2 = deck[26:52]

    tally = 0
    for i in range(26):
        if (hand1[i] > hand2[i]):
            tally += 1
        elif (hand1[i] < hand2[i]):
            tally -= 1

        if (tally != i + 1 or tally != i - 1):
            break

    #check if lasted 26 turns
    if (tally == 26 or tally == -26):
        count += 1
        
print(count)
