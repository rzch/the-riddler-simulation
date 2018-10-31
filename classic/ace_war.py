#The Riddler Classic 2017-09-08: Ace War
#Monte-Carlo simulation

import random

Nsim = 5000 #Number of simulations
count = 0 #Count number of wins

for N in range(Nsim):

    #Create and shuffle opponent deck
    opdeck = [item for item in range(12) for i in range(4)]
    random.shuffle(opdeck)

    mydeck = [12, 12, 12, 12] #Four aces

    #Cards in play
    myplay = []
    opplay = []
    
    while (len(mydeck) > 0 and len(opdeck) > 0):

        #Draw 1 card each
        myplay.insert(0, mydeck[0])
        mydeck.pop(0)

        opplay.insert(0, opdeck[0])
        opdeck.pop(0)

        #Compare first card
        if (myplay[0] > opplay[0]):
            winner_determined = True #Win
            #Add both shuffled cards to my deck
            myplay.extend(opplay)
            opplay = []
            random.shuffle(myplay)
            mydeck.extend(myplay)
            myplay = []
            
        elif (myplay[0] < opplay[0]): #Lose
            winner_determined = True
            #Add both shuffled cards to opponent deck
            opplay.extend(myplay)
            myplay = []
            random.shuffle(opplay)
            opdeck.extend(opplay)
            opplay = []
            
        elif (myplay[0] == opplay[0]): #Tie, play war
            winner_determined = False

        #Play War
        while(not winner_determined):
            #Draw 2 cards each
            if (len(mydeck) > 0):
                myplay.insert(0, mydeck[0])
                mydeck.pop(0)
            
            if (len(mydeck) > 0):
                myplay.insert(0, mydeck[0])
                mydeck.pop(0)

            if (len(opdeck) > 0):
                opplay.insert(0, opdeck[0])
                opdeck.pop(0)

            if (len(opdeck) > 0):
                opplay.insert(0, opdeck[0])
                opdeck.pop(0)

            #Win War
            if (len(mydeck) > 0 and len(opdeck) > 0 and myplay[0] > opplay[0]):
                winner_determined = True
                #Add shuffled in play cards to my deck
                myplay.extend(opplay)
                opplay = []
                random.shuffle(myplay)
                mydeck.extend(myplay)
                myplay = []

            #Lose War
            elif (len(mydeck) > 0 and len(opdeck) > 0 and myplay[0] < opplay[0]):
                winner_determined = True
                #Add shuffled in play cards to opponent deck
                opplay.extend(myplay)
                myplay = []
                random.shuffle(opplay)
                opdeck.extend(opplay)
                opplay = []

            #Tie, draw again
            elif (len(mydeck) > 0 and len(opdeck) > 0 and myplay[0] == opplay[0]):
                winner_determined = False
                
            #End game if a player runs out of cards
            if (len(mydeck) == 0 or len(opdeck) == 0):
                winner_determined = True

    if (len(opdeck) == 0):
        count += 1 #Count win

#Print empirical winning probability
print(count/Nsim)
