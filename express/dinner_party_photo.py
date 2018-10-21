#The Riddler Express 2016-11-18: Dinner Party Photo
#Computational solution to the problem.
#Treats the random lineup generating process as one where the first person from the first couple is inserted in the first spot from the left. The second person from the first couple is randomly inserted into an empty spot. Then the first person from the second couple is inserted into the next available spot from the left, then the second person from the second couple randomly inserted into a remaining spot. This process continues for all couples.
#Implements a recursive function that can compute the probability from any lineup where x amount of couples have been inserted

#function that determines whether a given lineup has a couple standing together
def isTogether(lineup):
  for i in range(0, len(lineup) - 1):
    if lineup[i] != 0 and lineup[i] == lineup[i + 1]:
      return True
    
  return False

#function that returns the number of non-zero (filled) spots in the lineup  
def numNonZero(lineup):
  return len([x for x in lineup if x > 0])

#function that returns the number of zero (unfilled) spots in the lineup
def numZero(lineup):
  return len([x for x in lineup if x == 0])

#recursive function for probability that a lineup has no couple standing together
def prNotTogether(lineup):
  #couple detected together
  if isTogether(lineup):
    return 0
    
  #lineup full and no couple together
  elif len(lineup) == numNonZero(lineup):
    return 1
    
  else:
    p = 0 #probability
    n = lineup.index(0) #the next empty spot
    c = int(numNonZero(lineup)/2) + 1 #the next couple to be inserted
    
    #insert first person of the couple
    lineup[n] = c
    
    #loop through all empty spots
    for i in range(n + 1, len(lineup)):

      if lineup[i] == 0:
        #create a copy of the lineup in a
        #a = lineup cannot be used because it makes a point to the original lineup
        a = list(lineup)
        
        #insert second person of the couple into the next empty spot and compute probability of that configuration leading to no couples together, weighted by the probability of achieving that configuration (the reciprocal of number of empty spots)
        a[i] = c
        p += prNotTogether(a)/numZero(lineup)
    
    return p

N = 14 #number of people (divide by 2 to get number of couples)

print(prNotTogether([0]*N))
