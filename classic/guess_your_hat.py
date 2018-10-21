#The Riddler Classic 2017-09-01: Guess Your Hat
#Monte Carlo simulation of optimal strategy

import random

Nsim = 1000000 #Number of simulations
num_wins = 0 #count number of times won

N = 2
n = 2**N - 1 #number of people

for x in range(Nsim):
    #randomly generate hats and format as a bit string
    #(with enough padded zeros to be n-bits long)
    #0 is black, 1 is white
    hats = format(random.getrandbits(n), '0' + str(n) + 'b')
    #store the decision for each player (-1 is pass)
    guesses = [-1]*n

    #implement optimal strategy
    for i in range(n):
        count = 0
        #XOR the numbers of all other black hats to obtain count
        for j in range(n):
            if (i != j and hats[j] == '0'):
                count = count ^ (j + 1)

        if (count == 0): #guess black if count is zero
            guesses[i] = 0
        elif (count == (i + 1)): #guess white if count is own number
            guesses[i] = 1

    #check win condition
    num_incorrect = 0
    num_correct = 0
    for i in range(n):
        if (guesses[i] != -1):
            if (guesses[i] == int(hats[i])):
                num_correct += 1
            else:
                num_incorrect += 1

    if (num_incorrect == 0 and num_correct >= 1):
        num_wins += 1

#print empirical win probability
print(num_wins/Nsim)
