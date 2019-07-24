#The Riddler Express 2018-06-28: World Cup Double Take
#Monte-Carlo simulation

import random

Nsim = 200000 #number of simulations
count = 0

for n in range(Nsim):

    #index teams so that all teams in same group are within distance of 4
    allteams = [0]*32
    for i in range(8):
        allteams[(i*4):((i + 1)*4)] = list(range(i*10, i*10 + 4))

    #generate round of 16 teams by randomly picking 2 winners from each group
    ro16_teams = []
    for i in range(8):
        ro16_teams += [random.sample(allteams[(i*4):((i + 1)*4)], 2)]

    #generate quaterfinal teams using same order of play as the 2018 world cup:
    #https://en.wikipedia.org/wiki/2018_FIFA_World_Cup_knockout_stage
    qf_teams = []
    #top half    
    for i in range(4):
        qf_teams += [random.sample([ro16_teams[2*i][0], ro16_teams[2*i + 1][1]], 1)[0]]
    #bottom half
    for i in range(4):
        qf_teams += [random.sample([ro16_teams[2*i + 1][0], ro16_teams[2*i][1]], 1)[0]]

    #generate semifinal teams
    sf_teams = []
    for i in range(4):
        sf_teams += [random.sample(qf_teams[2*i:2*(i + 1)], 1)[0]]

    #generate grand final teams
    gf_teams = []
    for i in range(2):
        gf_teams += [random.sample(sf_teams[2*i:2*(i + 1)], 1)[0]]

    #generate third place playoff teams
    thirdplace_teams = list.copy(sf_teams)
    thirdplace_teams.remove(gf_teams[0])
    thirdplace_teams.remove(gf_teams[1])

    #determine whether grand final or third place playoff teams are from
    #the same group
    if (abs(gf_teams[0] - gf_teams[1]) < 4 or
        abs(thirdplace_teams[0] - thirdplace_teams[1]) < 4):
        count += 1

#compute empirical probability
print(count/Nsim)
