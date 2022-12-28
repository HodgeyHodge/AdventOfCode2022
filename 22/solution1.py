
encode = {
    ' ': 0,
    '.': 1,
    '#': 2
}
decode = {
    0: ' ',
    1: '.',
    2: '#'
}

def load_map(filename):
    with open(filename) as file:
        return [[encode[x] for x in line] for line in file.read().split('\n')]

def load_instructions(filename):
    with open(filename) as file:
        return [line for line in file.read().replace('R', ',R,').replace('L', ',L,').split(',')]

def pretty_print(arena, position):
    for i, line in enumerate(arena):
        output = [decode[char] for char in line]
        if i == position[0]:
            output[position[1]] = position[2]
        print("".join(output))

def turn(cardinal, hand):
    if hand == 'R':
        if cardinal == 'N': return 'E'
        if cardinal == 'E': return 'S'
        if cardinal == 'S': return 'W'
        if cardinal == 'W': return 'N'
    if hand == 'L':
        if cardinal == 'N': return 'W'
        if cardinal == 'E': return 'N'
        if cardinal == 'S': return 'E'
        if cardinal == 'W': return 'S'
    raise Exception('lmao')

def proceed_flat(arena, position, n):
    for _ in range(n):
        position = step_flat(arena, position)
    return position

def step_flat(arena, position):
    if position[2] == 'E':
        if position[1] == len(arena[position[0]]) - 1 or arena[position[0]][position[1] + 1] == 0:
            candidate = [position[0], min([i for i, v in enumerate(arena[position[0]]) if v != 0]), 'E']
        else:
            candidate = [position[0], position[1] + 1, 'E']
    elif position[2] == 'W':
        if position[1] == 0 or arena[position[0]][position[1] - 1] == 0:
            candidate = [position[0], max([i for i, v in enumerate(arena[position[0]]) if v != 0]), 'W']
        else:
            candidate = [position[0], position[1] - 1, 'W']
    elif position[2] == 'S':
        if position[0] == len(arena) - 1 or len(arena[position[0] + 1]) <= position[1] or arena[position[0] + 1][position[1]] == 0:
            candidate = [min([i for i, v in enumerate(arena) if len(v) > position[1] and v[position[1]] != 0]), position[1], 'S']
        else:
            candidate = [position[0] + 1, position[1], 'S']
    elif position[2] == 'N':
        if position[0] == 0 or arena[position[0] - 1][position[1]] == 0:
            candidate = [max([i for i, v in enumerate(arena) if len(v) > position[1] and v[position[1]] != 0]), position[1], 'N']
        else:
            candidate = [position[0] - 1, position[1], 'N']
    if arena[candidate[0]][candidate[1]] == 1:
        position = candidate
    return position
        

arena = load_map('input_map.txt')
instructions = load_instructions('input_instructions.txt')
position = [0, min([i for i, v in enumerate(arena[0]) if v == 1]), 'E']
#pretty_print(arena, position)
#print(instructions)
#print(position)

for instruction in instructions:
    if instruction in ('L', 'R'):
        #print(f'Turning {instruction} from {position[2]}', end="")
        position[2] = turn(position[2], instruction)
        #print(f' to {position[2]}')
    else:
        n = int(instruction)
        print(f'Proceeding {n} spaces from {position[0], position[1]}', end="")
        position = proceed_flat(arena, position, n)
        print(f' to {position[0], position[1]}')
        #pretty_print(arena, position)

print(f'Answer to part one as posed: {1000 * (position[0] + 1) + 4 * (position[1] + 1) + 2}')