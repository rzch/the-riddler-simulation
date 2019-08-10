#The Riddler Expresss 2018-09-07: Riddler Lifeline
#Monte-Carlo simulation of optimal strategy

import random

Nsim = 5000000 #Number of simulations
winnings = [0]*Nsim

#multiple-choice options
choices = ['A', 'B', 'C', 'D']

for n in range(Nsim):

    #determine the correct answer randomly
    correct_answer = random.choice(choices)

    #group the other incorrect answers
    incorrect_answers = list.copy(choices)
    incorrect_answers.remove(correct_answer)

    #generate the 50-50 choices
    fiftyfifty = [correct_answer, random.choice(incorrect_answers)]
    random.shuffle(fiftyfifty)

    #generate the ask-audience responses
    r = random.random()
    audience_guess = list.copy(incorrect_answers)
    random.shuffle(audience_guess)
    if (r < 0.5):
        audience_guess.insert(0, correct_answer)
    elif (r < 0.8):
        audience_guess.insert(1, correct_answer)
    elif (r < 0.95):
        audience_guess.insert(2, correct_answer)
    else:
        audience_guess.insert(3, correct_answer)

    #find the audience rankings of the 50-50 options
    ind1 = audience_guess.index(fiftyfifty[0])
    ind2 = audience_guess.index(fiftyfifty[1])

    #pick the one that was most preferred by the audience
    if (ind1 < ind2):
        pick = fiftyfifty[0]
    else:
        pick = fiftyfifty[1]

    #check if pick was correct
    if (pick == correct_answer):
        prize = 500000
    else:
        prize = 10000

    winnings[n] = prize

#compute average winnings
print(sum(winnings)/Nsim)
