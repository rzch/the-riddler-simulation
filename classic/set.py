# The Riddler Classic 2020-03-20: SET
# https://fivethirtyeight.com/features/how-many-sets-of-cards-can-you-find/
# Monte-Carlo simulation

import random
import itertools

class card:

    def __init__(self, number, shape, color, shading):

        self.number = number
        self.shape = shape
        self.color = color
        self.shading = shading


    def is_set(card1, card2, card3):
        #determine whether 3 cards form a set

        number_flag = False
        shape_flag = False
        color_flag = False
        shading_flag = False

        #check all number different
        if (card1.number != card2.number and card1.number != card3.number
            and card2.number != card3.number):
            number_flag = True
        #check all number the same
        elif (card1.number == card2.number and card1.number == card3.number):
            number_flag = True

        #check all shape different
        if (card1.shape != card2.shape and card1.shape != card3.shape
            and card2.shape != card3.shape):
            shape_flag = True
        #check all shape the same
        elif (card1.shape == card2.shape and card1.shape == card3.shape):
            shape_flag = True

        #check all color different
        if (card1.color != card2.color and card1.color != card3.color
            and card2.color != card3.color):
            color_flag = True
        #check all color the same
        elif (card1.color == card2.color and card1.color == card3.color):
            color_flag = True

        #check all shading different
        if (card1.shading != card2.shading and card1.shading != card3.shading
            and card2.shading != card3.shading):
            shading_flag = True
        #check all shading the same
        elif (card1.shading == card2.shading and card1.shading == card3.shading):
            shading_flag = True

        if (number_flag and shape_flag and color_flag and shading_flag):
            return True
        else:
            return False

#attributes
numbers = [1, 2, 3]
shapes = ["oval", "diamond", "squiggle"]
colors = ["r", "g", "p"]
shadings = ["solid", "shaded", "outlined"]

#create the deck
deck = []
for i1 in numbers:
    for i2 in shapes:
        for i3 in colors:
            for i4 in shadings:
                deck.append(card(i1, i2, i3, i4))


Nsim = 100000 #number of simulations
count = 0

for N in range(Nsim):

    #sample a random board of 12
    board = random.sample(deck, 12)

    #generate all 12 choose 3 combinations from the board
    combos = list(itertools.combinations(board, 3))

    #check whether any of the combinations is a set
    for c in combos:
        if card.is_set(c[0], c[1], c[2]):
            count += 1
            break

print(count/Nsim)
