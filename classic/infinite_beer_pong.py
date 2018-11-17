#The Riddler Classic 2018-11-16: Infinite Beer Pong
#Monte-Carlo simulation

import random

nsim = 10000 #number of simulations

def mcsim(N):
    count_rounds = 0
    count_balls = 0
    
    for n in range(nsim):

        #generate empty cups
        cups = [[] for i in range(N)]

        #play a round while there are any empty cups
        while(any([cup == [] for cup in cups])):
            #simulate a round
            
            #throwing
            while(any([cup == [] for cup in cups])):
                cups[random.randint(1, N) - 1].append(random.randint(1, N))
                count_balls += 1

            #pruning
            cups = [[ball for ball in cups[c] if ball == c + 1] for c in range(N)]
            count_rounds += 1

    return count_rounds, count_balls

#---------------------------------------------
#Single N

N = 10
count_rounds, count_balls = mcsim(N)
print('Average rounds per game:')
print(count_rounds/nsim)
print('Average balls per game:')
print(count_balls/nsim)

#---------------------------------------------
#Multiple N

N = [x + 1 for x in range(26)] #number of cups

for j in range(len(N)):
    count_rounds, count_balls = mcsim(j)
    print(str(j) + '\t' + str(count_rounds/nsim) + '\t' + str(count_balls/nsim))
