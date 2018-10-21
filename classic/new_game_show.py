#The Riddler 04-03-2016: New Game Show
#Simulate game show probability

import random
from datetime import datetime

random.seed(datetime.now())

n = 400000 #Number of simulations
count = 0

both_total = 0
both_count = 0

other_total = 0
other_count = 0

you_total = 0
you_count = 0

no_total = 0
no_count = 0

p = 0.8 #player cutoff
q = 0.6 #opponent cutoff

for i in range(0, n):
	you = False
	other = False
	
	x = random.random()
	if (x < p):
		x = random.random()
		you = True
		
	y = random.random()
	if (y < q):
		y = random.random()
		other = True

	if (you == False and other == False):
		no_total += 1
	elif (you == True and other == False):
		you_total += 1
	elif (you == False and other == True):
		other_total += 1
	elif (you == True and other == True):
		both_total += 1

	if (x > y):
		count += 1
		if (you == False and other == False):
			no_count += 1
		elif (you == True and other == False):
			you_count += 1
		elif (you == False and other == True):
			other_count += 1	
		elif (you == True and other == True):
			both_count += 1

print('Overall')
print('Simulated: ' + str(count/n))

if (p <= q):
	thpr = 0.5*p*q + (1 - p)*q*(p + 0.5*(1 - p)) + 0.5*p*(1 - q)**2 + (1 - p)*(1 - q)*((1 - q)/(1 - p) - 0.5*(1 - q)/(1 - p))
else:
	thpr = 0.5*p*q + (1 - p)*q*(p + 0.5*(1 - p)) + 0.5*p*(1 - q)**2 + (1 - p)*(1 - q)*(1 - 0.5*(1 - p)/(1 - q))
	
print('Theoretical: ' + str(thpr))

print('')
print('Both mulligan')
print('Simulated: ' + str(both_count/both_total))
print('Theoretical: ' + str(0.5))
print('')
print('Other mulligan')
print('Simulated: ' + str(other_count/other_total))
print('Theoretical: ' + str(0.5 + 0.5*p))
print('')
print('You mulligan')
print('Simulated: ' + str(you_count/you_total))
print('Theoretical: ' + str(0.5*(1 - q)))
print('')
print('None mulligan')
print('Simulated: ' + str(no_count/no_total))
if (p <= q):
	thpr = (1 - q)/(1 - p) - 0.5*(1 - q)/(1 - p)
else:
	thpr = 1 - 0.5*(1 - p)/(1 - q)
print('Theoretical: ' + str(thpr))
