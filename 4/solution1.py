
filename = 'input1.txt'

with open(filename, 'r') as file:
    input_ = [[int(y) for x in line.split(',') for y in x.split('-')] for line in file.read().split('\n')]

print(input_)

# part one

envelopments = sum((x[0] <= x[2] and x[1] >= x[3]) or (x[2] <= x[0] and x[3] >= x[1]) for x in input_)

print(envelopments)

# part two

overlaps = sum(
    not (x[1] < x[2]) and not (x[0] > x[3]) for x in input_
)

print(overlaps)

