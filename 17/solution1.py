
SHAPES = [
    [[2, 0], [3, 0], [4, 0], [5, 0]],
    [[2, 1], [3, 0], [3, 1], [3, 2], [4, 1]],
    [[2, 0], [3, 0], [4, 0], [4, 1], [4, 2]],
    [[2, 0], [2, 1], [2, 2], [2, 3]],
    [[2, 0], [2, 1], [3, 0], [3, 1]]
]

def load_input(filename):
    with open(filename, 'r') as file:
        return file.read()

def current_height(arena):
    return max([-1] + [max([-1] + [i for i in a]) for a in arena])

def print_arena(arena):
    h = current_height(arena)
    for i in range(h, -1, -1):
        print(f'|{"".join(["#" if i in a else "." for a in arena])}|')
    print('+-------+')

def throw_shape(arena, shape, winds):
    h = current_height(arena)
    for tile in shape:
        tile[1] += h + 4

    landed = False
    ticks = 0
    while not landed:
        wind = winds[ticks % len(winds)]
        ticks += 1
        if wind == '>' and max([tile[0] for tile in shape]) < 6:
            new_shape = [[tile[0] + 1, tile[1]] for tile in shape]
            if not any(tile[1] in arena[tile[0]] for tile in new_shape):
                shape = new_shape
        elif wind == '<' and min([tile[0] for tile in shape]) > 0:
            new_shape = [[tile[0] - 1, tile[1]] for tile in shape]
            if not any(tile[1] in arena[tile[0]] for tile in new_shape):
                shape = new_shape
        new_shape = [[tile[0], tile[1] - 1] for tile in shape]
        if any(tile[1] in arena[tile[0]] for tile in new_shape) or min([tile[1] for tile in new_shape]) < 0:
            for tile in shape:
                arena[tile[0]].append(tile[1])
            landed = True  
        else:
            shape = new_shape
    return ticks

def part_one(filename):
    winds = load_input(filename)
    arena = [[], [], [], [], [], [], []]
    L = len(winds)
    wind_offset = 0
    for i in range(0, 2022):
        wind_offset = (wind_offset + throw_shape(arena, [s[:] for s in SHAPES[i % 5]], winds[wind_offset:] + winds[:wind_offset])) % L
    print(f'Final height: {current_height(arena) + 1}') # answer as posed will have fudge factor, height vs highest index

def part_two(filename):
    winds = load_input(filename)
    arena = [[], [], [], [], [], [], []]
    wind_offset = 0
    L = len(winds)
    tracker = {}
    for i in range(9999):
        wind_offset = (wind_offset + throw_shape(arena, [s[:] for s in SHAPES[i % 5]], winds[wind_offset:] + winds[:wind_offset])) % L
        print(f'i = {i}, h = {current_height(arena)}')
        if (i % 5, wind_offset) not in tracker:
            tracker[(i % 5, wind_offset)] = i
        else:
            print(f'Found a repeat: {(i % 5, wind_offset)}: {tracker[(i % 5, wind_offset)]} / {i}') # beware false positives if you stop at the first match!

# part one

part_one('testinput1.txt')
part_one('input1.txt')

# part two

part_two('testinput1.txt') # (4, 2): 14 / 49

# repeats every 35 blocks starting at i = 14, h = 24, going to i = 49, h = 77
# grows by 53 each time
# so 1000000000000 // 35 = 28571428571
# then 14 + 28571428571 * 35 = 999999999999
# and 24 + 28571428571 * 53 = 1514285714287
# but have to add the final 1000000000000 - 999999999999 = 1; can see from the records that this grows as i = 14 to 14 + 1; which is 24 to 25, ie 1
# so final answer is 1514285714287 + 1 = 1514285714288

part_two('input1.txt') # (4, 1809): 304 / 2009

# repeats every 1705 blocks starting at i = 304, h = 464 going to i = 2009, h = 3046
# grows by 2582 each time
# so 1000000000000 // 1705 = 586510263
# then 304 + 586510263 * 1705 = 999999998719
# and 464 + 586510263 * 2582 = 1514369499530
# but have to add the final 1000000000000 - 999999998719 = 1281; can see from the records that this grows as i = 304 to 304 + 1281; which is 464 to 2418, ie 1954
# so final answer is 1514369499530 + 1954 = 1514369501484




