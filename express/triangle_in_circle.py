#The Riddler Express 2018-01-12: Triangle in Circle
#Monte-Carlo simulation

import random
import math

def point_in_triangle(r, v1, v2, v3):
    #Takes a point r and checks whether it is inside the triangle of
    #vertices v1, v2, v3 in cartesian coordinates.
    #Uses barycentric coordinates, see eg. https://en.wikipedia.org/wiki/Barycentric_coordinate_system#Conversion_between_barycentric_and_Cartesian_coordinates

    #get cartesian coordinates
    x = r[0]
    y = r[1]
    x1 = v1[0]
    y1 = v1[1]
    x2 = v2[0]
    y2 = v2[1]
    x3 = v3[0]
    y3 = v3[1]

    #compute barycentric coordinates
    lambda1 = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3))/((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
    lambda2 = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3))/((y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3))
    lambda3 = 1 - lambda1 - lambda2

    #point is inside triangle if and only if all signs are the same
    if (math.copysign(1, lambda1) == math.copysign(1, lambda2) == math.copysign(1, lambda3)):
        return True
    else:
        return False
    

Nsim = 1000000 #number of simulations
count = 0

r = [0, 0] #centre of unit circle
for N in range(Nsim):
    #generate vertices uniformly on unit circle
    theta1 = 2*math.pi*random.random()
    v1 = [math.cos(theta1), math.sin(theta1)]
    theta2 = 2*math.pi*random.random()
    v2 = [math.cos(theta2), math.sin(theta2)]
    theta3 = 2*math.pi*random.random()
    v3 = [math.cos(theta3), math.sin(theta3)]

    if point_in_triangle(r, v1, v2, v3):
        count += 1


print(count/Nsim)
