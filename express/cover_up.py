# The Riddler Classic 2019-02-15: Cover Up
# https://fivethirtyeight.com/features/come-on-down-and-escape-the-maze/

import random

d = 5 #number of digits

Nsim = 1000000 #number of simulations

count = 0

for N in range(Nsim):

    #generate random price
    price = [random.randint(1, i + 2) for i in range(d)]

    #generate random initial guess
    guess = [random.randint(1, i + 2) for i in range(d)]

    #list of available options for each digit
    options = [list(range(1, i + 3)) for i in range(d)]
    #remove initial guess from list of options
    for i in range(d):
        options[i].remove(guess[i])

    #check whether there are any matches
    match = [price[i] == guess[i] for i in range(d)]

    #contestant can continue if there are any digits correct
    life = any(match)
    
    while(life):

        #check if contestant has won
        if (all(match)):
            count += 1
            break

        correct = False
        for i in range(d):
            if (not match[i]):
                #swap digit with available options
                guess[i] = random.sample(options[i], 1)[0]
                options[i].remove(guess[i])

                #check whether swap is correct
                if (guess[i] == price[i]):
                    correct = True

        #contestant can continue if there are any swaps correct
        life = correct
        
        #check whether there are any matches
        match = [price[i] == guess[i] for i in range(d)]

#print empirical win probability    
print(1.0*count/Nsim)
