#The Riddler Classic 2016-11-18: The Lonesome King
#analytical computation and monte carlo simulation

import random
import math

#function returning the binomial coefficient, ie. n choose k
def binomcoeff(n, k):
  return int(math.factorial(n)/math.factorial(k)/math.factorial(n - k))

#======================================================
#Simulation for the distribution of subjects chosen

N = 1 #Number of simulations

n = 6 #starting number of subjects

dist = [0]*n #initialise list to store frequency

for x in range(0, N):
  subjects = [0]*n #binary list for subjects
  for i in range(0, n):
    #a subject is made 1 if it is chosen
    subjects[random.randint(0, n - 1)] = 1

  #the sum of the list gives the number of subjects chosen
  #increment the frequency
  dist[sum(subjects) - 1] += 1

##print empirical distribution  
#print('1 chosen ... ' + str(n) + ' chosen')
#print([x/N for x in dist])

##print analytical distribution
#print([binomcoeff(n, i)*f(n, i)/(n**n) for i in range(1, n + 1)])

#======================================================
#Analytical probability for eventually 1 subject remaining

#function for number of ways to write a sequence n elements long where each of i elements must be used at least once
def f(n, i):
  x = i**n
  for j in range(i - 1, 0, -1):
    x -= binomcoeff(i, j)*f(n, j)
  
  return x

#function for probability that i subjects are chosen from n
def pr_cho(n, i):
  return binomcoeff(n, i)*f(n, i)/(n**n)

#function for probability that eventually 1 subject remains from n starting
def pr_1rem(n):
  
  dict_pr1rem = dict() #store previous values in dictionary
  dict_pr1rem[2] = 0.5 #initial trivial value
  
  
  for x in range(3, n + 1):
    
    #compute probability of eventually 1 remaining for each starting number of subjects
    p = pr_cho(x, x - 1)
    for i in range(1, x - 1):
      p += pr_cho(x, i)*dict_pr1rem[x - i]
    
    #store in dictionary
    dict_pr1rem[x] = p
  
  return dict_pr1rem[n]
  
n = 8 #number of starting subjects
print(pr_1rem(n))

#========================================================
#Simulation for probability of eventually 1 subject remaining

N = 100000 #number of simulations
n = 8 #number of starting subjects
count = 0 #store number of times there are 1 subject remaining

for x in range(0, N):
  num_subjects = n #starting number of subjects
  
  while num_subjects > 1:
    subjects = [0]*num_subjects
    
    #randomly choose subjects
    for i in range(0, num_subjects):
      subjects[random.randint(0, num_subjects - 1)] = 1
    
    #reduce number of subjects based on number chosen
    num_subjects = num_subjects - sum(subjects)
  
  if num_subjects == 1:
    count += 1
  
print(count/N)
