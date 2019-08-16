#The Riddler Express 2018-09-28: Election Day
#Monte-Carlo simulation

import random

Nsim = 100000 #number of simulations
count = 0

p_DD = 0.1 #minimum probability of both democrat
p_DR = 0.3 - p_DD #probability of democrat senate, republican house
p_RD = 0.8 - p_DD #probability of both republican senate, democrat house

for n in range(Nsim):

    count += (random.random() < p_DR + p_RD)

print('Max. probability:')
print(count/Nsim)

count = 0

p_DD = 0.3 #maximum probability of both democrat
p_DR = 0.3 - p_DD #probability of democrat senate, republican house
p_RD = 0.8 - p_DD #probability of both republican senate, democrat house

for n in range(Nsim):

    count += (random.random() < p_DR + p_RD)

print('Min. probability:')
print(count/Nsim)

