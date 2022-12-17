
filename = 'input1.txt'

with open(filename, 'r') as file:
    input_ = [line for line in file.read().split('\n')]

normalised_input = [0, 0]

for line in input_:
    if line.startswith('addx '):
        normalised_input.extend((int(line[5:]), 0))
    else:
        normalised_input.append(0)

beam_position = 1
display = ''
signal_strength = 0
for i in range(len(normalised_input)):
    if i % 40 == 20:
        signal_strength += i * beam_position
    beam_position += normalised_input[i]
    display += '#' if (i) % 40 in [beam_position - 1, beam_position, beam_position + 1] else ' '
    if i % 40 == 39:
        display += '\n'

print(signal_strength) # part one
print(display) # part two