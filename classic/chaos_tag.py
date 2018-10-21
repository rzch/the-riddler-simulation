#The Riddler Classic 2017-06-16: Chaos Tag
#Monte-Carlo simulation

import random

Nsim = 50000 #number of simulations
tags_count = [0]*Nsim


N = 6 #number of players
players = list(range(N)) #list of players

for x in range(Nsim):
    num_tags = 0 #count tags in game
    
    active = [1]*N #track whether a player is active
    tagged_by = [-1]*N #track who the player is tagged by

    while (sum(active) > 1): #while no winner
        #determine active players
        active_players = [i for i in players if active[i] == 1]
        #sample two random players to be involved in a tagging
        players_tagging = random.sample(active_players, 2)
        tagger = players_tagging[0]
        tagged = players_tagging[1]

        #make the tagged player inactive
        active[tagged] = 0
        tagged_by[tagged] = tagger

        #free all the inactive players who were tagged by the current tagged player
        for i in range(N):
            if (tagged_by[i] == tagged):
                active[i] = 1
                tagged_by[i] = -1

        num_tags += 1

    tags_count[x] = num_tags

#print empirical average
print(sum(tags_count)/Nsim)
