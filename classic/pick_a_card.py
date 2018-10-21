#The Riddler Classic 2017-04-21: Pick a Card
#Monte-Carlo simulation with optimal strategy

import random

Nsim = 500000 #number of simulations

count = 0

n = 100 #number of cards
k = 10 #number to draw

#create list of cards from 1 to 100
cards = list(range(n))
cards = [i + 1 for i in cards]

#thresholds in optimal strategy
threshold = [93, 92, 91, 89, 87, 84, 80, 72, 55, 10]

for x in range(Nsim):
    #sample cards
    draw = random.sample(cards, k)

    highest = max(draw)
    highest_seen = 0
    
    for i in range(k):
        highest_seen  = max(draw[i], highest_seen)
        if (draw[i] == highest_seen and draw[i] >= threshold[i]):
            break

    if (draw[i] == highest):
        count += 1

print(count/Nsim)
