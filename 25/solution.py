
with open('input.txt') as file:
    snafu_numbers = [line for line in file.read().split('\n')]

print(snafu_numbers)

decoder = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2
}
encoder = { # lol
    2: '2',
    1: '1',
    0: '0',
    -1: '-',
    -2: '='
}

# sum the numbers column-wise

output_deconstructed = [
    sum(decoder[s[-i]] for s in snafu_numbers if len(s) >= i) for i in range(1, max(len(n) for n in snafu_numbers) + 1)
]

# normalise the deconstructed sum

for i in range(len(output_deconstructed) - 1):
    while output_deconstructed[i] > 2:
        output_deconstructed[i + 1] += 1
        output_deconstructed[i] -= 5
    while output_deconstructed[i] < -2:
        output_deconstructed[i + 1] -= 1
        output_deconstructed[i] += 5

# reconstruct!

print(''.join(encoder[i] for i in reversed(output_deconstructed)))