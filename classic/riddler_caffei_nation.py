#The Riddler Classic 2019-04-05: Riddler Caffei-Nation
#https://fivethirtyeight.com/features/does-your-gift-card-still-have-free-drinks-on-it/
#Monte-Carlo simulation

import random

n = 50 #number of free drinks

Nsim = 1000000 #number of simulation replications

count = 0
leftover = [0]*Nsim
for N in range(Nsim):

    cards = [n for i in range(2)]

    while(cards[0] >= 0 and cards[1] >= 0):
        #pick a random card
        r = random.getrandbits(1)
        if (cards[r] > 0): #use up a random free drink
            cards[r] -= 1
        else: #no free drinks left on the card
            break

    #check how many free drinks are left on the other card
    leftover[N] = sum(cards)

    #check if there are also no free drinks left on the other card
    if (leftover[N] == 0):
        count += 1


print(count/Nsim)
print(sum(leftover)/Nsim)
