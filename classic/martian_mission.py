#The Riddler Classic 2019-01-11: Martian Mission
#https://fivethirtyeight.com/features/in-space-no-one-can-hear-your-3d-printer-die/
#Monte-Carlo simulation

import random

Nsim = 10000 #number of simulations

count = 0 #count number of times died

#number of days to spend on Mars
ndays = 1825
#probabilities of each printer breaking
probs = [0.1, 0.075, 0.05]
#number of printers
n_printers = len(probs)

for N in range(Nsim):

    #initialise all printers not broken
    printer_state = [True for j in range(n_printers)]
    
    for i in range(ndays):

        #determine whether a printer breaks
        broken = [random.random() < probs[j] for j in range(n_printers)]

        #update state of each printer
        printer_state = [printer_state[j] and not broken[j] for j in range(n_printers)]
        
        if (sum(printer_state) == 0): #check if all printers broken
            count += 1
            break
        else: #fix all printers
            printer_state = [True for j in range(n_printers)]

#print probability of survival
print(1 - count/Nsim)
        
