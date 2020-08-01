# The Riddler Classic 2019-04-19: Circular Conundrum
# https://fivethirtyeight.com/features/what-comes-after-840-the-answer-may-surprise-you/
# Monte-Carlo simulation

import random
import math

Nsim = 1000000

n = 5

count = 0
for N in range(Nsim):
    
    #generate and sort random points
    points = [random.random()*2*math.pi for i in range(n)]
    points.sort()
    
    mindist = 2*math.pi

    #check angle in between first point to last (wrap around)
    for i in range(n):
        j = (i + n - 1)%n
        
        dist = (points[j] - points[i])%(2*math.pi)

        mindist = min([dist, mindist])

    #check if smallest angle fits within half circle
    if mindist < math.pi:
        count += 1

print('Empirical probability:')
print(count/Nsim)
print('Theoretical probability:')
print(n/2**(n - 1))
