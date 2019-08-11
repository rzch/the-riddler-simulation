#The Riddler Classic 2018-08-31: Random Nim
#Monte-Carlo simulation
#Puzzle: https://fivethirtyeight.com/features/the-new-national-pastime-competitive-coin-flipping/
#Discussion of winning moves: https://plus.maths.org/content/play-win-nim

import random

Nsim = 500000 #Number of simulations
count = 0

#number of starting heaps
nheaps = 3
#number of sides per dice
nsides = 6

def nim_sum(heaps):
    #This function takes a list of the heap sizes in decimal, and outputs the
    #XOR addition of all the heap sizes in decimal

    sum = 0

    for i in range(len(heaps)):
        sum = sum ^ heaps[i]

    return sum

def apply_move(heaps, move):
    #This function takes the list of heap sizes and a move (a list of the changes
    #to the heaps), and outputs the new heap sizes
    
    return [heaps[k] + move[k] for k in range(len(heaps))]
    
def winning_move(heaps):
    #This function takes a list of the heap sizes, and outputs a winning move
    #(a list of the changes to the heaps)

    #enumerate through all the possible moves
    for i in range(len(heaps)):
        for j in range(heaps[i]):
            #candidate move is to remove j + 1 coins from the ith heap
            candidate_move = [-(j + 1)*(k == i) for k in range(len(heaps))]

            #check if the move causes the nim sum to be zero
            new_heaps = apply_move(heaps, candidate_move)
            if (nim_sum(new_heaps) == 0):
                return candidate_move

    #If they have no winning moves, return the last candidate_move
    return candidate_move

for n in range(Nsim):

    #generate the random starting heaps
    heaps = [random.randint(1, nsides) for i in range(nheaps)]

    #play the game
    while (sum(heaps) > 0):

        #apply A's optimal move
        A_move = winning_move(heaps)
        heaps = apply_move(heaps, A_move)

        #check if A has won
        if (sum(heaps) == 0):
            count += 1
            break

        #apply D's optimal move
        D_move = winning_move(heaps)
        heaps = apply_move(heaps, D_move)

#compute empirical probability
print('Empirical probability of first player winning:')
print(count/Nsim)
#compute theoretical probability
print('Theoretical probability of first player winning:')
print(192/216)
