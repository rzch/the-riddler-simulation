#The Riddler Express 2018-08-31: Competitive Coin Flipping
#Monte-Carlo simulation

from random import getrandbits

Nsim = 1000000 #Number of simulations
count_red = 0 #Count number of times red wins

quiet = True #Flag to supress game output

#Sequence needed for red to win, True used to represent heads
red_sequence = [True, False]
#Sequence needed for blue to win
blue_sequence = [True, True]

def coin_flip():
    return bool(getrandbits(1))

for n in range(Nsim):

    winner_found = False

    #start flipping
    while (not winner_found):
        
        red_flips = []
        blue_flips = []

        red_found = False
        blue_found = False

        #simultaneously flip coins as long as someone 
        while (not red_found and not blue_found):

            red_flips.append(coin_flip())
            blue_flips.append(coin_flip())

            #check if red has found its sequence
            if (len(red_flips) >= len(red_sequence)):
                if (all([red_sequence[-(i + 1)] == red_flips[-(i + 1)] for i in range(len(red_sequence))])):
                    red_found = True

            #check if blue has found its sequence
            if (len(blue_flips) >= len(blue_sequence)):
                if (all([blue_sequence[-(i + 1)] == blue_flips[-(i + 1)] for i in range(len(blue_sequence))])):
                    blue_found = True

        #determine if there is a unique winner
        if (not (red_found and blue_found)):
            winner_found = True

            if (not quiet):
                print(red_flips)
                print(blue_flips)
                if (red_found):
                    print('Red wins')
                else:
                    print('Blue wins')
                
                print()
            
        else:
            if (not quiet):
                print(red_flips)
                print(blue_flips)
                print('Restart')


    count_red += red_found

#print empirical probability
print(count_red/Nsim)
