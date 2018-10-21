#The Riddler 22/4/2016: Misanthropic Neighbours
#Group of 3

import random

n = 100 #street size

#===============Theoretical

f = dict() #use dictionary to store previously computed values
f[1] = 1 #initial value

#computed expected number of occupied houses using recurrence relation and dictionary lookup of stored values
for x in range(2, n + 1):
  fx = 0
  for i in range(3, x + 1):
    fx += f[i - 2]
  
  fx = 2*fx/x + 1
  f[x] = fx #store value
  
print(f[n]/n)

#===============Simulation

N = 1000 #number of simulations
fractions  = [] #store fraction of occupied houses for each simulation

for j in range(0, N):
  
  #binary list to represent occupied houses
  street = [0]*n
  #list of indexes for which houses are filled
  filled = [i for i, x in enumerate(street) if x == 1]
  #list of indexes for which houses are empty
  empty = [i for i, x in enumerate(street) if x == 0]

  diff = [n]

  #there are houses to be filled if the maximum distance between filled houses is greater than 3, eg. 010001
  while max(diff) > 3:
  
    filled = [i for i, x in enumerate(street) if x == 1]
    empty = [i for i, x in enumerate(street) if x == 0]
  
    #all eligible empty houses to be filled are the ones which do not have a neighbouring filled house
    eligible = list(filter(lambda x: x - 1 not in filled and x + 1 not in filled, empty))
  
    #randomly fill an eligible house
    street[random.choice(eligible)] = 1
  
    filled = [i for i, x in enumerate(street) if x == 1]
    empty = [i for i, x in enumerate(street) if x == 0]
  
    #insert indices so that the first and last houses are still counted when the distances between filled houses is computed
    filled.insert(0, -2)
    filled.append(n + 1)

    #calculate the distances between filled houses
    diff = [filled[i + 1] - filled[i] for i in range(len(filled) - 1)]
  
  fractions.append(sum(street)/n)

#compute the average fraction from all simulations
average = sum(fractions)/N
print(average)
