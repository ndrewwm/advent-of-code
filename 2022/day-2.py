"""Advent of Code 2022, Day 2"""

def clean_rps(round):
    round = round.replace('\n', '')
    round = round.replace('A', 'rock').replace('B', 'paper').replace('C', 'scissors')

    return round.split()

def judge_rps(opp, you):
    if opp == you:
        return 3
    if [opp, you] in [['rock', 'scissors'], ['paper', 'rock'], ['scissors', 'paper']]:
        return 0
    else:
        return 6

def shape_val(you):
    match you:
        case 'rock': return 1
        case 'paper': return 2
        case 'scissors': return 3

def score_rps_p1(round):
    opp, you = round
    you = you.replace('X', 'rock').replace('Y', 'paper').replace('Z', 'scissors')

    return judge_rps(opp, you) + shape_val(you)

def score_rps_p2(round):
    opp, you = round
    
    you = you.replace('Y', opp)
    if you == 'X':
        if opp == 'rock': you = 'scissors'
        if opp == 'paper': you = 'rock'
        if opp == 'scissors': you = 'paper'
    if you == 'Z':
        if opp == 'rock': you = 'paper'
        if opp == 'paper': you = 'scissors'
        if opp == 'scissors': you = 'rock'
    
    return judge_rps(opp, you) + shape_val(you)

with open('day-2-input.txt') as file:
    lines = file.readlines()
    lines_clean = [clean_rps(line) for line in lines]

points_p1 = []
points_p2 = []
for line in lines_clean:
    points_p1 += [score_rps_p1(line)]
    points_p2 += [score_rps_p2(line)]

score_1 = sum(points_p1)
score_2 = sum(points_p2)
