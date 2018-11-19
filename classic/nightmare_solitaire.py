#The Riddler Classic 2018-03-30: Nightmare Solitaire
#Monte-Carlo simulation

import random


class Card:
    #Card class with rank and colour
    def __init__(self, num, red):
        self.num = num
        self.red = red

def is_legal(top, bottom):
    #Check if the bottom card can be legally placed above of the top card 
    if (bottom.num == top.num - 1 and bottom.red != top.red):
        return True

    return False

Nsim = 1000000 #number of simulations
count = 0

#generate a standard deck
deck = [Card(i, j) for i in range(1, 14) for j in [True, False, True, False]]
    
for N in range(Nsim):

    random.shuffle(deck)

    #draw faceup cards
    faceup = deck[0:7]
    #draw 8 cards to deal
    deal = deck[7:15]

    has_legal_move = False

    #check for aces in faceup cards
    for i in range(7):
        if (faceup[i].num == 1):
            has_legal_move = True
            break

    if (has_legal_move):
        continue

    #check for aces in dealt cards
    for i in range(8):
        if (deal[i].num == 1):
            has_legal_move = True
            break

    if (has_legal_move):
        continue

    #check for legal moves between faceup cards
    for i in range(7):
        for j in range(7):
            if (is_legal(faceup[i], faceup[j])):
                has_legal_move = True
                break
        if (has_legal_move):
            break

    if (has_legal_move):
        continue    

    #check for legal moves from dealt cards on faceup cards
    for i in range(8):
        for j in range(7):
            if (is_legal(faceup[j], deal[i])):
                has_legal_move = True
                break
        if (has_legal_move):
            break

    if (has_legal_move == False):
        count += 1

print(count/Nsim)
    
