#The Riddler Express 2019-11-22: Unusual World Series
#Monte-Carlo simulation and theoretical calculation
#Puzzle: https://fivethirtyeight.com/features/can-you-decode-the-riddler-lottery/

import random

n = 7 #number of games
c = 6 #home 

p = 0.54 #probability of home win
q = 1 - p #probability of home loss

Nsim = 1000000 #number of simulations

count = 0
for N in range(Nsim):

    streak = 0
    for i in range(n):
        if (random.random() < q): #simulate whether home lost
            streak += 1

            if (streak >= c): #check if streak achieved
                count += 1
                break
            
        else: #streak broken
            streak = 0

print('Empirical probability:')
print(count/Nsim)

#-------------------------------------
#Theoretical calculation using the inclusion-exclusion principle

def choose_iter(elements, length):
    #recursive function used in choose(l, k)
    for i in range(len(elements)):
        if length == 1:
            yield (elements[i],)
        else:
            for next in choose_iter(elements[i+1:len(elements)], length-1):
                yield (elements[i],) + next
                
def choose(l, k):
    #function that returns all k-combinations in a list
    #adapted from https://stackoverflow.com/questions/127704/algorithm-to-return-all-combinations-of-k-elements-from-n
    return list(choose_iter(l, k))


#number of possible c-length streaks
d = n - c + 1

#generate the list of sets for all the possible c-length streaks
A = [set(range(i, i + c)) for i in range(d)]

prob = 0
for i in range(d):
    #generate combinations from A
    combs = choose(list(range(d)), i + 1)

    for j in range(len(combs)):
        #create the set union of sets from A
        s = set()
        for k in range(i + 1):
            s = s.union(A[combs[j][k]])

        #update summand in inclusion-exclusion principle formula
        prob += ((-1)**i)*(q**len(s))

print('Theoretical probability:')
print(prob)
