
def load_data(filename):
    with open(filename) as file:
        lines = file.read().split('\n')
    n = set((i, j) for i, line in enumerate(lines) for j, char in enumerate(line) if char == '^')
    e = set((i, j) for i, line in enumerate(lines) for j, char in enumerate(line) if char == '>')
    s = set((i, j) for i, line in enumerate(lines) for j, char in enumerate(line) if char == 'v')
    w = set((i, j) for i, line in enumerate(lines) for j, char in enumerate(line) if char == '<')
    height = len(lines)
    width = len(lines[0])
    return n, e, s, w, height, width

def pretty_print(arena):
    for row in range(arena[4]):
        for col in range(arena[5]):
            if (row, col) in arena[0] | arena[1] | arena[2] | arena[3]:
                print('X', end="")
            else:
                print('.', end="")
        print("")
    print("")

def adjacent(arena, i, j):
    output = []
    if (i, j) not in arena[0] | arena[1] | arena[2] | arena[3]:
        output.append((i, j))
    if i > -1 and i < arena[4] and j < arena[5] - 1 and (i, j + 1) not in arena[0] | arena[1] | arena[2] | arena[3]:
        output.append((i, j + 1))
    if i > -1 and i < arena[4] and j > 0 and (i, j - 1) not in arena[0] | arena[1] | arena[2] | arena[3]:
        output.append((i, j - 1))
    if i < arena[4] - 1 and (i + 1, j) not in arena[0] | arena[1] | arena[2] | arena[3]:
        output.append((i + 1, j))
    if i > 0 and (i - 1, j) not in arena[0] | arena[1] | arena[2] | arena[3]:
        output.append((i - 1, j))
    return output

def iterate(arena):
    return (
        set((x[0] - 1 if x[0] > 0 else arena[4] - 1, x[1]) for x in arena[0]),
        set((x[0], x[1] + 1 if x[1] < arena[5] - 1 else 0) for x in arena[1]),
        set((x[0] + 1 if x[0] < arena[4] - 1 else 0, x[1]) for x in arena[2]),
        set((x[0], x[1] - 1 if x[1] > 0 else arena[5] - 1) for x in arena[3]),
        arena[4],
        arena[5]
    )


filename = 'input1.txt'

arena = load_data(filename)
heads = set([(-1, 0)])
t = 0
while True:
    t += 1
    arena = iterate(arena)
    heads = set([]).union(*[adjacent(arena, head[0], head[1]) for head in heads])
    if (arena[4] - 1, arena[5] - 1) in heads:
        print(f'Time to cross first time: {t + 1}')
        time_there = t + 1
        break

arena = load_data(filename) # though some will accuse me of being lazy and inefficient for iterating through again to get to the correct state, instead of reusing the arena variable above...
heads = set([(arena[4], arena[5] - 1)])
t = 0
while True:
    t += 1
    arena = iterate(arena)
    if t < time_there:
        continue
    heads = set([]).union(*[adjacent(arena, head[0], head[1]) for head in heads])
    if (0, 0) in heads:
        print(f'Time to cross back: {t + 1}')
        time_back = t + 1
        break

arena = load_data(filename)
heads = set([(-1, 0)])
t = 0
while True:
    t += 1
    arena = iterate(arena)
    if t < time_back:
        continue
    heads = set([]).union(*[adjacent(arena, head[0], head[1]) for head in heads])
    if (arena[4] - 1, arena[5] - 1) in heads:
        print(f'Time to cross again: {t + 1}')
        break


