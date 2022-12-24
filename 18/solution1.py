

filename = 'input1.txt'
with open(filename) as file:
    data = [tuple(int(s) for s in line.split(',')) for line in file.read().split('\n')]

l = len(data)

xmin = min(line[0] for line in data)
xmax = max(line[0] for line in data)
ymin = min(line[1] for line in data)
ymax = max(line[1] for line in data)
zmin = min(line[2] for line in data)
zmax = max(line[2] for line in data)

# part one

x = 0
previous = None
for i, v in enumerate(sorted(data, key=lambda x: [x[1], x[2], x[0]])):
    if previous and v[1] == previous[1] and v[2] == previous[2] and v[0] - previous[0] in (-1, 1):
        x += 1
    previous = v

y = 0
previous = None
for i, v in enumerate(sorted(data, key=lambda x: [x[2], x[0], x[1]])):
    if previous and v[2] == previous[2] and v[0] == previous[0] and v[1] - previous[1] in (-1, 1):
        y += 1
    previous = v

z = 0
previous = None
for i, v in enumerate(sorted(data, key=lambda x: [x[0], x[1], x[2]])):
    if previous and v[0] == previous[0] and v[1] == previous[1] and v[2] - previous[2] in (-1, 1):
        z += 1
    previous = v

print(f'Final size: {6 * l - 2 * (x + y + z)}')

# part two

def get_adjacent_cubes(cube):
    output = []
    if cube[0] <= xmax: output.append((cube[0] + 1, cube[1], cube[2]))
    if cube[0] >= xmin: output.append((cube[0] - 1, cube[1], cube[2]))
    if cube[1] <= ymax: output.append((cube[0], cube[1] + 1, cube[2]))
    if cube[1] >= ymin: output.append((cube[0], cube[1] - 1, cube[2]))
    if cube[2] <= zmax: output.append((cube[0], cube[1], cube[2] + 1))
    if cube[2] >= zmin: output.append((cube[0], cube[1], cube[2] - 1))
    return output


flood = []
active = [(xmin - 1, ymin - 1, zmin - 1)]
surface = 0
while True:
    new = []
    for a in active:
        for c in get_adjacent_cubes(a):
            if c in data:
                surface += 1
            elif c not in flood and c not in active:
                new.append(c)
    flood.extend(active)
    active = list(set(new))
    if len(active) == 0:
        break
            
print(f'surface: {surface}')



