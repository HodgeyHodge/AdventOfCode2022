
filename = 'input1.txt'

with open(filename, 'r') as file:
    input_ = [(x[0], int(x[1])) for x in [[thing for thing in line.split(' ')] for line in file.read().split('\n')]]

# part one

def follow(tail, head):
    if head[0] == tail[0] + 2:
        return (tail[0] + 1, head[1])
    if head[0] == tail[0] - 2:
        return (tail[0] - 1, head[1])
    if head[1] == tail[1] + 2:
        return (head[0], tail[1] + 1)
    if head[1] == tail[1] - 2:
        return (head[0], tail[1] - 1)
    return tail

head = (0, 0)
tail = (0, 0)
visited = set([(0, 0)])

for instruction in input_:
    if instruction[0] == 'U':
        for i in range(instruction[1]):
            head = (head[0], head[1] + 1)
            tail = follow(tail, head)
            visited.add(tail)
    elif instruction[0] == 'D':
        for i in range(instruction[1]):
            head = (head[0], head[1] - 1)
            tail = follow(tail, head)
            visited.add(tail)
    elif instruction[0] == 'R':
        for i in range(instruction[1]):
            head = (head[0] + 1, head[1])
            tail = follow(tail, head)
            visited.add(tail)
    else:
        for i in range(instruction[1]):
            head = (head[0] - 1, head[1])
            tail = follow(tail, head)
            visited.add(tail)

print(len(visited))

# part two

def follow(tail, head): # can now have diagonal pull
    if head[0] == tail[0] + 2:
        if head[1] == tail[1] + 2:
            return (tail[0] + 1, tail[1] + 1)
        elif head[1] == tail[1] - 2:
            return (tail[0] + 1, tail[1] - 1)
        else:
            return (tail[0] + 1, head[1])
    elif head[0] == tail[0] - 2:
        if head[1] == tail[1] + 2:
            return (tail[0] - 1, tail[1] + 1)
        elif head[1] == tail[1] - 2:
            return (tail[0] - 1, tail[1] - 1)
        else:
            return (tail[0] - 1, head[1])
    elif head[1] == tail[1] + 2:
        if head[0] == tail[0] + 2:
            return (tail[0] + 1, tail[1] + 1)
        elif head[0] == tail[0] - 2:
            return (tail[0] - 1, tail[1] + 1)
        else:
            return (head[0], tail[1] + 1)
    elif head[1] == tail[1] - 2:
        if head[0] == tail[0] + 2:
            return (tail[0] + 1, tail[1] - 1)
        elif head[0] == tail[0] - 2:
            return (tail[0] - 1, tail[1] - 1)
        else:
            return (head[0], tail[1] - 1)
    return tail

rope = [
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0),
    (0, 0)
]
visited = set([(0, 0)])

for instruction in input_:
    if instruction[0] == 'U':
        for i in range(instruction[1]):
            rope[0] = (rope[0][0], rope[0][1] + 1)
            for section in range(1, 10):
                rope[section] = follow(rope[section], rope[section - 1])
            visited.add(rope[9])
    elif instruction[0] == 'D':
        for i in range(instruction[1]):
            rope[0] = (rope[0][0], rope[0][1] - 1)
            for section in range(1, 10):
                rope[section] = follow(rope[section], rope[section - 1])
            visited.add(rope[9])
    elif instruction[0] == 'R':
        for i in range(instruction[1]):
            rope[0] = (rope[0][0] + 1, rope[0][1])
            for section in range(1, 10):
                rope[section] = follow(rope[section], rope[section - 1])
            visited.add(rope[9])
    else:
        for i in range(instruction[1]):
            rope[0] = (rope[0][0] - 1, rope[0][1])
            for section in range(1, 10):
                rope[section] = follow(rope[section], rope[section - 1])
            visited.add(rope[9])

print(len(visited))
