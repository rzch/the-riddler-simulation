#The Riddler Classic 2017-12-08: Pub Game
#Monte-Carlo simulation

import random

def throw_dart():
    #Throw a dart uniformly inside unit circle using rejection sampling
    inside_circle = False

    while(not inside_circle):
        x = 2*random.random() - 1
        y = 2*random.random() - 1

        if (x**2 + y**2 <= 1):
            inside_circle = True

    return x, y


Nsim = 1000000 #number of simulations
scores = [0]*Nsim
count = 0

for N in range(Nsim):
    score = 0
    xhist = [0]*7
    yhist = [0]*7
    in_play = True

    while(in_play):
        x, y = throw_dart()
        xhist[score] = x
        yhist[score] = y
        #compare with location of other thrown darts
        for i in range(score):
            if ((xhist[i] - x)**2 + (yhist[i] - y)**2 < 1):
                in_play = False

        if (in_play == True):
            score += 1

    if (score > 1):
        count += 1
        
    scores[N] = score

print('Probability of getting a score greater than 1:')
print(count/Nsim)
print('Expected score:')
print(sum(scores)/Nsim)
