#The Riddler Express 2018-04-13: Nut Hand
#Monte-Carlo simulation

import random
import itertools #for itertools.combinations()
import time #for time.time()

#---------------------------------------
#Classes and functions

class Card:
    #Card class with rank and suite
    def __init__(self, num, suite):
        self.num = num
        #2: two
        #10: ten
        #11: jack
        #12: queen
        #13: king
        #14: ace
        self.suite = suite
        #1: spades
        #2: clubs
        #3: hearts
        #4: diamonds

def rank(hand):
    #determines the rank of a hand
    #see https://en.wikipedia.org/wiki/List_of_poker_hands
    nums = [c.num for c in hand]
    suites = [c.suite for c in hand]

    counts = [0]*15
    for i in range(5):
        counts[nums[i]] += 1

    #check for straight
    if (max(nums) - min(nums) == 4 and max(counts) == 1):
        has_straight = True
    else:
        has_straight = False

    #check for flush
    if (all([s == suites[0] for s in suites])):
        has_flush = True
    else:
        has_flush = False

    if (has_straight and has_flush):
        return 1 #straight flush

    if (max(counts) == 4):
        return 2 #four of a kind

    if (max(counts) == 3 and sorted(counts)[-2] == 2):
        return 3 #full house

    if (has_flush):
        return 4 #flush

    if (has_straight):
        return 5 #straight

    if (max(counts) == 3):
        return 6 #three of a kind

    if (max(counts) == 2 and sorted(counts)[-2] == 2):
        return 7 #two pair

    if (max(counts) == 2):
        return 8 #one pair

    return 9 #high card

def rank_hands(hand1, hand2):
    #ranks two five-card hands
    #returns 1 if hand1 outranks hand2, returns 2 if hand2 outranks hand1
    #returns 0 if tied
    #see https://en.wikipedia.org/wiki/List_of_poker_hands
    
    r1 = rank(hand1)
    r2 = rank(hand2)
    
    if (r1 < r2):
        return 1
    elif (r1 > r2):
        return 2

    #break ties
    nums1 = sorted([c.num for c in hand1], reverse = True)
    nums2 = sorted([c.num for c in hand2], reverse = True)
    if (r1 == 1 or r1 == 5): #straight flush or straight
        if (nums1[0] > nums2[0]):
            return 1
        elif (nums1[0] < nums2[0]):
            return 2
    elif (r1 == 2): #four of a kind
        quad1 = max(set(nums1), key=nums1.count) #finds the mode
        quad2 = max(set(nums2), key=nums2.count) #finds the mode
        if (quad1 > quad2):
            return 1
        elif (quad1 < quad2):
            return 2

        kicker1 = min(set(nums1), key=nums1.count)
        kicker2 = min(set(nums2), key=nums2.count)

        if (kicker1 > kicker2):
            return 1
        elif (kicker1 < kicker2):
            return 2
    elif (r1 == 3): #full house
        full1 = max(set(nums1), key=nums1.count) #finds the mode
        full2 = max(set(nums2), key=nums2.count) #finds the mode
        if (full1 > full2):
            return 1
        elif (full1 < full2):
            return 2

        over1 = min(set(nums1), key=nums1.count)
        over2 = min(set(nums2), key=nums2.count)

        if (over1 > over2):
            return 1
        elif (over1 < over2):
            return 2
    elif (r1 == 4 or r1 == 9): #flush or high card
        for i in range(5):
            if (nums1[i] > nums2[i]):
                return 1
            elif (nums1[i] < nums2[i]):
                return 2
    elif (r1 == 6): #three of a kind
        trip1 = max(set(nums1), key=nums1.count) #finds the mode
        trip2 = max(set(nums2), key=nums2.count) #finds the mode
        if (trip1 > trip2):
            return 1
        elif (trip1 < trip2):
            return 2

        kickers1 = list(filter(lambda a: a != trip1, nums1)) #remove trip from hand
        kickers2 = list(filter(lambda a: a != trip2, nums2)) #remove trip from hand
        high_kicker1 = max(kickers1)
        high_kicker2 = max(kickers2)
        if (high_kicker1 > high_kicker2):
            return 1
        elif (high_kicker1 < high_kicker2):
            return 2
        
        low_kicker1 = min(kickers1)
        low_kicker2 = min(kickers2)
        if (low_kicker1 > low_kicker2):
            return 1
        elif (low_kicker1 < low_kicker2):
            return 2
    elif (r1 == 7): #two pair
        kicker1 = min(set(nums1), key=nums1.count)
        kicker2 = min(set(nums2), key=nums2.count)

        nums1.remove(kicker1)
        nums2.remove(kicker2)
        high_pair1 = max(nums1)
        high_pair2 = max(nums2)
        if (high_pair1 > high_pair2):
            return 1
        elif (high_pair1 < high_pair2):
            return 2       

        low_pair1 = min(nums1)
        low_pair2 = min(nums2)
        if (low_pair1 > low_pair2):
            return 1
        elif (low_pair1 < low_pair2):
            return 2        
    elif (r1 == 8): #one pair
        pair1 = max(set(nums1), key=nums1.count) #finds the mode
        pair2 = max(set(nums2), key=nums2.count) #finds the mode
        if (pair1 > pair2):
            return 1
        elif (pair1 < pair2):
            return 2

        kickers1 = list(filter(lambda a: a != pair1, nums1)) #remove pair from hand
        kickers2 = list(filter(lambda a: a != pair2, nums2)) #remove pair from hand
        high_kicker1 = max(kickers1)
        high_kicker2 = max(kickers2)
        if (high_kicker1 > high_kicker2):
            return 1
        elif (high_kicker1 < high_kicker2):
            return 2

        kickers1.remove(high_kicker1)
        kickers2.remove(high_kicker2)
        mid_kicker1 = max(kickers1)
        mid_kicker2 = max(kickers1)        
        if (mid_kicker1 > mid_kicker2):
            return 1
        elif (mid_kicker1 < mid_kicker2):
            return 2
        
        low_kicker1 = min(kickers1)
        low_kicker2 = min(kickers2)
        if (low_kicker1 > low_kicker2):
            return 1
        elif (low_kicker1 < low_kicker2):
            return 2
        
    return 0

