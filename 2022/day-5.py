"""Advent of Code 2022, Day 5"""

def clean_towers(stacks):
    # determine how many stacks there are
    lastrow = stacks.pop()
    positions = []
    for char in range(0, len(lastrow)):
        if lastrow[char] != ' ': positions += [int(char)]

    towers = {}
    for position in positions:
        towers[int(lastrow[position])] = []

    for row in stacks:
        crates = []
        for position in positions:
            crates += [row[position]]

        for col, box in enumerate(crates, 1):
            if box != ' ':
                towers[col] += [box]

    return towers

def parse_order(order):
    order = order.replace('move ', '').replace(' from ', ', ').replace(' to ', ', ')
    order = [int(num) for num in order.split(', ')]
    
    return order

def shift_crates(towers, order, part1 = True):
    move, start, end = order
    
    if part1:
        crates = list(reversed(towers[start][:move]))
    else:
        crates = towers[start][:move]

    del towers[start][:move]

    towers[end] = crates + towers[end]

    return towers

with open('day-5-input.txt') as file:
    lines = file.readlines()
    lines = [line.replace('\n', '') for line in lines]

# part 1
towers = clean_towers(lines[:9])

for line in lines[10:]:
    order = parse_order(line)
    shift_crates(towers, order)

message = ''
for index, column in enumerate(towers, 1):
    message += towers[index][0]

print(message)

# part 2
towers = clean_towers(lines[:9])

for line in lines[10:]:
    order = parse_order(line)
    shift_crates(towers, order, part1 = False)

message = ''
for index, column in enumerate(towers, 1):
    message += towers[index][0]

print(message)