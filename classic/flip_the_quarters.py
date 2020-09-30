# The Riddler Classic 2019-06-21: Flip the Quarters
# https://fivethirtyeight.com/features/i-would-walk-500-miles-and-i-would-riddle-500-more/
# Monte-Carlo simulation of strategy

import random

Nsim = 100000 #number of simulations
moves = [0]*Nsim
count = 0

def random_rotate(table):
    #performs random rotation of the table in place
    
    r = random.random()

    temp0 = table[0]
    temp1 = table[1]
    temp2 = table[2]
    temp3 = table[3]
    
    if (r < 0.25):
        table[0] = temp1
        table[1] = temp2
        table[2] = temp3
        table[3] = temp0
    elif (r < 0.5):
        table[0] = temp2
        table[1] = temp3
        table[2] = temp0
        table[3] = temp1
    elif (r < 0.75):
        table[0] = temp3
        table[1] = temp0
        table[2] = temp1
        table[3] = temp2
    
def flip_one(table):
    #flips one quarter in place

    table[0] = not table[0]

def flip_two_adjacent(table):
    #flips two adjacent quarters in place

    table[0] = not table[0]
    table[1] = not table[1]

def flip_two_opposite(table):
    #flips two oppostite quarters in place

    table[0] = not table[0]
    table[2] = not table[2]

def flip_three(table):
    #flips three quarters in place
    
    table[0] = not table[0]
    table[1] = not table[1]
    table[2] = not table[2]
    
def flip_four(table):
    #flips four quarters in place
    
    table[0] = not table[0]
    table[1] = not table[1]
    table[2] = not table[2]
    table[3] = not table[3]

instructions = [4, 2, 4, 1, 4, 2, 4, 0, 4, 2, 4, 1, 4, 2, 4]

for N in range(Nsim):

    #generate random table
    table = [bool(random.getrandbits(1)) for i in range(4)]

    #perform moves
    i = 0
    while (not all([q for q in table]) and i < len(instructions)):

        if (instructions[i] == 0):
            flip_one(table)
            
        elif (instructions[i] == 1):
            flip_two_adjacent(table)
            
        elif (instructions[i] == 2):
            flip_two_opposite(table)
            
        elif (instructions[i] == 3):
            flip_three(table)
            
        elif (instructions[i] == 4):
            flip_four(table)

        random_rotate(table)
        i += 1

        
    if all([q for q in table]):
        count += 1

    moves[N] = i

print('Proportion of tables solved:')
print(count/Nsim)
print('Average number of moves to solve:')
print(sum(moves)/Nsim)

    
