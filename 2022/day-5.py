"""Advent of Code 2022, Day 5"""

def clean_towers(stacks):
    towers = {}
    for i in range(1, 10):
        towers[i] = []

    for row in stacks:
        crates = []
        for char in range(1, 37, 4):
            crates += [row[char]]

        for col, box in enumerate(crates, 1):
            if box != ' ':
                towers[col] += [box]

    return towers

def parse_order(order):
    order = order.replace('move ', '').replace(' from ', ', ').replace(' to ', ', ')
    order = [int(num) for num in order.split(', ')]
    
    return order

def shift_crates(towers, order):
    move, start, end = order
    
    crates = sorted(towers[start][:move], reverse = True)
    del towers[start][:move]

    towers[end] = crates + towers[end]

    return towers

with open('day-5-input.txt') as file:
    lines = file.readlines()
    lines = [line.replace('\n', '') for line in lines]

towers = clean_towers(lines[:8])

for line in lines[10:]:
    order = parse_order(line)
    shift_crates(towers, order)

# part 1
# CNSFCGJSM incorrect
# LGWHLLRFN incorrect
message = ''
for index, column in enumerate(towers, 1):
    message += towers[index][0]

print(message)
