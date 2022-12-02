with open('day-1-input.txt') as file:
    lines = file.readlines()

cal = []
elf = []
for line in lines:
    if line != '\n':
        elf += [int(line)]
    else:
        cal += [sum(elf)]
        elf = []

# part 1
max(cal)

# part 2
cal = sorted(cal, reverse = True)
sum(cal[0:3])
