#The Riddler 2016-12-30 Lonely Solitaire Monte-Carlo simulation
import random

N = 100000 #Number of simulations
count = 0 #Count number of wins

#Generate a deck
deck = [x % 13 + 1 for x in range(0, 52)]

for i in range(0, N):
    #Copy the deck and shuffle it
    shuffled_deck = deck.copy()
    random.shuffle(shuffled_deck)

    #Play the game and increment counter if won
    win = 1
    for j in range(0, 52):
        if deck[j] == shuffled_deck[j]:
            win = 0
            break

    count += win

#Print average
print(count/N)
