"""Advent of Code 2022, Day 6"""

def tune(signal):
    track = []
    counter = 0
    for char in signal:
        counter += 1
        track += [char]
        if counter >= 4 and sorted(track) == sorted(list(set(track))):
            break

        if len(track) == 4:
            track.pop(0)
    
    return counter

with open('day-6-input.txt') as file:
    d6input = file.readline()

tune(d6input)
