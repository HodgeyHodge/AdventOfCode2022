
import json

def compare(l, r):
    if type(l) is int and type(r) is int:
        if l < r:
            return 1
        if l > r:
            return -1
        else:
            return 0
    elif type(l) is int and type(r) is list:
        return compare([l], r)
    elif type(l) is list and type(r) is int:
        return compare(l, [r])
    else:
        i = 0
        while True:
            if len(l) == i and len(r) == i:
                return 0
            elif len(l) == i:
                return 1
            elif len(r) == i:
                return -1
            else:
                point_comparison = compare(l[i], r[i])
                if point_comparison != 0:
                    return point_comparison
            i += 1


# part one

def load_file(filename):
    out = []
    with open(filename, 'r') as file:
        for line in file.read().split('\n\n'):
            l, r = line.split('\n')
            out.append((json.loads(l), json.loads(r)))
    return out

input_ = load_file('input1.txt')

print(sum(i + 1 for i, v in enumerate(input_) if compare(v[0], v[1]) == 1))


# part two

def load_file(filename):
    out = []
    with open(filename, 'r') as file:
        for line in file.read().replace('\n\n', '\n').split('\n'):
            out.append(json.loads(line))
    return out

input_ = load_file('input1.txt')

d1 = [[2]]
d2 = [[6]]

p1 = len([i for i in input_ if compare(i, d1) == 1])
p2 = len([i for i in input_ if compare(i, d2) == 1])

print((p1 + 1) * (p2 + 2))