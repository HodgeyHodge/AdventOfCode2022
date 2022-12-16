
filename = 'input1.txt'

def valuation(char):
    return ord(char) - 38 if char == char.upper() else ord(char) - 96

# part one

with open(filename, 'r') as file:
    input_ = [[set(line[:len(line)//2]), set(line[len(line)//2:])] for line in file.read().split('\n')]

print(sum([valuation(x) for item in input_ for x in item[0] if x in item[1]]))

# part two

with open(filename, 'r') as file:
    input_ = [set(line) for line in file.read().split('\n')]

grouped_input = [list(input_[3*i].intersection(input_[3*i + 1], input_[3*i + 2])) for i in range(len(input_)//3)]

print(grouped_input)

if max([len(i) for i in grouped_input]) > 1:
    print('Danger Zone!')

print(sum([valuation(x[0]) for x in grouped_input]))