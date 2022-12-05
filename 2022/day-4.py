"""Advent of Code 2022, Day 4"""

def clean_assignments(pair):
    sections = pair.split(',')
    elfA, elfB = [section.split('-') for section in sections]
    elfA = [int(end) for end in elfA]
    elfB = [int(end) for end in elfB]

    return [elfA, elfB]

def interval_contained(pair):
    elfA, elfB = pair

    intervalA = range(elfA[0], elfA[1] + 1)
    intervalB = range(elfB[0], elfB[1] + 1)
    
    # an elf might only be assigned 1 section
    if elfA[0] == elfA[1]:
        return elfA[0] in intervalB
    if elfB[0] == elfB[1]:
        return elfB[0] in intervalA
    
    # otherwise, we check for nesting
    AinB = elfA[0] in intervalB and elfA[1] in intervalB
    BinA = elfB[0] in intervalA and elfB[1] in intervalA

    return AinB or BinA

with open('day-4-input.txt') as file:
    lines = file.readlines()
    lines = [line.replace('\n', '') for line in lines]

total = []
for line in lines:
    pair = clean_assignments(line)
    total += [interval_contained(pair)]

sum(total)
