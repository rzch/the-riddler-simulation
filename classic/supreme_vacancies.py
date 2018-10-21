from random import randint,uniform

num_reps = 100000000
accum = 0

num_vacancies = 0
duration_accum = 0

# A running list of the vacant seats, starting with all of them.
Vacancies = [0,1,2,3,4,5,6,7,8]

# A list of the times justices in the 9 seats are due to retire
# or die yes I went there. We use num_reps as a dummy value to
# start.
Expiration = [num_reps]*9

for rep in range(num_reps):
	# the current "rep" is the number of 2-year periods that have 
	# passed.

	# Here we will figure the average number of vacancies since
	# the last election, including new vacancies. 
	
	# If there were vacancies after the last election it's 
	# because there is not joint control, so those vacancies
	# remain. So the Average number of vacancies over this past
	# 2-year cycle is at least:
	AvgVacancies = len(Vacancies)

	# Create a list for the expiration times seats will
	# have going into this election.
	NewExpiration = [num_reps]*9
	for i in range(9):
		# Looping through the seats
		if rep-1 < Expiration[i] <= rep:
			# Seat i has been vacated since the last election
			if SameParty:
				# Seat was filled as needed until due to expire after 
				# this election, so it's been continuously occupied,
				# and adds nothing to average vacancies. For each filled
				# vacancy we increment num_vacancies. We leave 
				# duration_accum alone, as the duration is 0.
				NewExp = Expiration[i]
				while NewExp <= rep:
					# Seat went vacant before now, so:
					num_vacancies += 1
					NewExp += uniform(0,20)
				NewExpiration[i] = NewExp
			else:
				# Seat has been unfilled for (rep - Expiration[i]) reps,
				# adding that same amount to the average number of
				# vacancies since the last rep. 
				AvgVacancies += (rep - Expiration[i])
				# This is the only place we add to the list of vacancies.
				Vacancies.append(i)
				# We keep track of when the seat went vacant so that we
				# can record the duration of the vacancy when it's filled.
				NewExpiration[i] = Expiration[i]
		else:
			# Two cases here. (1) Seat remains occupied so there's no 
			# effect on AvgVacancies. (2) Seat was already vacant as of 
			# the last election (or as of the start) and remains in 
			# Vacancies, so AvgVacancies has already counted it. We track 
			# when it will or did expire.
			NewExpiration[i] = Expiration[i]

	Expiration = NewExpiration
	# We add up the average numbers of vacancies between reps, and will 
	# divide by num_reps to give the overall average.
	accum += AvgVacancies

	# Hold elections
	SameParty = randint(0,1)

	if SameParty:
		# Fill empty seats
		for i in Vacancies:
			# Again we increment num_vacancies upon filling one.
			num_vacancies += 1
			if Expiration[i] > rep:
				# These are the initial vacancies
				duration_accum += rep
			else:
				duration_accum += rep - Expiration[i]
			Expiration[i] = rep + uniform(0,20)
		# This is the only place seats are removed from the vacancies list.
		Vacancies = []

print("Average number of vacancies:",accum/num_reps)
print("Average duration of a vacancy:",2*duration_accum/num_vacancies,"years")

