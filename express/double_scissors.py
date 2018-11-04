#The Riddler Express 2017-09-29: Double Scissors
#Monte-Carlo simulation of optimal strategies

import random

def decision(strategy):
    r = random.random()
    if (r <= strategy[0]):
        return 0 #rock
    elif (r <= sum(strategy[0:1])):
        return 1 #double scissors
    elif (r <= sum(strategy[0:2])):
        return 2 #scissors
    else:
        return 3 #paper

def winner(decision1, decision2):
    if (decision1 == 0): #rock
        if (decision2 == 1 or decision2 == 2): #double scissors or scissors
            return 1 #player 1 win
        elif (decision2 == 3): #paper
            return 2 #player 2 win

    if (decision1 == 1): #double scissors
        if (decision2 == 1 or decision2 == 3): #scissors or paper
            return 1 #player 1 win
        elif (decision2 == 0): #rock
            return 2 #player 2 win

    if (decision1 == 2): #scissors
        if (decision2 == 3): #paper
            return 3 #player 1 auto win
        elif (decision2 == 0 or decision2 == 1): #rock or double scissors
            return 2 #player 2 win

    if (decision1 == 3): #paper
        if (decision2 == 0): #rock
            return 1 #player 1 win
        elif (decision2 == 1): #double scissors
            return 2 #player 2 win
        elif (decision2 == 2): #scissors
            return 4 #player 2 auto win

    return 0 #draw


Nsim = 1000000 #Number of simulations
N10 = 0 #Number of times it went to 1-0
count = 0

#rock, double scissors, scissors, paper
strategy00 = [0.52, 0, 0.24, 0.24]
strategy10 = [0.4, 0.33, 0, 0.27]
strategy01 = [0.55, 0, 0.21, 0.25]
strategy11 = [1/3, 1/3, 0, 1/3]

for N in range(Nsim):

    score1 = 0
    score2 = 0

    went_to_10 = False

    while(score1 < 2 and score2 < 2):

        #determine winner
        winner_decided = 0
        while(winner_decided == 0):
            if (score1 == 0 and score2 == 0):
                d1 = decision(strategy00)
                d2 = decision(strategy00)
            elif (score1 == 1 and score2 == 0):
                if (not went_to_10):
                    N10 += 1
                    
                went_to_10 = True
                
                d1 = decision(strategy10)
                d2 = decision(strategy01)
            elif (score1 == 0 and score2 == 1):
                d1 = decision(strategy01)
                d2 = decision(strategy10)        
            elif (score1 == 1 and score2 == 1):
                d1 = decision(strategy11)
                d2 = decision(strategy11)
                
            winner_decided = winner(d1, d2)

        #update scores
        if (winner_decided == 1): #player 1 win
            score1 += 1
        elif (winner_decided == 2): #player 2 win
            score2 += 1
        elif (winner_decided == 3): #player 1 auto win
            score1 = 2
        elif (winner_decided == 4): #player 2 auto win
            score2 = 2

    #Increase count given it went to 1-0
    if (score1 == 2 and went_to_10):
        count += 1

#Empirical probability
print(count/N10)
    
