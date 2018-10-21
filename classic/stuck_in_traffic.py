#The Riddler 5/2/2016: Stuck in Traffic
#Monte-carlo simulate the expected number of groups
#Naive approach

import random

#number of simulations
N = 10000

#group size
n = 40

counts = []

for i in range(0, N):

	numbers = []

	for i in range(0, n):
		numbers.append(i + 1)

	random.shuffle(numbers)
	
	smallers = 0
	for i in range(0, n - 1):
		if (numbers[i] > numbers[i + 1]):
			smallers += 1
			
	counts.append(smallers + 1)

#calculate average
sum = 0
for i in range(0, N):
	sum += counts[i]

print(sum/N)

#analytical answer
print(1 + (n - 1)/2)
