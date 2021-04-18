# The Riddler Classic 2020-10-02: Eat the Chocolates
# https://fivethirtyeight.com/features/can-you-eat-all-the-chocolates/
# Monte-Carlo simulation and recursive computation

import random

Nsim = 1000000; #number of simulation replications
count = 0;

m = 2; #number of starting milk chocolates
d = 8; #number of starting dark chocolates

for N in range(Nsim):
    #True for milk
    bag = [True]*m + [False]*d

    last = -1
    while(len(bag) > 0):
        #pick a chocolate
        chocolate = random.choice(bag)

        #check whether to eat
        if (last == -1 or chocolate == last):
            bag.remove(chocolate)
            last = chocolate
        else:
            last = -1

    if (last == True):
        count += 1
        
print("Monte-Carlo simulation:")
print(count/Nsim)

#------------------------------------------------------
#https://stackoverflow.com/questions/1988804/what-is-memoization-and-how-can-i-use-it-in-python
class Memoize:
    def __init__(self, f):
        self.f = f
        self.memo = {}
    def __call__(self, *args):
        if not args in self.memo:
            self.memo[args] = self.f(*args)
        #Warning: You may wish to do a deepcopy here if returning objects
        return self.memo[args]
    
@Memoize #decotrator
def pr_last_choc_milk(m, d, last):

    if (m == 0):
        return 0
    elif (d == 0):
        return 1
    elif (last == "none"):
        return pr_last_choc_milk(m-1, d, "milk")*m/(m + d) \
               + pr_last_choc_milk(m, d-1, "dark")*d/(m + d)
    elif (last == "milk"):
        return pr_last_choc_milk(m-1, d, "milk")*m/(m + d) \
               + pr_last_choc_milk(m, d, "none")*d/(m + d)
    elif (last == "dark"):
        return pr_last_choc_milk(m, d, "none")*m/(m + d) \
               + pr_last_choc_milk(m, d-1, "dark")*d/(m + d)

print("Recursive computation:")
print(pr_last_choc_milk(2, 8, "none"))
