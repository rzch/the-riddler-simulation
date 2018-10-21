#The Riddler 2016-09-16: Expected Draft position
#Monte-carlo simulation

import random

#number of simulations
n = 200000

places = []

for i in range(0, n):
	A = []
	B = []
	
	inA = False
	
	#simulate the coin flips
	for j in range(0, 30):
		if (random.random() > 0.5):
			A.append(j + 1)
			if (j == 9):
				inA = True
		else:
			B.append(j + 1)
			if (j == 9):
				inA = False
			
	
	#calculate the draft position
	A.sort()
	B.sort()
	
	if (inA):
		place = A.index(10) + 1
	else:
		place = len(A) + B.index(10) + 1
		
	places.append(place)

#compute average and standard deviation
sum = 0
for i in range(0, n):
	sum += places[i]

average = sum/n

sum = 0
for i in range(0, n):
	sum += (average - places[i])**2

std = (sum/(n - 1))**0.5

print(average)
print(std)
