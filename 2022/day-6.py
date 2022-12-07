"""Advent of Code 2022, Day 6"""

def tune(signal, nchar = 4):
    track = []
    counter = 0
    for char in signal:
        counter += 1
        track += [char]
        if counter >= nchar and sorted(track) == sorted(list(set(track))):
            break

        if len(track) == nchar:
            track.pop(0)
    
    return counter

with open('day-6-input.txt') as file:
    d6input = file.readline()

# part 1
tune(d6input, 4)

# part 2
tune(d6input, 14)
