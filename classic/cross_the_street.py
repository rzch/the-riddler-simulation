#The Riddler Classic 2018-04-20: Cross the Street
#Monte-Carlo simulation

import random

def walk_signal_available():
    #return True or False uniformly randomly
    return (random.random() < 0.5)

Nsim = 500000 #number of simulations

t_north = [0]*Nsim #walking time for walking north
t_east = [0]*Nsim #walking time for walking east

count = 0 #occurences of walking east beats walking north

T = 8 #period
W = 10 #time taken to walk one block

for N in range(Nsim):

    T20 = T*random.random() #waiting time at (2, 0)

    T01 = T*random.random() #waiting time at (0, 1)

    T10 = 2*T*random.random() #time in cycle for (1, 0) at initial time

    #walk north journey-------------------------------
    t_north[N] += W #from (2, 1) to (2, 0)
    
    if (walk_signal_available()): #walk signal is east at (2, 0) 
        t_north[N] += 0
    else:
        t_north[N] += T20
        
    t_north[N] += W #from (2, 0) to (1, 0)

    #time in cycle when north-walker arrives at (1, 0)
    T10_north = (t_north[N] + T10)%(2*T) 
    
    if (T10_north < T): #walk signal is east at (1, 0) 
        t_north[N] += 0
    else:
        t_north[N] += (2*T - T10_north) #wait remaining time in cycle

    t_north[N] += W #from (1, 0) to (0, 0)

    #walk east journey---------------------------------
    t_east[N] += 1 #wait 1 second for signal
    t_east[N] += W #from (2, 1) to (1, 1)    
    
    if (walk_signal_available()): #walk signal is north at (1, 1) 
        t_east[N] += W #from (1, 1) to (1, 0)

        #time in cycle when east-walker arrives at (1, 0)
        T10_east = (t_east[N] + T10)%(2*T)
        if (T10_east < T): #walk signal is east at (1, 0) 
            t_east[N] += 0
        else:
            t_east[N] += (2*T - T10_east) #wait remaining time in cycle

        t_east[N] += W #from (1, 0) to (0, 0)
        
    else: #walk signal is east at (1, 1)
        t_east[N] += W #from (1, 1) to (0, 1)
        
        if (walk_signal_available()): #walk signal is north at (0, 1) 
            t_east[N] += 0
        else:
            t_east[N] += T01

        t_east[N] += W #from (0, 1) to (0, 0)

    if (t_east[N] <= t_north[N]):
        count += 1

print('Proportion of times walking east beats walking north:')
print(count/Nsim)
print('Waiting time at lights for walking north:')
print(sum(t_north)/Nsim - 3*W)
print('Waiting time at lights for walking east:')
print(sum(t_east)/Nsim - 3*W)
