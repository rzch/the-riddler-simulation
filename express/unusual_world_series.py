#The Riddler Express 2019-11-22: Unusual World Series
#Monte-Carlo simulation and theoretical calculation
#Puzzle: https://fivethirtyeight.com/features/can-you-decode-the-riddler-lottery/

import random
import math

n = 7 #number of games played
schedule = [True, True, False, False, False, True, True] #team 1 hosting schedule
c = 6 #home streak required
m = math.ceil(n) #minimum number of games to win the series

p = 0.54 #probability of home win
q = 1 - p #probability of home loss

Nsim = 1000000 #number of simulations

count = 0
for N in range(Nsim):

    t1 = 0 #team1 score
    t2 = 0 #team2 score
    streak = 0
    
    for i in range(n):
        result = random.random() < q
        if (result): #simulate whether home lost
            streak += 1

            if (streak >= c): #check if streak achieved
                count += 1
                break
            
        else: #streak broken
            streak = 0

        #update series score
        if (result):
            if (schedule[i]):
                t1 += 1
            else:
                t2 += 1
        else:
            if (schedule[i]):
                t2 += 1
            else:
                t1 += 1            

        if (t1 >= 4 or t2 >= 4): #series finished
            break

print('Empirical probability:')
print(count/Nsim)

