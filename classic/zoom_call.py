# The Riddler Classic 2020-05-28: Zoom Call
# https://fivethirtyeight.com/features/can-you-join-the-worlds-biggest-zoom-call/
# Monte-Carlo simulation

import random

n = 10 #total number of people joining the call

Nsim = 100000 #number of simulations
count  = 0

for N in range(Nsim):

    join = [0]*n
    leave = [0]*n

    latest_join = 0
    earliest_leave = 1

    #generate meeting join and leave times
    for i in range(n):
        t1 = random.random()
        t2 = random.random()

        join[i] = min(t1, t2)
        leave[i] = max(t1, t2)

        latest_join = max(latest_join, join[i])
        earliest_leave = min(earliest_leave, leave[i])

    #check whether someone was with everybody else on the call
    for i in range(n):
        if (join[i] <= earliest_leave and leave[i] >= latest_join):
            count += 1
            break

print(count/Nsim)
