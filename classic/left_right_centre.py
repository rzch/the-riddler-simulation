#The Riddler Classic 2017-12-22: Left Right Centre
#Monte-Carlo simulation

import random

Nsim = 100000 #number of simulations
gamelengths = [0]*Nsim

n = 6 #number of players
d = 3 #starting cash

for N in range(Nsim):

    money = [3]*6
    pot = 0

    gamelength = 0
    
    while(not max(money) == sum(money)):
        turn = gamelength%n
        gamelength += 1
        
        for i in range(min(3, money[turn])): #roll up to 3 dice
            r = random.random()

            money[turn] -= 1
            if (r < 1/3): #roll 1 or 2
                money[(turn - 1)%n] += 1
            elif (r < 2/3): #roll 3 or 4
                 money[(turn + 1)%n] += 1            
            else: #roll 5 or 6
                pot += 1

            if (max(money) == sum(money)): #terminate the game if winner decided
                break

    gamelengths[N] = gamelength

print('Expected game length with ' + str(n) + ' players starting with $' + str(d) + ' each:')
print(sum(gamelengths)/Nsim)
