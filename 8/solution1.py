
filename = 'input1.txt'
width = 99

with open(filename, 'r') as file:
    input_ = [[int(x) for x in list(line)] for line in file.read().split('\n')]

original = input_
transposition = list(map(list, zip(*original)))

# part one

internal_visible_count = 0

for x in range(1, width - 1):
    for y in range(1, width - 1):
        if min(
            max(original[x][y + 1:]),
            max(original[x][:y]),
            max(transposition[y][x + 1:]),
            max(transposition[y][:x])
        ) < original[x][y]:
            internal_visible_count += 1

print(internal_visible_count + 4 * (width - 1))

# part two

def scenic_score(row, index):
    blocker_right = min([i for i in range(width) if i > index and row[i] >= row[index]] + [width - 1])
    blocker_left = max([i for i in range(width) if i < index and row[i] >= row[index]] + [0])
    return (index - blocker_left) * (blocker_right - index)


scenic_score_max = 0

for x in range(1, width - 1):
    for y in range(1, width - 1):
        score = scenic_score(original[x], y) * scenic_score(transposition[y], x)
        if score > scenic_score_max:
            scenic_score_max = score

print(scenic_score_max)