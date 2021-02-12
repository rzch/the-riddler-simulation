import random

N = 20 #number of pairs

def prob_sock(n):
    #computes the probability of drawing a matching pair after the nth sock
    p = 1

    for i in range(1, n - 1):
        p *= (2*N - 2*i)/(2*N - i)

    p *= (n - 1)/(2*N - n + 1)

    return p

#compute expected number of draws
a = 0
for n in range(1, N + 2):
    a += n*prob_sock(n)

print("Analytical Probability:")
print(a)

#generate the pairs of socks
socks = [i//2 + 1 for i in range(2*N)]

Nsim = 1000000 #number of simulations
draws = [0]*Nsim

for j in range(Nsim):
    drawn = []
    drawer = socks.copy()

    drawn_pair = False
    while(drawn_pair == False): #keep drawing until pair found

        #remove a random sock from the drawer
        sock = random.choice(drawer)
        drawer.remove(sock)

        if (any([sock == d for d in drawn])): #check if pair found
            drawn.append(sock)
            draws[j] = len(drawn)
            break
        else:
            drawn.append(sock)

print("Monte-Carlo Probability:")
print(sum(draws)/Nsim)
