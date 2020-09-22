# The Riddler Classic 2019-07-19: Optimal Tournament
# https://fivethirtyeight.com/features/can-you-construct-the-optimal-tournament/
# Monte-Carlo simulation of optimal tournament

import random

Nsim = 100000 #number of simulations
rankings = [1, 2, 3, 4] #rankings of players
count = 0

def play_game(player1, player2):
    #simulate the winner of a game

    if (random.random() < 2/3):
        if (player1 > player2):
            return player1
        else:
            return player2
    else:
        if (player1 > player2):
            return player2
        else:
            return player1       


for N in range(Nsim):

    players = rankings.copy()
    random.shuffle(players)

    A = players[0]
    B = players[1]
    C = players[2]
    D = players[3]

    AB = play_game(A, B)
    ABC = play_game(AB, C)
    ABD = play_game(AB, D)
    champ = play_game(ABC, ABD)

    if (champ == 4):
        count += 1

print(count/Nsim)