def best_hand(community, hole):
    #determines the best hand available from 5 community cards and 2 hole cards

    #generate all combinations
    combs = list(itertools.combinations(range(5), 3))

    best_i = 0
    #go through each of the combinations
    for i in range(len(combs)):

        if (i == 0):
            #form the 5-card hand
            hand = [community[j] for j in combs[i]] + hole
            
        elif (i > 0):
            #form the 5-card hand, compare and take the best
            temp_hand = [community[j] for j in combs[i]] + hole
            if (rank_hands(hand, temp_hand) > 1):
                best_i = i
                hand = temp_hand.copy()

    return hand, rank(hand)

def best_hand2(community, pool):
    #determines the best hand available from 5 community cards and a pool of possible hole cards

    #generate all combinations
    combs_community = list(itertools.combinations(range(5), 3))
    combs_pool = list(itertools.combinations(range(len(pool)), 2))

    #go through each of the combinations
    for i in range(len(combs_community)):
        for j in range(len(combs_pool)):
            if (i == 0 and j == 0):
                #form the 5-card hand
                hand = [community[k] for k in combs_community[i]] \
                       + [pool[k] for k in combs_pool[j]]
            else:
                #form the 5-card hand, compare and take the best
                temp_hand = [community[k] for k in combs_community[i]] \
                            + [pool[k] for k in combs_pool[j]]
                if (rank_hands(hand, temp_hand) > 1):
                    hand = temp_hand.copy()

    return hand, rank(hand)

def print_cards(cards):
    #prints a list of cards
    for i in range(len(cards)):
        print(cards[i].__dict__)

    print()
    
#---------------------------------------
#Unit tests

perform_unit_tests = False

