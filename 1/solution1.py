
filename = 'input1.txt'

with open(filename, 'r') as file:
    input_ = file.read().split('\n\n')

aggregated_input = list(map(lambda x: sum([int(y) for y in x.split('\n')]), input_))

# for part 1

print(max(aggregated_input)) 

# for part 2

total = 0
for _ in range(3):
    maxima = [(i, v) for i, v in enumerate(aggregated_input) if v == max(aggregated_input)]
    total += maxima[0][1]
    aggregated_input.pop(maxima[0][0])

print(total) 

