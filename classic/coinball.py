#The Riddler Classic 2017-10-13: Coinball
#Monte-Carlo simulation of optimal strategies

import random

Nsim = 10000 #number of simulations

n = 50 #number of tosses per player

def playrush(score1, score2):
    if random.random() < 0.5:
        return score1 + 1, score2
    else:
        return score1, score2 + 1

def playpass(score1, score2):
    if random.random() < 0.5:
        return score1 + 2, score2
    else:
        return score1, score2 + 2
    
#1---Case when opponent goes first and always Rushes
count = 0
for N in range(Nsim):
    score1 = 0
    score2 = 0

    for i in range(n):
        round = i + 1
        
        #opponent goes first and rushes
        score1, score2 = playrush(score1, score2)

        #player optimal strategy
        if (score1 > score2):
            score1, score2 = playrush(score1, score2) #rush
        elif (score1 < score2):
            score1, score2 = playpass(score1, score2) #pass
        elif (score1 == score2):
            score1, score2 = playrush(score1, score2) #rush

    if (score1 > score2):
        count += 1
    elif (score1 == score2): #count draw as a half
        count += 0.5
        
print('Case when opponent goes first and always Rushes:')
print(count/Nsim)

#2---Case when opponent goes second and always Rushes
count = 0
for N in range(Nsim):
    score1 = 0
    score2 = 0

    for i in range(n):
        round = i + 1

        #player optimal strategy
        if (score1 > score2):
            score1, score2 = playrush(score1, score2) #rush
        elif (score1 < score2):
            score1, score2 = playpass(score1, score2) #pass
        elif (score1 == score2):
            if (round%2 == 0): #even round
                score1, score2 = playrush(score1, score2) #rush
            else: #odd round
                score1, score2 = playpass(score1, score2) #rush

        #opponent goes first and rushes
        score1, score2 = playrush(score1, score2)
        
    if (score1 > score2):
        count += 1
    elif (score1 == score2): #count draw as a half
        count ++ 0.5
        
print('Case when opponent goes second and always Rushes:')
print(count/Nsim)

#3---Case when opponent goes first and always Passes
count = 0
for N in range(Nsim):
    score1 = 0
    score2 = 0

    for i in range(n):
        round = i + 1
        
        #opponent goes first and rushes
        score1, score2 = playpass(score1, score2)

        #player optimal strategy
        if (score1 > score2):
            score1, score2 = playrush(score1, score2) #rush
        elif (score1 < score2):
            score1, score2 = playpass(score1, score2) #pass
        elif (score1 == score2):
            score1, score2 = playrush(score1, score2) #rush

    if (score1 > score2):
        count += 1
    elif (score1 == score2): #count draw as a half
        count += 0.5

print('Case when opponent goes first and always Passes:')
print(count/Nsim)

#4---Case when opponent goes second and always Passes
count = 0
for N in range(Nsim):
    score1 = 0
    score2 = 0

    for i in range(n):
        round = i + 1

        #player optimal strategy
        if (score1 > score2):
            score1, score2 = playrush(score1, score2) #rush
        elif (score1 < score2):
            score1, score2 = playpass(score1, score2) #pass
        elif (score1 == score2):
            if (round%2 == 0): #even round
                score1, score2 = playrush(score1, score2) #rush
            else: #odd round
                score1, score2 = playpass(score1, score2) #rush

        #opponent goes first and rushes
        score1, score2 = playpass(score1, score2)
        
    if (score1 > score2):
        count += 1
    elif (score1 == score2): #count draw as a half
        count += 0.5

print('Case when opponent goes second and always Passes:')
print(count/Nsim)

#5---Case when opponent goes first and both play optimally
Nsim = 1000000
count = 0
for N in range(Nsim):
    score1 = 0
    score2 = 0

    for i in range(n):
        round = i + 1

        #opponent optimal strategy
        if (score1 < score2):
            score1, score2 = playrush(score1, score2) #rush
        elif (score1 > score2):
            score1, score2 = playpass(score1, score2) #pass
        elif (score1 == score2):
            if (round%2 == 0): #even round
                score1, score2 = playrush(score1, score2) #rush
            else: #odd round
                score1, score2 = playpass(score1, score2) #rush

        #player optimal strategy
        if (score1 > score2):
            score1, score2 = playrush(score1, score2) #rush
        elif (score1 < score2):
            score1, score2 = playpass(score1, score2) #pass
        elif (score1 == score2):
            score1, score2 = playrush(score1, score2) #rush
        
    if (score1 > score2):
        count += 1
    elif (score1 == score2): #count draw as a half
        count += 0.5

print('Case when opponent goes first and both play optimally:')
print(count/Nsim)
