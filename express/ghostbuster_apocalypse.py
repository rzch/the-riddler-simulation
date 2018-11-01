#The Riddler Express 2017-09-15: Ghostbuster Apocalypse
#Monte-Carlo simulation (naive)

import random
import math

def intersect_inside_unit_circle(x1, y1, x2, y2, w1, z1, w2, z2):

    #slopes
    mAC = (y2 - y1)/(x2 - x1)
    mBD = (z2 - z1)/(w2 - w1)

    #case of parallel lines
    if (mAC == mBD):
        return False

    #determine intersection
    x = (mAC*x1 - y1 - mBD*w1 + z1)/(mAC - mBD)
    y = mAC*(x - x1) + y1

    #determine inside unit circle
    if (x**2 + y**2 < 1):
        return True
    else:
        return False

Nsim = 10000 #Number of simulations
count = 0

n = 20; #people in circle

dtheta = 2*math.pi/n #angle (rad) between each person

#positions in circle, slight offset to avoid vertical lines
angles = [dtheta*i + dtheta/(n + 1) for i in range(n)]

for N in range(Nsim):
    #random placement in circle
    random.shuffle(angles)

    #assign places
    A = angles[0]
    B = angles[1]
    C = angles[2]
    D = angles[3]

    #cartesian coordinates of each place
    x1 = math.cos(A)
    y1 = math.sin(A)

    x2 = math.cos(C)
    y2 = math.sin(C)

    w1 = math.cos(B)
    z1 = math.sin(B)

    w2 = math.cos(D)
    z2 = math.sin(D)

    if (intersect_inside_unit_circle(x1, y1, x2, y2, w1, z1, w2, z2)):
        count += 1

print(count/Nsim)
    
