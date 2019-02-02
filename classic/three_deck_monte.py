#The Riddler Classic 2019-02-01: Three Deck Monte
#Monte-Carlo simulation

import random


def play_game(deck1, deck2):
    #Simulate a single game between deck1 and deck2
    score1 = 0
    score2 = 0

    random.shuffle(deck1)
    random.shuffle(deck2)

    turn = 0
    while(score1 < 5 and score2 < 5):
        if (deck1[turn] > deck2[turn]):
            score1 += 1
        else:
            score2 += 1

        turn += 1

    if (score1 == 5):
        return 1
    else:
        return 2

def sim_games(Nsim, deck1, deck2):
    #Simulate games and return the proportion of times deck1 won
    count = 0
    
    for N in range(Nsim):
        result = play_game(deck1, deck2)
        if (result == 1):
            count += 1

    return count/Nsim

#Three decks
red_deck = [14, 14, 14, 14, 9, 9, 9, 9, 7, 7, 7, 7]
blue_deck = [13, 13, 13, 13, 11, 11, 11, 11, 6, 6, 6, 6]
black_deck = [12, 12, 12, 12, 10, 10, 10, 10, 8, 8, 8, 8]

Nsim = 100000 #Number of simulations

#Compute and print empirical probabilities
p_red_blue = sim_games(Nsim, red_deck, blue_deck)
print('Red deck beats blue deck approximately ' + str(p_red_blue) + ' of the time')

p_red_black = sim_games(Nsim, red_deck, black_deck)
print('Red deck beats black deck approximately ' + str(p_red_black) + ' of the time')

p_blue_black = sim_games(Nsim, blue_deck, black_deck)
print('Blue deck beats black deck approximately ' + str(p_blue_black) + ' of the time')
