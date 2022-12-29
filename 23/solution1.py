
def load_data(filename):
    output = []
    with open(filename) as file:
        lines = [line for line in file.read().split('\n')]
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[len(lines) - i - 1][j] == '#':
                    output.append((i, j))
    return output

order_of_play = [
    lambda elf: (elf[0] + 1, elf[1]) if (elf[0] + 1, elf[1] - 1) not in elves and (elf[0] + 1, elf[1]) not in elves and (elf[0] + 1, elf[1] + 1) not in elves else None,
    lambda elf: (elf[0] - 1, elf[1]) if (elf[0] - 1, elf[1] - 1) not in elves and (elf[0] - 1, elf[1]) not in elves and (elf[0] - 1, elf[1] + 1) not in elves else None,
    lambda elf: (elf[0], elf[1] - 1) if (elf[0] - 1, elf[1] - 1) not in elves and (elf[0], elf[1] - 1) not in elves and (elf[0] + 1, elf[1] - 1) not in elves else None,
    lambda elf: (elf[0], elf[1] + 1) if (elf[0] - 1, elf[1] + 1) not in elves and (elf[0], elf[1] + 1) not in elves and (elf[0] + 1, elf[1] + 1) not in elves else None,
    lambda elf: (elf[0], elf[1])
]

def lonely(elf, elves):
    if (elf[0] - 1, elf[1] - 1) in elves or \
        (elf[0] - 1, elf[1]) in elves or \
        (elf[0] - 1, elf[1] + 1) in elves or \
        (elf[0], elf[1] - 1) in elves or \
        (elf[0], elf[1] + 1) in elves or \
        (elf[0] + 1, elf[1] - 1) in elves or \
        (elf[0] + 1, elf[1]) in elves or \
        (elf[0] + 1, elf[1] + 1) in elves:
        return False
    return True

def cycle(order_of_play):
    return order_of_play[1:4] + [order_of_play[0], order_of_play[4]]

def iterate(elves, order_of_play):
    propositions = {}
    non_movers = []
    for elf in elves:
        if lonely(elf, elves):
            non_movers.append(elf)
        else:
            proposition = [x for x in [f(elf) for f in order_of_play] if x][0]
            if proposition in propositions:
                non_movers.append(elf)
                non_movers.append(propositions[proposition])
            propositions[proposition] = elf
    return [k for k, v in propositions.items() if v not in non_movers] + non_movers


elves = load_data('input1.txt')

i = 0
while True:
    i += 1
    new_elves = iterate(elves, order_of_play)
    order_of_play = cycle(order_of_play)
    changes = len(set(new_elves) -  set(elves))
    print(f'Iteration {i}: {changes} changes.')
    if changes == 0:
        break
    elves = new_elves

    if i == 10:
        area = (1 + max([e[0] for e in elves]) - min([e[0] for e in elves])) * \
            (1 + max([e[1] for e in elves]) - min([e[1] for e in elves])) - \
            len(elves)
        print(f'Part one: area = {area}.')



