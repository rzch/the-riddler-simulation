# The Riddler Classic 2021-02-05: Move the Tower
# https://fivethirtyeight.com/features/can-you-randomly-move-the-tower/
# Monte-Carlo simulation

import random

class Tower:
    #tower implemented as a list of stacks
    
    def __init__(self, state = [[3, 2, 1], [], []]):

        self.state = state
    
    def reset(self):
        #resets the tower to the starting state

        self.state = [[3, 2, 1], [], []]
        
    def move(self, col1, col2):
        #attempts to move a piece from col1 to col2, and returns a flag whether successful

        #needs to be a piece available to move
        if (len(self.state[col1]) > 0):
            #a piece cannot go on a piece smaller than ifself
            if (len(self.state[col2]) == 0 or self.state[col1][-1] < self.state[col2][-1]):
                self.state[col2].append(self.state[col1][-1])
                self.state[col1].pop()

                return True

        return False


    def isComplete(self):
        #check if the tower is complete

        if (self.state == [[], [3, 2, 1], []]):
            return True
        elif (self.state == [[], [], [3, 2, 1]]):
            return True

        return False

Nsim = 100000 #number of simulation replications
counts = [0]*Nsim

t = Tower()
movelist = [[0,1], [1,0], [0,2], [2,0], [1,2], [2,1]]

for N in range(Nsim):
    
    t.reset()
    c = 0
    
    while(not t.isComplete()):

        #try moves in random order until the first successful one
        random.shuffle(movelist)
        for m in movelist:
            moved = t.move(m[0], m[1])
            if moved:
                break

        c += 1

    counts[N] = c  


print(sum(counts)/Nsim)
