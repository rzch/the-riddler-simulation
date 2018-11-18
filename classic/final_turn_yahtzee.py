#The Riddler Classic 2018-03-09: Final Turn Yahtzee
#Monte-Carlo simulation of optimal strategies

import random

Nsim = 1000000 #number of simulations
count = 0

def roll_dice():
    return random.randint(1, 6)

#strategy of going for 3
for N in range(Nsim):

    #first and second rerolls
    if (roll_dice() == 3 or roll_dice() == 3):
        count += 1

print('Probability when going for 3:')
print(count/Nsim)

count = 0
#strategy of going for 3 and 6
for N in range(Nsim):

    numbers = [2, 4, 5]
    
    #first reroll
    r1 = roll_dice()
    r2 = roll_dice()

    #second reroll
    if (r1 in [2, 4, 5] and r2 in [2, 4, 5]): #two useless
        numbers.append(roll_dice())
        numbers.append(roll_dice())
        
    elif (r1 in [1, 6] and r2 == 3) or (r1 == 3 and r2 in [1, 6]): #win
        numbers.append(r1)
        numbers.append(r2)

    elif (r1 in [1, 6] and r2 != 3) or (r1 != 3 and r2 in [1, 6]): #at least one 1 or 6 and no 3
        numbers.append(1)
        numbers.append(roll_dice())

    else: #at least one 3 and the other useless
        numbers.append(3)
        numbers.append(roll_dice())

    if (sorted(numbers) == [1, 2, 3, 4, 5] or sorted(numbers) == [2, 3, 4, 5, 6]):
        count += 1


print('Probability when going for 3 or 6:')
print(count/Nsim)
