#The Riddler Classic 2018-04-11: Find a Running Buddy
#Monte-Carlo simulation

#Note that the published Riddler solution is not correct because |Xi - Xj| are
#not independent random variables; the dependence is through Xi. Hence taking
#the product of complementary CDFs does not give the correct answer. This
#simulation computes values for the dependent and independent case, as well as
#the probability that *all* runners have a running buddy. 

import random

Nsim = 100000 #number of simulations

mu = 6.78 #mean
sig = 1.16 #standard deviation
s = 0.5 #running speed threshold

n = 18 #number of runners

count1 = 0 #independent case occurences
count2 = 0 #dependent case occurences
count3 = 0 #all runners have buddy occurences

for N in range(Nsim):
    #generate speeds
    speeds = [random.gauss(mu, sig) for i in range(n)]
    #generate speeds for independent sample
    speeds2 = [random.gauss(mu, sig) for i in range(n)]

    #minimum absolute difference for independent case
    indep_mindiff = min([abs(speeds2[i] - speeds[i]) for i in range(n - 1)])
    
    #minimum absolute difference between first runner and all others
    mindiff = min([abs(speeds[i] - speeds[1]) for i in range(n) if i != 1])

    #maximum over the minimum absolute difference between each runner and every other runner
    maxdiff = max([min([abs(speeds[i] - speeds[j]) for i in range(n) if i != j]) \
                   for j in range(n)])

    if (indep_mindiff <= s):
        count1 += 1

    if (mindiff <= s):
        count2 += 1
        
    if (maxdiff <= s):
        count3 += 1

print('Empirical probability that an individual runner has buddy (independent case):')
print(count1/Nsim)

print('Empirical probability that an individual runner has buddy:')
print(count2/Nsim)

print('Empirical probability that all runners have buddies:')
print(count3/Nsim)
