
filename = 'input1.txt'

with open(filename, 'r') as file:
    input_ = [line for line in file.read().split('\n')]

# part one

tracker = [] # one per depth
output = [] # one per directory
total = 0
current_depth = -1

for line in input_:
    #print('processing:', line)
    if line == '$ cd ..':
        for i in range(current_depth + 1):
            tracker[i] += total
        #print('    exiting, final size = ', tracker[current_depth])
        output.append(tracker[current_depth])
        total = 0
        tracker[current_depth] = 0
        current_depth -= 1
        #print(f'        tracker: {tracker}')
    elif line.startswith('$ cd'):
        for i in range(current_depth + 1):
            tracker[i] += total
        current_depth += 1
        if current_depth >= len(tracker):
            tracker.append(0)
        total = 0
        #print('    entering, new current_depth =', current_depth)
    elif line == '$ ls':
        pass
    elif line.startswith('dir '):
        pass
    else:
        filesize = int(line.split(' ')[0])
        total += filesize
while current_depth >= 0:
    # record size on exiting so simulate "cd .." all the way up at the end
    for i in range(current_depth + 1):
        tracker[i] += total
    #print('    exiting, final size = ', tracker[current_depth])
    output.append(tracker[current_depth])
    total = 0
    tracker[current_depth] = 0
    current_depth -= 1

print(sum(x for x in output if x <= 100000))

# part two

space_required = max(x for x in output) - 40000000

print(min(x for x in output if x >= space_required))