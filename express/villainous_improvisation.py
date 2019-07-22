#2018-06-08 Riddler Express: Villainous Improvisation
#Monte-Carlo simulation

import random

num_performers = 5 #number of performers
num_villains = 2 #number of villains
num_rounds = 2 #number of rounds

performers = list(range(num_performers))

Nsim = 100000 #number of replications
count = 0

for n in range(Nsim):

    #store history of who was a villain
    was_villain = [[0 for j in range(num_rounds)] for i in range(num_performers)]

    #simulate each round
    for j in range(num_rounds):
        #remember the previous roles
        prev_characters = list.copy(performers)
        is_derangement = False

        #randomly generate an arrangement to achieve a derangement
        while (not is_derangement):
            random.shuffle(performers)
            is_derangement = not any([performers[i] == prev_characters[i] for i in range(num_performers)])

        #determine whether each performer was a villian for that round
        #the first num_villains in the derangement are counted as villains
        for i in range(num_performers):
            was_villain[i][j] = any([performers[k] == i for k in range(num_villains)])

    #check if any performer played the villain in all the rounds
    count += any([all(was_villain[i][:]) for i in range(num_performers)])
            
#print empirical probability
print(count/Nsim)
