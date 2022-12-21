def pretty_print(arena):
    for j in range(len(arena[0])):
        for i in range(len(arena)):
            print({0: '.', 1: '#', 2: 'O'}[arena[i][j]], end='')
        print('')

def drop_sand(arena, col, row):
    if row == len(arena[0]) - 1:
        return False
    while True:
        landing = next((i for i, x in enumerate(arena[col]) if x != 0 and i >= row), None)
        if landing:
            if landing == 0:
                return False
            if col == 0:
                return False
            elif arena[col - 1][landing] == 0:
                return drop_sand(arena, col - 1, landing)
            elif col == len(arena) - 1:
                return False
            elif arena[col + 1][landing] == 0:
                return drop_sand(arena, col + 1, landing)
            else:
                arena[col][landing - 1] = 2
                return True
        else:
            return False

def fill_arena(blocks, height, width, border):
    horizontal_blocks = []
    vertical_blocks = []
    for line in blocks:
        for i in range(len(line) - 1):
            if line[i][0] == line[i + 1][0]:
                vertical_blocks.append((line[i][0], min(line[i][1], line[i + 1][1]), max(line[i][1], line[i + 1][1])))
            else:
                horizontal_blocks.append((min(line[i][0], line[i + 1][0]), max(line[i][0], line[i + 1][0]), line[i][1]))
    
    #magic numbers come from here:

    #print(min([h[0] for h in horizontal_blocks]))
    #print(max([h[1] for h in horizontal_blocks]))
    #print(min([h[2] for h in horizontal_blocks]))
    #print(max([h[2] for h in horizontal_blocks]))
    
    #print(min([v[0] for v in vertical_blocks]))
    #print(max([v[0] for v in vertical_blocks]))
    #print(min([v[1] for v in vertical_blocks]))
    #print(max([v[2] for v in vertical_blocks]))
    
    arena = [[0] * height for _ in range(width)] # one list per column, pointing downwards
    
    for h in horizontal_blocks:
       for i in range(h[0], h[1] + 1):
           arena[i][h[2]] = 1
    
    for v in vertical_blocks:
        for i in range(v[1], v[2] + 1):
            arena[v[0]][i] = 1
    
    if border: # to simulate the question as posed, put in walls, and then at the end, add the missing slopes back in
        for i in range(height):
            arena[0][i] = 1
            arena[width - 1][i] = 1
        for i in range(width):
            arena[i][height - 1] = 1

    return arena

def part_one(filename, height, width, offset):
    with open(filename, 'r') as file:
        input_ = [[tuple([int(coord.split(',')[0]) - offset, int(coord.split(',')[1])]) for coord in line.split(' -> ')] for line in file.read().split('\n')]
    
    arena = fill_arena(input_, height, width, False)
    
    print('start:')
    pretty_print(arena)
    
    while True:
        landed = drop_sand(arena, 500 - offset, 0)
        if not landed:
            break
    
    print('end:')
    pretty_print(arena)
    
    print(f'Total sand: {sum(sum([1 for x in y if x == 2]) for y in arena)}')

def part_two(filename, height, width, offset):
    with open(filename, 'r') as file:
        input_ = [[tuple([int(coord.split(',')[0]) - offset, int(coord.split(',')[1])]) for coord in line.split(' -> ')] for line in file.read().split('\n')]
    
    arena = fill_arena(input_, height, width, True)
    
    print('start:')
    pretty_print(arena)
    
    while True:
        landed = drop_sand(arena, 500 - offset, 0)
        if not landed:
            break
    
    print('end:')
    pretty_print(arena)
    
    print(f'Total in-bounds sand: {sum(sum([1 for x in y if x == 2]) for y in arena)}') # final answer is this plus the "triangle" on each side


# part two

part_one('testinput1.txt', 10, 10, 494)
part_one('input1.txt', 165, 62, 483)

# part two

part_two('testinput1.txt', 12, 14, 492)
part_two('input1.txt', 167, 66, 481)


