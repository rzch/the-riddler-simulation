import random

Nsim = 1000000; #number of simulations
count = 0

for x in range(0, Nsim):

    #generate points randomly in each quadrant
    x1 = random.random()
    y1 = random.random()

    x2 = -random.random()
    y2 = random.random()

    x3 = -random.random()
    y3 = -random.random()

    x4 = random.random()
    y4 = -random.random()

    #vector from quadrant 4 point to quadrant 2 point
    bx = x2 - x4
    by = y2 - y4

    #vector from quadrant 4 point to quadrant 1 point
    ax = x1 - x4
    ay = y1 - y4

    #if the cross product axb is negative, then the quadrilateral is not convex
    #(using the right hand rule)
    if (ax*by - ay*bx < 0):
        count += 1

#more than one angle cannot be 'inward', so use mutual exclusivity and symmetry
print(1 - 4*count/Nsim)
