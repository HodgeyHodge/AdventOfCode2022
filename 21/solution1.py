
def load(filename):
    with open(filename) as file:
        return {x[0]: x[1] for x in [line.split(': ') for line in file.read().split('\n')]}

def merge_figures(data):
    progress = False
    pop_me = []
    for k in data:
        try:
            data[k] = str(eval(data[k]))
            for j, w in data.items():
                if w.find(k) > -1:
                    progress = True
                    data[j] = w.replace(k, data[k])
            pop_me.append(k)
        except NameError:
            pass
    for p in pop_me:
        if p != 'root':
            data.pop(p)
    return progress

def part_one(filename):
    data = load(filename)
    while True:
        if not merge_figures(data):
            break
    print(data['root'])

part_one('testinput1.txt')
part_one('input1.txt')

def part_two(filename):
    data = load(filename)

    # reduce what can be reduced

    data['humn'] = 'humn'
    while True:
        if not merge_figures(data):
            break
    #print(data)

    # then traverse the logic, undoing all operations:

    current = 'humn'
    output = []
    while True:
        next_ = [k for k in data if data[k].find(current) > -1]
        if len(next_):
            output.append(data[next_[0]])
            current = next_[0]
        else:
            break

    for step in range(len(output) - 1, -1, -1):
        print(output[step])

part_two('testinput1.txt')
part_two('input1.txt')

# honestly quicker from this point to manually step down the list and undo each operation than to unpick programmatically...