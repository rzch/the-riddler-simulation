#The Riddler Classic 2018-10-26: Organisational Obsession
#Monte-Carlo simulation

import random

class Card:

    def __init__(self, rank, suit):

        self.rank = rank
        self.suit = suit
    
def draw(n, deck):
    #This function returns a random hand of size n drawn from a deck

    return random.sample(deck, n)

def same_colour(s1, s2):
    #This function returns whether two suits are of the same colour
    
    if (s1 == 'Clubs' and s2 == 'Spades'):
        return True
    elif (s1 == 'Spades' and s2 == 'Clubs'):
        return True
    elif (s1 == 'Hearts' and s2 == 'Diamonds'):
        return True    
    elif (s1 == 'Diamonds' and s2 == 'Hearts'):
        return True

    return False

def is_organised(hand):
    #This function determines whether a hand is organised

    #use a dictionary to count how many of each suit are in the hand
    suits = {'Clubs', 'Spades', 'Diamonds', 'Hearts'}
    count_suits = dict()

    for s in suits:
        count_suits[s] = sum([c.suit == s for c in hand])

    #go through the cards
    i = 0
    while (i < len(hand)):
        #count sequentially all cards of the same suit
        current_suit = hand[i].suit
        j = i
        while (j < len(hand) and hand[j].suit == current_suit):
            j += 1

        #if all the cards counted sequentially of the same suit
        #are not all the cards of the same suit in the hand
        if (j - i < count_suits[current_suit]):
            return False

        #reached end of the hand
        if (j >= len(hand)):
            return True

        #if the next suit is of the same colour
        if (same_colour(current_suit, hand[j].suit)):
            #if there are two different colours in the hand
            if ((count_suits['Clubs'] > 0 or count_suits['Spades'] > 0) and
                (count_suits['Hearts'] > 0 or count_suits['Diamonds'] > 0)):
                return False

        i = j

    return True
    
def get_moves(hand):
    #This function returns a list of all the possible moves that can be made
    #for a given hand

    n = len(hand)

    moves = []
    
    for i in range(1, n + 1): #loop through block sizes
        for j in range(n - i + 1): #loop through each block of that size
            for k in range(n - i + 1): #loop through each position where that block can be placed

                temp_hand = list.copy(hand)

                #extract the block
                block = temp_hand[j:(j + i)]
                for c in block:
                    temp_hand.remove(c)

                #move the block to the new position
                move = temp_hand[0:k] + block + temp_hand[k:len(hand)]

                #add to list of moves
                moves.append(move)

    return moves

def is_sortable(hand):
    #This function returns whether a hand can be sorted

    moves = get_moves(hand)

    for m in moves:
        if (is_organised(m)):
            return True

    return False

def print_cards(hand):
    #This function prints the cards in a hand, useful for debugging

    s = ''
    for c in hand:
        s += c.suit[0] + str(c.rank) + ','

    print(s)

#------------------------------------------------------------------------
#Unit tests
    
suits1 = ['Clubs', 'Diamonds', 'Spades', 'Hearts']
suits2 = ['Clubs', 'Spades', 'Diamonds', 'Hearts']
deck1 = [Card(r, s) for s in suits1 for r in range(1, 14)]
deck2 = [Card(r, s) for s in suits2 for r in range(1, 14)]
deck3 = [Card(r, suits1[0]) for r in range(1, 7)]
deck4 = [Card(r, suits1[0]) for s in suits2[0:2] for r in range(1, 4)]
deck5 = [Card(r, suits1[0]) for s in suits2[2:4] for r in range(1, 4)]

hand1 = [Card(5, 'Diamonds'), Card(6, 'Hearts'), Card(3, 'Diamonds'),
         Card(5, 'Hearts'), Card(2, 'Hearts'), Card(10, 'Hearts')]
hand2 = [Card(2, 'Spades'), Card(3, 'Clubs'), Card(5, 'Spades'),
         Card(13, 'Clubs'), Card(1, 'Clubs'), Card(4, 'Clubs')]
hand3 = [Card(5, 'Diamonds'), Card(3, 'Diamonds'), Card(6, 'Hearts'),
         Card(5, 'Hearts'), Card(2, 'Hearts'), Card(10, 'Hearts')]

assert is_organised(deck1) == True, "Unit test fail"
assert is_organised(deck2) == False, "Unit test fail"
assert is_organised(deck3) == True, "Unit test fail"
assert is_organised(deck4) == True, "Unit test fail"
assert is_organised(deck5) == True, "Unit test fail"

assert is_sortable(hand1) == True, "Unit test fail"
assert is_sortable(hand2) == True, "Unit test fail"
assert is_organised(hand3) == True, "Unit test fail"

#------------------------------------------------------------------------
#Main script

Nsim = 100000 #Number of simulations
count = 0

n = 6 #Hand size

for N in range(Nsim):

    #draw cards
    hand = draw(n, deck1)

    #determine if sortable
    if is_sortable(hand):
        count += 1
    
#compute empirical probability
print(count/Nsim)
    
