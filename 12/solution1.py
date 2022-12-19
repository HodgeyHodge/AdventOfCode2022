
def load_input(filename):
    with open(filename, 'r') as file:
        input_ = [line.replace('E', 'z').replace('S', 'a') for line in file.read().split('\n')]
        width = len(input_[0])
        height = len(input_)
    return input_, width, height

def climbable(terrain, old, new):
    return ord(terrain[new[0]][new[1]]) <= ord(terrain[old[0]][old[1]]) + 1

def get_adjacent(width, height, old):
    out = []
    if old[0] > 0:
        out.append((old[0] - 1, old[1]))
    if old[0] < height - 1:
        out.append((old[0] + 1, old[1]))
    if old[1] > 0:
        out.append((old[0], old[1] - 1))
    if old[1] < width - 1:
        out.append((old[0], old[1] + 1))
    return out

def flatten(l):
    return [item for sublist in l for item in sublist]

def part_one():
    def step(terrain, width, height, climbed_to):
        active = []
        new_paths = 0
        for current in climbed_to[-1]:
            for candidate in get_adjacent(width, height, current):
                if candidate not in flatten(climbed_to) and climbable(terrain, current, candidate):
                    active.append(candidate)
                    new_paths += 1
        climbed_to.append(list(set(active)))
        return new_paths

    terrain, width, height = load_input('input1.txt')
    start = (20, 0)
    end = (20, 154)
    #terrain, width, height = load_input('testinput1.txt')
    #start = (0, 0)
    #end = (2, 5)
    
    climbed_to = [[start]]
    new_paths = 1
    while new_paths > 0:
        new_paths = step(terrain, width, height, climbed_to)
    
    print([index for index,value in enumerate(climbed_to) if end in value])

def part_two():
    def step(terrain, width, height, descended_to):
        active = []
        new_paths = 0
        for current in descended_to[-1]:
            for candidate in get_adjacent(width, height, current):
                if candidate not in flatten(descended_to) and climbable(terrain, candidate, current): # reversed args!
                    active.append(candidate)
                    new_paths += 1
                    if terrain[candidate[0]][candidate[1]] == 'a':
                        print(f'hit rock bottom: {candidate}, {len(descended_to)}')
                        return 0
        descended_to.append(list(set(active)))
        return new_paths

    #terrain, width, height = load_input('testinput1.txt')
    #start = (2, 5)
    terrain, width, height = load_input('input1.txt')
    start = (20, 154)

    descended_to = [[start]]
    new_paths = 1
    while new_paths > 0:
        new_paths = step(terrain, width, height, descended_to)





part_one()
part_two()