
def load_input(filename):
    with open(filename) as file:
        return [int(n) for n in file.read().split('\n')]

def build_linked_list(data):
    l = len(data)
    output = []
    for i, v in enumerate(data):
        output.append((v, (i - 1) % len(data), (i + 1) % l))
    return output

def pretty_print(linked_list):
    zeroes = [i for i, v in enumerate(linked_list) if v[0] == 0]
    if len(zeroes) != 1:
        raise Exception(f'Was expecting a unique 0 in the linked list...')
    i = zeroes[0]
    for _ in range(len(linked_list)):
        print(linked_list[i][0], end=",")
        i = traverse(linked_list, i, 1)
    print("")

def traverse(linked_list, i, n):
    if n > 0:
        for _ in range(n):
            i = linked_list[i][2]
    elif n < 0:
        for _ in range(-n):
            i = linked_list[i][1]
    return i

def get_position(linked_list, magic_multiplier = 1):
    i0 = [i for i, v in enumerate(linked_list) if v[0] == 0][0]
    i1 = traverse(linked_list, i0, 1000)
    i2 = traverse(linked_list, i1, 1000)
    i3 = traverse(linked_list, i2, 1000)
    return (linked_list[i1][0], linked_list[i2][0], linked_list[i3][0], magic_multiplier * (linked_list[i1][0] + linked_list[i2][0] + linked_list[i3][0]))

def mix(linked_list, magic_multiplier = 1):
    l = len(linked_list)
    for k, v in enumerate(linked_list):
        offset = (magic_multiplier * v[0]) % (l - 1)
        old_prev = traverse(linked_list, k, -1)
        old_next = traverse(linked_list, k, 1)
        while v[0] < 0:
            v = (v[0] + l - 1, v[1], v[2])
        if v[0] > 0 and offset != 0:
            new_prev = traverse(linked_list, k, offset)
            new_next = traverse(linked_list, new_prev, 1)
            linked_list[old_prev] = (linked_list[old_prev][0], linked_list[old_prev][1], old_next)
            linked_list[old_next] = (linked_list[old_next][0], old_prev, linked_list[old_next][2])
            linked_list[new_prev] = (linked_list[new_prev][0], linked_list[new_prev][1], k)
            linked_list[new_next] = (linked_list[new_next][0], k, linked_list[new_next][2])
            linked_list[k] = (linked_list[k][0], new_prev, new_next)

# part one

filename = 'testinput1.txt'
data = load_input(filename)
linked_list = build_linked_list(data)
mix(linked_list)
print(get_position(linked_list))

filename = 'input1.txt'
data = load_input(filename)
linked_list = build_linked_list(data)
mix(linked_list)
print(get_position(linked_list))

# part two

filename = 'testinput1.txt'
data = load_input(filename)
linked_list = build_linked_list(data)
for _ in range(10):
    mix(linked_list, 811589153)
print(get_position(linked_list, 811589153))

filename = 'input1.txt'
data = load_input(filename)
linked_list = build_linked_list(data)
for _ in range(10):
    mix(linked_list, 811589153)
print(get_position(linked_list, 811589153))

