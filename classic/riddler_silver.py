#The Riddler Classic 2018-09-07: Riddler Silver
#Monte-Carlo simulation

import random

ncards = 100 #number of cards to collect
cards = list(range(ncards)) #list of all cards
packsize = 10 #size of a pack
packs_perweek = 10 #number of packs that can be purchased per week

Nsim = 50000 #Number of simulations

weeks = [0]*Nsim
allnumpacks = [0]*Nsim

for n in range(Nsim):

    #set of cards remaining to collect
    collector_list = set(cards)

    week = 0
    numpacks = 0
    
    #keep buying pakcs while there are cards to collect
    while(len(collector_list) > 0):
        week += 1
        
        for i in range(packs_perweek):
            #generate a random pack
            pack = random.sample(cards, packsize)
            numpacks += 1
            
            for j in range(packsize):
                #remove collected card from set
                collector_list.discard(pack[j])

            if (len(collector_list) == 0):
                break

        
    allnumpacks[n] = numpacks
    weeks[n] = week

#compute average weeks and packs to collect all cards
print('Average number of weeks:')
print(sum(weeks)/Nsim)
print('Average number of packs:')
print(sum(allnumpacks)/Nsim)
