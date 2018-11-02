#The Riddler Classic 2017-09-15: Breaking Sticks
#Monte Carlo simulation

import random

Nsim = 500000 #Number of simulations
count1 = 0
count2 = 0
count3 = 0
count4 = 0

for N in range(Nsim):
    #-----------Problem 1
    r1 = random.random()
    r2 = random.random()
    a = min(r1, r2)
    b = max(r1, r2) - a
    
    c = 1 - a - b

    #Triangle condition
    if (a + b > c and a + c > b and b + c > a):
        count1 += 1
        
    #-----------Problem 2
    a = random.random()
    b = random.random()
    c = random.random()

    #Triangle condition
    if (a + b > c and a + c > b and b + c > a):
        count2 += 1

    #-----------Problem 3
    r1 = random.random()
    r2 = random.random()
    a = min(r1, r2)
    b = max(r1, r2) - a
    
    c = 1 - a - b

    #Acute angle condition
    if (a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and b**2 + c**2 > a**2):
        count3 += 1

    #-----------Problem 4
    a = random.random()
    b = random.random()
    c = random.random()

    #Acute angle condition
    if (a**2 + b**2 > c**2 and a**2 + c**2 > b**2 and b**2 + c**2 > a**2):
        count4 += 1

print('Problem 1:')
print(count1/Nsim)
print('Problem 2:')
print(count2/Nsim)
print('Problem 3:')
print(count3/Nsim)
print('Problem 4:')
print(count4/Nsim)
