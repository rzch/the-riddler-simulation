#The Riddler Classic 2018-10-12: Tetrahedron in Sphere
#Monte-Carlo simulation

import math
import random

def inverse3by3(M):
    #explicit inverse of 3x3 matrix
    #see eg. https://ardoris.wordpress.com/2008/07/18/general-formula-for-the-inverse-of-a-3x3-matrix/

    [[a, b, c], [d, e, f], [g, h, i]] = M
    
    #determinant
    det = a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)

    #adjugate
    adj = [[e*i - f*h, c*h - b*i, b*f - c*e], \
           [f*g - d*i, a*i - c*g, c*d - a*f], \
           [d*h - e*g, b*g - a*h, a*e - b*d]]

    return [[m/det for m in row] for row in adj]

def point_in_tetrahedron(r, v1, v2, v3, v4):
    #determine if a point r in Euclidean coordinates lies in a tetrahedron
    #with vertices v1, v2, v3, v4 in Euclidean coordinates
    #
    #uses barycentric coordinates, see eg.
    #https://en.wikipedia.org/wiki/Barycentric_coordinate_system#Barycentric_coordinates_on_tetrahedra
    
    #assign Euclidean coordinates
    [x, y, z] = r
    [x1, y1, z1] = v1
    [x2, y2, z2] = v2
    [x3, y3, z3] = v3
    [x4, y4, z4] = v4

    T = [[x1 - x4, x2 - x4, x3 - x4], \
         [y1 - y4, y2 - y4, y3 - y4], \
         [z1 - z4, z2 - z4, z3 - z4]]

    invT = inverse3by3(T)

    #compute barycentric coordinates with matrix multipication and convex constraint
    lambdas = [0]*4
    for i in range(3):
        for j in range(3):
            lambdas[i] += invT[i][j]*(r[j] - v4[j])

    lambdas[3] = 1 - sum(lambdas[0:3])

    #point lies in tetrahedron if and only if all barycentric coordinates have the same sign
    if (math.copysign(1, lambdas[0]) == math.copysign(1, lambdas[1]) \
        == math.copysign(1, lambdas[2]) == math.copysign(1, lambdas[3])):
        return True
    else:
        return False
    
Nsim = 1000000 #number of simulations
count = 0

r = [0, 0, 0] #centre of unit sphere
for N in range(Nsim):
    #generate vertices of tetrahedron uniform with sphere picking
    #see eg. http://mathworld.wolfram.com/SpherePointPicking.html
    theta1 = 2*math.pi*random.random()
    phi1 = math.acos(2*random.random() - 1)
    v1 = [math.cos(theta1)*math.sin(phi1), math.sin(theta1)*math.sin(phi1), math.cos(phi1)]
    theta2 = 2*math.pi*random.random()
    phi2 = math.acos(2*random.random() - 1)
    v2 = [math.cos(theta2)*math.sin(phi2), math.sin(theta2)*math.sin(phi2), math.cos(phi2)]
    theta3 = 2*math.pi*random.random()
    phi3 = math.acos(2*random.random() - 1)
    v3 = [math.cos(theta3)*math.sin(phi3), math.sin(theta3)*math.sin(phi3), math.cos(phi3)]
    theta4 = 2*math.pi*random.random()
    phi4 = math.acos(2*random.random() - 1)
    v4 = [math.cos(theta4)*math.sin(phi4), math.sin(theta4)*math.sin(phi4), math.cos(phi4)]

    if (point_in_tetrahedron(r, v1, v2, v3, v4)):
        count += 1

print(count/Nsim)
