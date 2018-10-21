import math
import random
from collections import defaultdict

#Function to compute the binomial coefficient
def binomial(n, k):
  if k == 0:
      return 1
  elif 2*k > n:
      return binomial(n,n-k)
  else:
      e = n-k+1
      for i in range(2,k+1):
          e *= (n-k+i)
          e /= i
      return e
      

#=======================================
#Can change these settings
N = 11 #Number of generations to compute for
p = 0.8 #Probability of multiplication

#=======================================
#Theoretical

q = 1 - p #Complement of p

#Declare multidimensional dictionary to hold probability distribution
pdist = defaultdict(dict)

#Populate trivial distribution for 1st generation
pdist[1][0] = q
pdist[1][2] = p

#For each generation
for n in range(2, N + 1): 
  #For each possible number of organism in this generation
  for x in range(0, 2**n + 1, 2): 
    S = 0 #Summation variable
    nm1 = n - 1 #n minus 1
    i = int(0.5*x) #Half of x
    
    #Compute sum
    for j in range(math.ceil(0.25*x), 2**(nm1 - 1) + 1):
      y = 2*j
      S = S + binomial(y, i)*(p**i)*(q**(y - i))*pdist[nm1][y]
    
    #Add to dictionary  
    pdist[n][x] = S

print('Theoretical:')  
print(pdist[N][0])

#========================================
#Simulation

Nsim = 40000 #Number of simulations
count = 0 #Store the number of times of extinction

for i in range(0, Nsim):
  
  organisms = 1 #Start with 1 organism
  #Loop through all generations up until the one desired
  for n in range(1, N + 1):
    survived = 0 #The number of organisms which survive
    #Loop through each organism and determine if it survives
    for x in range(0, organisms):
      if random.random() < p:
        survived = survived + 1
    
    #Calculate the new number of organsims
    organisms = 2*survived
  
  #Check if the species are extinct
  if organisms == 0:
    count = count + 1

print('Simulated:')
print(count/Nsim)