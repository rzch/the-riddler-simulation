# The Riddler Express 2019-04-26: Thanos Snaps
# https://fivethirtyeight.com/features/how-many-earthlings-would-survive-63-thanos-snaps/
# Monte-Carlo simulation

from random import getrandbits
import numpy as np

Nsim = 1000000 #number of simulation replications

#number of starting thanos
T0 = 63 

#number of starting population
pop0 = 7500000000

E = [0]*Nsim

#%%

def halve_population(pop):
    
    #randomly halve the population
    
    #maximum amount to halve at a time
    M = 1250000000
    
    div = pop//M
    rem = pop%M
    
    pops = [M for i in range(div)]
    pops.append(rem)
    
    halfpops = [np.random.binomial(pops[i], p=0.5) for i in range(len(pops))]
    
    return sum(halfpops)
    
#%%
    
for N in range(Nsim):
    
    T = T0
    pop = pop0

    while (T > 0):
        #Thanos snaps
        T -= 1
        
        #halve remaining Thanos
        T = sum([not getrandbits(1) for i in range(T)])
        #halve remaining population
        pop = halve_population(pop)
        
    E[N] = pop
    
#compute mean
print(sum(E)/Nsim)