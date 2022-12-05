"""Advent of Code 2022, Day 4"""

def clean_assignments(pair):
    sections = pair.split(',')
    elfA, elfB = [section.split('-') for section in sections]
    elfA = [int(end) for end in elfA]
    elfB = [int(end) for end in elfB]

    return [elfA, elfB]

def check_overlaps(pair, check_contained = True):
    elfA, elfB = pair

    intervalA = range(elfA[0], elfA[1] + 1)
    intervalB = range(elfB[0], elfB[1] + 1)
    
    # an elf might only be assigned 1 section
    if elfA[0] == elfA[1]:
        return elfA[0] in intervalB
    if elfB[0] == elfB[1]:
        return elfB[0] in intervalA
    
    # otherwise, check the end points
    checkA = sum([point in intervalB for point in elfA])
    checkB = sum([point in intervalA for point in elfB])

    if check_contained:
        return 2 in [checkA, checkB]
    else:
        return 1 in [checkA, checkB] or 2 in [checkA, checkB]

with open('day-4-input.txt') as file:
    lines = file.readlines()
    lines = [line.replace('\n', '') for line in lines]

contained = []
overlaps = []
for line in lines:
    pair = clean_assignments(line)
    contained += [check_overlaps(pair)]
    overlaps += [check_overlaps(pair, check_contained = False)]

sum(contained) # 431
sum(overlaps) # 823
