# The Riddler Express 2020-11-13: Daily Double
# https://fivethirtyeight.com/features/can-you-snatch-defeat-from-the-jaws-of-victory/
# Monte-Carlo simulation and numerical computation of expectation

import random

Nsim = 100000 #number of simulation replications

#construct jeopardy board
board = [200]*6 + [400]*6 + [600]*6 + [800]*6 + [1000]*6
n = len(board)

winnings = [0]*Nsim

for N in range(Nsim):

    x = 0

    d = random.randint(0, n-1) #random daily double location

    #go through each clue and update winnings
    for i in range(n):
        if (i == d):
            if (x <= 1000):
                x += 1000
            else:
                x *= 2

        else:
            x += board[i]

    winnings[N] = x

print('Empirical expectation:')
print(sum(winnings)/Nsim)

##---------------------------------------------------
#Numerical computation

E = 0

for i in range(n):
    s = sum(board[0:i])
    E += (n-1)*board[i]/n + max(1000, s)/n

print('Analytical expectation:')
print(E)

##---------------------------------------------------
#Extra credit

winnings = [0]*Nsim
order = list(range(n))

for N in range(Nsim):

    x = 0

    d = random.randint(0, n-1) #random daily double location

    #go through each clue in random order and update winnings
    random.shuffle(order)
    for i in order:
        if (i == d):
            if (x <= 1000):
                x += 1000
            else:
                x *= 2

        else:
            x += board[i]

    winnings[N] = x

print('Empirical expectation for random order:')
print(sum(winnings)/Nsim)
