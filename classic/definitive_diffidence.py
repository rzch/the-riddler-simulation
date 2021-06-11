# The Riddler Classic 2021-05-07: Definitive Diffidence
# https://fivethirtyeight.com/features/can-you-find-a-trio-of-squares/
# Monte-Carlo simulation of 'strategising' interpretation

import random

Nsim = 1000000 #number of simulation trials
count = 0

for N in range(Nsim):

    X = random.random() #Martina's number
    Y = random.random() #Olivia's number

    #extract leading digits
    a = int(X*10)
    b = int(Y*10)

    #to count the number of turns waited
    waits_M = 0
    waits_O = 0

    M_turn = True

    #initialise with a round of each predicting their own number is bigger
    M_guess_X_bigger = True
    O_guess_X_bigger = False
    agree = False
        
    while (not agree):

        #wait leading digit number of turns before predicting other person's number
        if M_turn:
            if (waits_M >= a):
                M_guess_X_bigger = False
            else:
                M_guess_X_bigger = True

            waits_M += 1
        else:
            if (waits_O >= b):
                O_guess_X_bigger = True
            else:
                O_guess_X_bigger = False

            waits_O += 1
        
        M_turn = not M_turn

        agree = (M_guess_X_bigger == O_guess_X_bigger)
    
    if (M_guess_X_bigger and X > Y):
        count += 1
    elif (not M_guess_X_bigger and Y > X):
        count += 1

print(count/Nsim)
