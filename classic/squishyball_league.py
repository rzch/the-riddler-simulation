#The Riddler 2017-07-14 National Squishyball League
#Analytical computation and monte carlo simulation

import random

p = 0.6 #Probability of winning a game
q = 1 - p #Probability of losing a game

#==========================
#Analytical

def binomial(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke.
    See http://stackoverflow.com/questions/3025162/statistics-combinations-in-python
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0


def expected_winnings(n):
    #Function that returns the expected winnings for a best of n game series
    sum = 0
    m = int((n - 1)/2)
    for i in range(0, m + 1):
        sum = sum + binomial(m + i, m)*(p**(m + 1))*(q**i)

    return (1000000 - (m + 1)*10000)*sum

#Create a dictionary and fill it with expected winnings 
exps = dict()

#Step through the odd numbers from 1 to 99
for x in range(1, 100, 2):
    exps[x] = expected_winnings(x)

#Print the dictionary (to find which one is the highest)
#print(exps)

#25 is found to be the highest so print the value of expected winnings
print(exps[25])

#========================
#Monte carlo simulation

N = 300000 #Number of simulations
n = 25 #However many games the series is best of

mm = int((n - 1)/2) + 1 #Number of games the winner must win

winnings = 0 #Store total winnings over all the simulations

prize = 1000000 - 10000*mm #Prize money for winning a series

for x in range(0, N):
    play = 0 #Number of games won by our team
    opp = 0 #Number of games win by opponent
    #Play a series until win condition
    while play < mm and opp < mm:
        if random.random() < p:
            play += 1
        else:
            opp += 1
    #Add winnings if won
    if play > opp:
        winnings += prize

#Print average winnings
print(winnings/N)
            
