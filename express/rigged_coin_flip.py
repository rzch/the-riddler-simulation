#The Riddler Express 2018-11-02: Rigged Coin Flip
#Monte-Carlo simulation

import random

Nsim = 1000000 #number of simulations

#----------------------------------------------------
#Methods for coin flips and comparing flip results

def coin_flip():
    #Outputs the result of a single coin flip
    return bool(random.getrandbits(1))

def flip_coins(x):
    #Outputs the result of x coin flips
    return [coin_flip() for i in range(x)]

def match_template(flips, template):
    #Determine whether a flip sequence matches a template
    x = len(win_template)
    return all([flips[i] == template[i] for i in range(x)])

#----------------------------------------------------
#Game with 1/3 win chance

count = 0
for n in range(Nsim):

    winner_found = False

    #if this is flipped, A wins the game:
    win_template = [True, True]
    #if this is flipped, replay the game:
    reset_template = [False, False]

    x = len(win_template)
    
    while (not winner_found):

        flips = flip_coins(x)
        #determine whether game ends
        if (not match_template(flips, reset_template)):
            winner_found = True

            #determine whether A wins
            if (match_template(flips, win_template)):
                count += 1
                
print('Win proportion for game with 1/3 win chance:')
print(count/Nsim)

#----------------------------------------------------
#Game with 1/4 win chance

count = 0
for n in range(Nsim):

    #if this is flipped, A wins the game:
    win_template = [True, True]

    x = len(win_template)
    flips = flip_coins(x)
    #determine whether A wins
    if (match_template(flips, win_template)):
        count += 1
                
print('Win proportion for game with 1/4 win chance:')
print(count/Nsim)

#----------------------------------------------------
#Game with 1/5 win chance

count = 0
for n in range(Nsim):

    winner_found = False
    
    #if this is flipped, A wins the game:
    win_template = [True, True, True]
    #if this is flipped, replay the game:
    reset_templates = [[False, False, False],
                       [False, False, True],
                       [False, True, False]]

    x = len(win_template)
    
    while (not winner_found):

        flips = flip_coins(x)
        #determine whether game ends
        if (not any([match_template(flips, t) for t in reset_templates])):
            winner_found = True
            #determine whether A wins
            if (match_template(flips, win_template)):
                count += 1
                
print('Win proportion for game with 1/5 win chance:')
print(count/Nsim)
