#The Riddler Express 2018-03-09: One Turn Yahtzee
#Monte-Carlo simulation of strategies

import random

def roll():
    #rolls one 6-sided die
    return random.randint(1, 6)

def roll5():
    #rolls five 6-sided die
    return [random.randint(1, 6) for i in range(5)]

def unique_numbers(die):
    #returns the number of unique numbers
    return len(list(set(die)))

def freq_num(die, n):
    #returns the frequency of a number in dice
    return sum([1 for i in die if i == n])

def score(die):

    if (unique_numbers(die) == 1): #Yahtzee
        return 50
    elif (sorted(die) == [1, 2, 3, 4, 5] or \
          sorted(die) == [2, 3, 4, 5, 6]): #Large Straight
        return 40
    elif (1 in die and 2 in die and 3 in die and 4 in die) or \
         (2 in die and 3 in die and 4 in die and 5 in die) or \
         (3 in die and 4 in die and 5 in die and 6 in die): #Small Straight
        return 30
    elif (unique_numbers(die) == 2):
        unique_die = list(set(die))
        if (freq_num(die, unique_die[0]) == 2 and \
            freq_num(die, unique_die[1]) == 3) or \
            (freq_num(die, unique_die[0]) == 3 and \
            freq_num(die, unique_die[1]) == 2): #Full House
            return 25

    #Three of a Kind, Four of a Kind, Chance
    return sum(die)


Nsim = 1000000 #number of simulations
total_score1 = 0
total_score2 = 0

for N in range(Nsim):
    #strategy of rerolling both 5s
    total_score1 += score([4, 4, 4, roll(), roll()])

    #strategy of rerolling 4, 4, 5
    total_score2 += score([4, 5, roll(), roll(), roll()])

print(total_score1/Nsim)
print(total_score2/Nsim)

    
