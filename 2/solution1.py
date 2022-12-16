
filename = 'input1.txt'

def decoder_l(move):
    pad = {'A': 'R', 'B': 'P', 'C': 'S'}
    return pad[move]

scoring = {
    ('R', 'R'): 1 + 3,
    ('R', 'P'): 2 + 6,
    ('R', 'S'): 3 + 0,
    ('P', 'R'): 1 + 0,
    ('P', 'P'): 2 + 3,
    ('P', 'S'): 3 + 6,
    ('S', 'R'): 1 + 6,
    ('S', 'P'): 2 + 0,
    ('S', 'S'): 3 + 3
}

with open(filename, 'r') as file:
    input_ = [(decoder_l(line[0]), line[2]) for line in file.read().split('\n')]

# part one

def naive_decoder_r(move):
    pad = {'X': 'R', 'Y': 'P', 'Z': 'S'}
    return pad[move]

print(sum([scoring[(ply[0], naive_decoder_r(ply[1]))] for ply in input_]))

# part two

scoring = {
    ('R', 'Y'): 1 + 3,
    ('R', 'Z'): 2 + 6,
    ('R', 'X'): 3 + 0,
    ('P', 'X'): 1 + 0,
    ('P', 'Y'): 2 + 3,
    ('P', 'Z'): 3 + 6,
    ('S', 'Z'): 1 + 6,
    ('S', 'X'): 2 + 0,
    ('S', 'Y'): 3 + 3
}

print(sum([scoring[(ply[0], ply[1])] for ply in input_]))