if (perform_unit_tests):
    #straight flush
    test_hand1 = [Card(11, 2), Card(10, 2), Card(9, 2), Card(8, 2), Card(7, 2)]
    #four of a kind
    test_hand2 = [Card(5, 1), Card(5, 2), Card(5, 3), Card(5, 4), Card(2, 2)]
    #full house
    test_hand3 = [Card(6, 1), Card(6, 2), Card(6, 3), Card(13, 4), Card(13, 2)]
    #flush
    test_hand4 = [Card(11, 4), Card(9, 4), Card(8, 4), Card(4, 4), Card(3, 4)]
    #straight
    test_hand5 = [Card(10, 4), Card(9, 1), Card(8, 3), Card(7, 4), Card(6, 2)]
    #three of a kind
    test_hand6 = [Card(12, 4), Card(12, 1), Card(12, 3), Card(9, 4), Card(2, 2)]
    #two pair
    test_hand7 = [Card(11, 4), Card(11, 1), Card(3, 3), Card(3, 4), Card(2, 2)]
    #one pair
    test_hand8 = [Card(10, 4), Card(10, 1), Card(8, 3), Card(7, 4), Card(4, 2)]
    #high card
    test_hand9 = [Card(13, 4), Card(12, 1), Card(7, 3), Card(4, 4), Card(3, 2)]

    #straight flush
    better_hand1 = [Card(12, 2), Card(11, 2), Card(10, 2), Card(9, 2), Card(8, 2)]
    #four of a kind
    better_hand2 = [Card(6, 1), Card(6, 2), Card(6, 3), Card(6, 4), Card(2, 2)]
    #full house
    better_hand3 = [Card(7, 1), Card(7, 2), Card(7, 3), Card(13, 4), Card(13, 2)]
    #flush
    better_hand4 = [Card(13, 4), Card(9, 4), Card(8, 4), Card(4, 4), Card(3, 4)]
    #straight
    better_hand5 = [Card(11, 4), Card(10, 1), Card(9, 3), Card(8, 4), Card(7, 2)]
    #three of a kind
    better_hand6 = [Card(13, 4), Card(13, 1), Card(13, 3), Card(9, 4), Card(2, 2)]
    #two pair
    better_hand7 = [Card(11, 4), Card(11, 1), Card(5, 3), Card(5, 4), Card(2, 2)]
    #one pair
    better_hand8 = [Card(10, 4), Card(10, 1), Card(8, 3), Card(7, 4), Card(5, 2)]
    #high card
    better_hand9 = [Card(13, 4), Card(12, 1), Card(7, 3), Card(4, 4), Card(4, 2)]

    #unit tests
    print(rank(test_hand1) == 1)
    print(rank(test_hand2) == 2)
    print(rank(test_hand3) == 3)
    print(rank(test_hand4) == 4)
    print(rank(test_hand5) == 5)
    print(rank(test_hand6) == 6)
    print(rank(test_hand7) == 7)
    print(rank(test_hand8) == 8)
    print(rank(test_hand9) == 9)
    print()
    print(rank_hands(test_hand1, better_hand1) == 2)
    print(rank_hands(test_hand2, better_hand2) == 2)
    print(rank_hands(test_hand3, better_hand3) == 2)
    print(rank_hands(test_hand4, better_hand4) == 2)
    print(rank_hands(test_hand5, better_hand5) == 2)
    print(rank_hands(test_hand6, better_hand6) == 2)
    print(rank_hands(test_hand7, better_hand7) == 2)
    print(rank_hands(test_hand8, better_hand8) == 2)
    print(rank_hands(test_hand9, better_hand9) == 2)
    print()
    print(rank_hands(test_hand1, test_hand2) == 1)
    print(rank_hands(test_hand3, test_hand3) == 0)

    test_community = [Card(5, 3), Card(6, 3), Card(14, 3), Card(9, 3), Card(5, 1)]
    test_hole = [Card(7, 3), Card(8, 3)]

    test_best_hand, test_rank = best_hand(test_community, test_hole)
    print()
    print(sorted([c.num for c in test_best_hand]) == [5, 6, 7, 8, 9])
    print()

#---------------------------------------
#Monte-Carlo simulation
    
Nsim = 1000 #Number of simulations
count = 0

#generate a standard deck with ace spades and ten spades removed
deck = [Card(i, j) for i in range(2, 15) for j in [1, 2, 3, 4] \
        if not (i == 14 and j == 1) and not (i == 10 and j == 1)]
#create AT hole card
hole = [Card(14, 1), Card(10, 1)]

starttime = time.time()

for N in range(Nsim):

    #shuffle and deal
    random.shuffle(deck)
    community = deck[0:5]
    pool = deck[5:50]

    #compare best possible hands
    hand1, rank1 = best_hand(community, hole)
    hand2, rank2 = best_hand2(community, pool)
    r = rank_hands(hand1, hand2)
    #nut hand cannot be beaten
    if (r <= 1):
        count += 1
        
    #rint_cards(community)
    #print_cards(hand1)
    #print(rank1)
    #print_cards(hand2)
    #print(rank2)

endtime = time.time()

print('Time elapsed: ' + str(endtime - starttime) + ' seconds')
print(str(Nsim) + ' simulations run')
print('Estimated probability that AT is the nut hand:')
print(count/Nsim)

Nsim = 1000
count = 0

#create full deck
deck = [Card(i, j) for i in range(2, 15) for j in [1, 2, 3, 4]]

starttime = time.time()

for N in range(Nsim):

    #shuffle and deal
    random.shuffle(deck)
    community = deck[0:5]
    pool = deck[5:52]

    #determine nut hand
    hand2, rank2 = best_hand2(community, pool)

    #check if AT
    if (hand2[3].suite == hand2[4].suite and \
        (hand2[3].num == 14 and hand2[4].num == 10 or \
         hand2[3].num == 10 and hand2[4].num == 14)):
        count += 1
    
    #print_cards(hand2)

endtime = time.time()

print('Time elapsed: ' + str(endtime - starttime) + ' seconds')
print(str(Nsim) + ' simulations run')
print('Estimated probability that the nut hand is AT:')
print(count/Nsim)
