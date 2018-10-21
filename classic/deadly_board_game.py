#The Riddler 2016-10-14: Deadly Board Game

import random

n = 100 #board size (1000 not needed since probability converges to 2/7 very quickly)
board = [0]*n #initialise board

#initialise first six spaces
for i in range(0, 6):
  board[i] = 1/6

#compute probability that the token will land on a particular space using the recurrence relation 
for i in range(0, n):
  for j in range(i - 6, i):
    if j >= 0:
      board[i] += board[j]/6

print(board)

#=================================================
#Simulation
#N = 100000
N = 1
boardsim = [0]*n

for x in range(0, N):
  piece = 0
  while piece <= n:
    piece += random.randint(1, 6)
    if (piece > n):
      break
    else:
      boardsim[piece - 1] += 1

#print([i/N for i in boardsim])

#================================================
#Computing probability that the token will land on either of 3 spaces

#Formula for probability that token will land on two spaces
def AandB(a, b, board):
  return board[a - 1]*board[b - a - 1]
  
#Formula for probability that the token will land on either of 3 spaces
def AorBorC(a, b, c, board):
  return board[a - 1] + board[b - 1] + board[c - 1] - AandB(a, b, board) - AandB(a, c, board) - AandB(b, c, board) + board[a - 1]*board[b - a - 1]*board[c - b - 1]

#Verify value for win-maximising selection of coins
print(AorBorC(4, 5, 6, board))
