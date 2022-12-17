from copy import deepcopy

def get_instructions(filename):
    with open(filename, 'r') as file:
        return [[int(y[1]), int(y[3]) - 1, int(y[5]) - 1] for y in [[x for x in line.split(' ')] for line in file.read().split('\n')]]

test_instructions = get_instructions('testinput1.txt')
live_instructions = get_instructions('input1.txt')

test_stacks = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P']
]

live_stacks = [
    ['G', 'F', 'V', 'H', 'P', 'S'],
    ['G', 'J', 'F', 'B', 'V', 'D', 'Z', 'M'],
    ['G', 'M', 'L', 'J', 'N'],
    ['N', 'G', 'Z', 'V', 'D', 'W', 'P'],
    ['V', 'R', 'C', 'B'],
    ['V', 'R', 'S', 'M', 'P', 'W', 'L', 'Z'],
    ['T', 'H', 'P'],
    ['Q', 'R', 'S', 'N', 'C', 'H', 'Z', 'V'],
    ['F', 'L', 'G', 'P', 'V', 'Q', 'J']
]

# part one

def rearrange_9000(stacks, instructions):
    for instruction in instructions:
        for _ in range(instruction[0]):
            stacks[instruction[2]].append(stacks[instruction[1]].pop(-1))

S = deepcopy(test_stacks)
rearrange_9000(S, test_instructions)
print(''.join(x[-1] for x in S))

S = deepcopy(live_stacks)
rearrange_9000(S, live_instructions)
print(''.join(x[-1] for x in S))

# part two

def rearrange_9001(stacks, instructions):
    for instruction in instructions:
        x, y = stacks[instruction[1]][:-instruction[0]], stacks[instruction[1]][-instruction[0]:]
        stacks[instruction[1]] = x
        stacks[instruction[2]].extend(y)

S = deepcopy(test_stacks)
rearrange_9001(S, test_instructions)
print(''.join(x[-1] for x in S))

S = deepcopy(live_stacks)
rearrange_9001(S, live_instructions)
print(''.join(x[-1] for x in S))

