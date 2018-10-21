#The Riddler Express 2017-01-13:Birthday Party Puzzle
#Script to Monte Carlo simulate solution
import random

N = 100000 #Number of simulations
counts = [0]*N
C = 30

for i in range(0, N):
  n = C
  count = 0 #count the number of tries to blow all candles
  
  #keep blowing until there are no candles left
  while n > 0:
    n = random.randint(0, n - 1)
    count += 1
  
  counts[i] = count

#Print empirical answer
average = sum(counts)/N
print(average)

#Print the analytical answer
print(sum([1/(i + 1) for i in range(0, C)]))
