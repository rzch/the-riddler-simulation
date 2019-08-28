#The Riddler Classic 2018-10-19: Riddleria Archipelago
#Monte-Carlo simulation

import random

#----------------------------------------------------
#Functions

def generate_archipelago(n):
    #This function generates a random valid archipelago with n islands.
    #The archipelago is the form of a 2d list with represents the adjacency
    #matrix of the tree.
    
    maxchildren = 2 #maximum number of children each island can have

    #create blank archipelago
    archipelago = [[0 for i in range(n)] for j in range(n)]

    #index each island
    islands = list(range(n))

    #initial level of the tree
    generation = [0]

    #list of islands that need to be connected to the archipelago
    islands_to_connect = list.copy(islands)
    islands_to_connect.remove(0)

    #add islands to the archipelago until there are no more left to add
    while (len(islands_to_connect) > 0):

        #previous level
        old_gen = list.copy(generation)

        #to store the new level
        generation = []

        #each island in the current level spawns connections to unconnected
        #islands
        for i in range(len(old_gen)):
            #randomly determine how many connections
            s = random.randint(1, min(maxchildren, len(islands_to_connect)))
            #randomly choose which islands to connect to
            children = random.sample(islands_to_connect, s)

            #attach each island to the tree
            for j in range(len(children)):
                archipelago[old_gen[i]][children[j]] = 1
                archipelago[children[j]][old_gen[i]] = 1
                generation.append(children[j])
                islands_to_connect.remove(children[j])

            #exit if there are no more islands left to connect
            if (len(islands_to_connect) == 0):
                break
            
    return archipelago

def get_neighbours(island, archipelago):
    #This function returns a list of all the neighbour islands connected to the
    #provided island

    n = len(archipelago)

    return [i for i in range(n) if archipelago[island][i] == 1]

def num_communities(archipelago):
    #This function returns the number of disparate communities in an archipelago

    c = 0
    
    n = len(archipelago)

    #get a list of all the islands that have not erupted
    islands = [i for i in range(n) if archipelago[i][i] != -1]

    #while there are islands that have not been counted yet
    while (len(islands) > 0):
        c += 1

        #begin a search for all the islands connected to the first island
        community = set([islands[0]]) #store as set so adding non-unique element wont change size
        nc = 0 #size of the community
        
        #keep adding islands to the community until the size stops changing
        while(len(community) != nc):
            nc = len(community)

            #set to add newfound islands
            new_community = set.copy(community)

            #get and add all the neighbours of the community to the community
            for i in community:
                neighbours = get_neighbours(i, archipelago)
                for j in range(len(neighbours)):
                    new_community.add(neighbours[j])

            community = set.copy(new_community)

        #remove all islands in the community from the list of uncounted islands
        for i in community:
            islands.remove(i)

    return c

def erupt(archipelago, p):
    #This function simulates an eruption on the archipelago with probability p

    n = len(archipelago)

    for i in range(n):

        if (random.random() < p):
            #if the island erupts, set all the elements in the ith row and col
            #as -1 to denote the node is deleted from the graph
            for j in range(n):
                archipelago[i][j] = -1
                archipelago[j][i] = -1

    return archipelago

#----------------------------------------------------
#Main script

n = 15 #number of islands
p = 0.5 #probability of an island erupting

Nsim = 100000 #number of simulation replications
communities = [0]*Nsim #store number of communities left each replication

for N in range(Nsim):

    archipelago = generate_archipelago(n)

    archipelago = erupt(archipelago, p)

    communities[N] = num_communities(archipelago)

#print results
print('Average number of communities:')
print(sum(communities)/Nsim)
print('Theoretical expectation:')
print(1 - p + (n - 1)*p*(1 - p))
