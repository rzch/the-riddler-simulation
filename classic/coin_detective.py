#The Riddler Classic 2017-09-29: Coin Detective
#Computation of analytical solution and Monte-Carlo simulation

import random

def binomial(n, r):
    #Adapted from https://stackoverflow.com/questions/26560726/python-binomial-coefficient
    ''' Binomial coefficient, nCr, aka the "choose" function 
        n! / (r! * (n - r)!)
    '''
    p = 1    
    for i in range(1, min(r, n - r) + 1):
        p *= n
        p //= i
        n -= 1
    return p

#Coin flip probabilities
p1 = 0.5 #Fair coin
p2 = 0.6 #Doctored coin

#===========Analytical

nmax = 134 #Maximum flips which to compute for

p_greater = [0]*nmax

for x in range(nmax):
    n = x + 1 #Number of flips

    #PDFs on support {0, ..., n}
    pdf1 = [0]*(n + 1)
    pdf2 = [0]*(n + 1)

    #Compute the binomial probability mass distributions
    for i in range(n + 1):
        ncr = binomial(n, i);
        pdf1[i] = ncr*(p1**i)*(1 - p1)**(n - i)
        pdf2[i] = ncr*(p2**i)*(1 - p2)**(n - i)

    #Compute probability
    for i in range(n):
        p_greater[x] += pdf1[i]*sum(pdf2[(i + 1):(n + 1)]) #Strictly greater than
        p_greater[x] += 0.5*pdf1[i]*pdf2[i] #50-50 guess if equal

    p_greater[x] += 0.5*pdf1[n]*pdf2[n] 

print('Probability of correctly guessing the coin for number of flips:')
for x in range(nmax):
    print(f'n = {x+1:4}   p = {p_greater[x]:6.4}')

#===========Monte-Carlo

n = 134 #Number of flips

Nsim = 100000 #Number of simulations
count = 0

for N in range(Nsim):
    sum1 = 0;
    sum2 = 0;
    for i in range(n):
        if (random.random() < p1):
            sum1 += 1

        if (random.random() < p2):
            sum2 += 1

    if (sum2 > sum1):
        count += 1
    elif (sum2 == sum1 and random.random() < 0.5):
        count += 1

print('')
print('Empirical probability with n = ' + str(n) + ' and ' + str(Nsim) + ' simulations:')
print(count/Nsim)
