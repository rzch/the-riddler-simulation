# The Riddler Classic 2018-12-21: Santa's Playlist
# https://fivethirtyeight.com/features/santa-needs-some-help-with-math/

import random

m = 100 #number of songs to play
n = 7175 #length of playlist

Nsim = 100000 #number of simulation replications
count = 0

for N in range(Nsim):

    #generate random songs to play
    songs = [random.randint(1, n) for i in range(m)]

    #get all unique songs
    unique_songs = set(songs)

    #check if all songs are unique
    if len(unique_songs) == m:
        count += 1

print(count/Nsim)
