
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

def proceed_cube(arena, position, n):
    for _ in range(n):
        position = step_cube(arena, position)
    return position

def step_cube(arena, position):
    if position[3] == 'N':
        if position[1] == 0:
            if position[0] == 0:
                candidate = [5, 49, position[2], 'N']
            elif position[0] == 1:
                candidate = [5, position[2], 0, 'E']
            elif position[0] == 2:
                candidate = [1, 49, position[2], 'N']
            elif position[0] == 3:
                candidate = [2, 49, position[2], 'N']
            elif position[0] == 4:
                candidate = [2, position[2], 0, 'E']
            elif position[0] == 5:
                candidate = [4, 49, position[2], 'N']
            else:
                raise Exception(f'Unexpected face: {position[0]}')
        else:
            candidate = [position[0], position[1] - 1, position[2], 'N']
    elif position[3] == 'E':
        if position[2] == 49:
            if position[0] == 0:
                candidate = [3, 49 - position[1], 49, 'W']
            elif position[0] == 1:
                candidate = [0, position[1], 0, 'E']
            elif position[0] == 2:
                candidate = [0, 49, position[1], 'N']
            elif position[0] == 3:
                candidate = [0, 49 - position[1], 49, 'W']
            elif position[0] == 4:
                candidate = [3, position[1], 0, 'E']
            elif position[0] == 5:
                candidate = [3, 49, position[1], 'N']
            else:
                raise Exception(f'Unexpected face: {position[0]}')
        else:
            candidate = [position[0], position[1], position[2] + 1, 'E']
    elif position[3] == 'S':
        if position[1] == 49:
            if position[0] == 0:
                candidate = [2, position[2], 49, 'W']
            elif position[0] == 1:
                candidate = [2, 0, position[2], 'S']
            elif position[0] == 2:
                candidate = [3, 0, position[2], 'S']
            elif position[0] == 3:
                candidate = [5, position[2], 49, 'W']
            elif position[0] == 4:
                candidate = [5, 0, position[2], 'S']
            elif position[0] == 5:
                candidate = [0, 0, position[2], 'S']
            else:
                raise Exception(f'Unexpected face: {position[0]}')
        else:
            candidate = [position[0], position[1] + 1, position[2], 'S']
    elif position[3] == 'W':
        if position[2] == 0:
            if position[0] == 0:
                candidate = [1, position[1], 49, 'W']
            elif position[0] == 1:
                candidate = [4, 49 - position[1], 0, 'E']
            elif position[0] == 2:
                candidate = [4, 0, position[1], 'S']
            elif position[0] == 3:
                candidate = [4, position[1], 49, 'W']
            elif position[0] == 4:
                candidate = [1, 49 - position[1], 0, 'E']
            elif position[0] == 5:
                candidate = [1, 0, position[1], 'S']
            else:
                raise Exception(f'Unexpected face: {position[0]}')
        else:
            candidate = [position[0], position[1], position[2] - 1, 'W']
    else:
        raise Exception(f'Unexpected direction: {position[3]}')
    
    if arena[candidate[0]][candidate[1]][candidate[2]] == 1:
        position = candidate
    
    return position


arena = [
    load_map('input_map_A.txt'),
    load_map('input_map_B.txt'),
    load_map('input_map_C.txt'),
    load_map('input_map_D.txt'),
    load_map('input_map_E.txt'),
    load_map('input_map_F.txt')
]
instructions = load_instructions('input_instructions.txt')
position = [1, 0, 0, 'E']

def pretty_print():
    for i, face in enumerate(arena):
        print(f'FACE {i}:')
        for j, line in enumerate(face):
            output = [decode[char] for char in line]
            if position[0] == i and position[1] == j:
                output[position[2]] = position[3]
            print("".join(output))

pretty_print()
print(instructions)
print(position)

for instruction in instructions:
    if instruction in ('L', 'R'):
        print(f'Turning {instruction} from {position[3]}', end="")
        position[3] = turn(position[3], instruction)
        print(f' to {position[3]}')
    else:
        n = int(instruction)
        print(f'Proceeding {n} spaces from {position[0], position[1], position[2], position[3]}', end="")
        position = proceed_cube(arena, position, n)
        print(f' to {position[0], position[1], position[2], position[3]}')
        #pretty_print(arena, position)


# face = 2, y = 44, h = 28, d = E
# 1000 * (44 + 50 + 1) + 4 * (28 + 50 + 1) + 0
# this will not make sense unless you are looking at the diagram of the net of the cube :^)
