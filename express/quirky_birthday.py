#The Riddler Express 2017-06-16: Quirky Birthday Problem
#Monte Carlo simulation

import random

Nsim = 500000 #Number of simulations

d = 365 #Number of days in a year

ppl = 23 #Number of people
group1 = 14 #Number of people in one side of the family

count1 = 0
count2 = 0

for x in range(Nsim):
    birthdays1 = d*[0]
    birthdays2 = d*[0]
    #randomly generate the birthdays for first side
    for i in range(group1):
        birthdays1[random.randint(0, d - 1)] += 1

    #randomly generate the birthdays for other side
    for i in range(ppl - group1):
        birthdays2[random.randint(0, d - 1)] += 1
        
    #count the number of pairs (or multi) of birthdays for first side
    num_of_pairs1 = 0
    num_of_multi1 = 0
    
    for i in range(d):
        if (birthdays1[i] > 2):
            num_of_multi1 += 1
        elif (birthdays1[i] == 2):
            num_of_pairs1 += 1

    #count the number of pairs (or multi) of birthdays for other side      
    num_of_pairs2 = 0
    num_of_multi2 = 0
    
    for i in range(d):
        if (birthdays2[i] > 2):
            num_of_multi2 += 1
        elif (birthdays2[i] == 2):
            num_of_pairs2 += 1

    #count the number of pairs (or multi) of birthdays for combined
    num_of_pairs3 = 0
    num_of_multi3 = 0
    
    for i in range(d):
        if (birthdays1[i] + birthdays2[i] > 2):
            num_of_multi3 += 1
        elif (birthdays1[i] + birthdays2[i] == 2):
            num_of_pairs3 += 1

    if (num_of_pairs3 == 3 and num_of_multi3 == 0):
        count1 += 1

    if (num_of_pairs1 == 3 and num_of_multi1 == 0 and num_of_pairs2 == 0 and num_of_multi2 == 0):
        count2 += 1


print(count1/Nsim)
print(count2/Nsim)
