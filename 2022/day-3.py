"""Advent of Code 2022, Day 3"""

import string

priority = {}
for index, letter in enumerate(string.ascii_letters):
    priority[letter] = 1 + index

def split_rucksack(rucksack):
    midpt = len(rucksack) // 2
    compA = rucksack[:midpt]
    compB = rucksack[-midpt:]

    return [compA, compB]

def intersect_items(compartments):
    return list(set(compartments[0]).intersection(set(compartments[1])))[0]

with open('day-3.txt') as file:
    lines = file.readlines()
    lines = [line.replace('\n', '') for line in lines]

total = []
for line in lines:
    comp = split_rucksack(line)
    item = intersect_items(comp)
    total += [priority[item]]

sum(total)

