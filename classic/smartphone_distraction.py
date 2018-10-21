#The Riddler 22-12-2015: Smarthphone Distraction
#Monte-carlo simulation

import random

n = 100000 #Number of simulations

minutes = []

for i in range(0, n):
	count = 0
	me = random.randint(1, 5)
	sis = random.randint(1, 5)
	
	while (me != 0 and sis != 0):
		me -= 1
		sis -= 1
		count += 1
		
		if (me == 0 and sis != 0):
			me = random.randint(1, 5)
			
		if (sis == 0 and me != 0):
			sis = random.randint(1, 5)
	
	minutes.append(count)

sum = 0
for i in range(0, n):
	sum += minutes[i]
	
print(sum/n)
