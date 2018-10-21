#The Riddler 2017-08-25 Vitamin Routine

import random

#============
#Monte carlo

N = 500000 #Number of simulations

count = 0 #Count total days across all simulations

for i in range(0, N):
    days = 0 #Number of days passed
    halfpills = 0 #Number of half pills in bottle
    
    #Loop days until a half-pill is picked
    while True:
        days += 1
        if random.random() < halfpills/100:
            break
        else:
            halfpills += 1

    count += days

#Print average
print(count/N)


#============
#Analytical

#Recurrence relation
def recurrence(k):
    if k == 0:
        return 1
    else:
        return k*recurrence(k - 1)/100 + 1

#Recurrence relation for extra credit
def recurrence_extra(k):
    a = 2 #Number of times a full-pill is more likely than half-pill
    if k == 0:
        return 1
    else:
        return a*k*recurrence_extra(k - 1)/(a*k + 100 - k) + 1

print(recurrence(100))
print(recurrence_extra(100))
