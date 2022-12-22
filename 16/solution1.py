def load_input(filename):
    with open(filename, 'r') as file:
        input_ = [(
            line[6:8],
            int(line[23:25].replace(';', '')),
            line[line.find(' to valve') + 10:].replace(' ', '').split(',')
        ) for line in file.read().split('\n')]
    ordering = sorted([x[0] for x in input_])
    nodes = {}
    for line in input_:
        nodes[ordering.index(line[0])] = (line[1], {ordering.index(w): 1 for w in line[2]})
    return nodes

def minimise_graph(graph):
    # don't need 0-value nodes with only 2 neighbours
    pop_me_do = []
    for k, v in graph.items():
        if v[0] == 0 and len(v[1]) == 2:
            A, B = v[1].items()
            if B[0] not in graph[A[0]][1]:
                graph[A[0]][1][B[0]] = A[1] + B[1]
                graph[B[0]][1][A[0]] = A[1] + B[1]
            graph[A[0]][1].pop(k)
            graph[B[0]][1].pop(k)
            pop_me_do.append(k)
    for i in pop_me_do:
        graph.pop(i)

def complete_graph(graph):
    # work out shortest distance from any node to any other
    for k, v in graph.items():
        for _ in range(len(graph)):
            new_neighbours = []
            for neighbour, weight in v[1].items():
                    for sesquineighbour, sesquiweight in graph[neighbour][1].items():
                        if sesquineighbour != k: # don't include a -> b -> a
                            new_neighbours.append((sesquineighbour, sesquiweight + weight))
            merge_down(v[1], new_neighbours)

def merge_down(d, n):
    for thing in n:
        if thing[0] not in d or thing[1] < d[thing[0]]:
            d[thing[0]] = thing[1]

def build_walks(graph, end_time):
    walks = [{(): (0, 0)}]
    for l in range(len(graph) - 1):
        child_walks = {}
        for k, v in walks[-1].items():
            for next_node in graph:
                if next_node != 0 and next_node not in k:
                    new_time = v[0] + 1 + graph[next_node][1][(k[-1] if len(k) > 0 else 0)]
                    if new_time < end_time:
                        new_pressure = v[1] + (end_time - new_time) * graph[next_node][0]
                        child_walks[(*k, next_node)] = (new_time, new_pressure)
        walks.append(child_walks)
    return walks

def build_dual_walks(graph, end_time):
    walks = [{((), ()): (0, 0, 0)}]
    for l in range(len(graph) - 1):
        child_walks = {}
        for k, v in walks[-1].items():
            unexplored_nodes = [n for n in graph if n != 0 and n not in k[0] and n not in k[1]]
            if len(unexplored_nodes) >= 2:
                for a in unexplored_nodes:
                    t_A = v[0] + 1 + graph[a][1][(k[0][-1] if len(k[0]) > 0 else 0)]
                    p_A = (end_time - t_A) * graph[a][0]
                    for b in [b for b in unexplored_nodes if b != a and (len(k[0]) > 0 or b > a)]:
                        t_B = v[1] + 1 + graph[b][1][(k[1][-1] if len(k[1]) > 0 else 0)]
                        p_B = (end_time - t_B) * graph[b][0]
                        if t_A < end_time and t_B < end_time:
                            new_pressure = v[2] + p_A + p_B
                            child_walks[((*k[0], a), (*k[1], b))] = (t_A, t_B, new_pressure)
                        elif t_A < end_time and v[1] > end_time - 2: #only include straggler if no b at all could work
                            new_pressure = v[2] + p_A
                            child_walks[((*k[0], a), k[1])] = (t_A, v[1], new_pressure)
                        elif t_B < end_time and v[0] > end_time - 2: #as above
                            new_pressure = v[2] + p_B
                            child_walks[(k[0], (*k[1], b))] = (v[0], t_B, new_pressure)
                        else:
                            pass
            elif len(unexplored_nodes) == 1:
                next_node = unexplored_nodes[0]
                t_A = v[0] + 1 + graph[next_node][1][(k[0][-1] if len(k[0]) > 0 else 0)]
                t_B = v[1] + 1 + graph[next_node][1][(k[1][-1] if len(k[1]) > 0 else 0)]
                if t_A < end_time:
                    new_pressure = v[2] + (end_time - t_A) * graph[next_node][0]
                    child_walks[((*k[0], next_node), k[1])] = (t_A, v[1], new_pressure)
                if t_B < end_time:
                    new_pressure = v[2] + (end_time - t_B) * graph[next_node][0]
                    child_walks[(k[0], (*k[1], next_node))] = (v[0], t_B, new_pressure)
        walks.append(child_walks)
    return walks

def part_one(filename, t):
    print(f'Part one, {filename}')
    data = load_input(filename)
    minimise_graph(data)
    complete_graph(data)
    for k, v in data.items():
        print(f'{k}: {v}')

    walks = build_walks(data, t)

    l = [len(d) for d in walks]
    print(f'Number of walks per length: {l}')

    m = [max([0] + [v[1] for k, v in d.items()]) for d in walks]
    print('Best walk per length:')
    for x in ([[k, v] for (k, v) in d.items() if v[1] == m[i]] for i, d in enumerate(walks)):
        print(x)

def part_two(filename, t):
    print(f'Part two, {filename}')
    data = load_input(filename)
    minimise_graph(data)
    complete_graph(data)
    for k, v in data.items():
        print(f'{k}: {v}')

    walks = build_dual_walks(data, t)

    #print('ALL THE WALKS...')
    #for i, w in enumerate(walks):
    #    print(f'...of length {i}:')
    #    for k, v in w.items():
    #        print(f'{k}: {v}')

    l = [len(d) for d in walks]
    print(f'Number of walks per length: {l}')

    m = [max([0] + [v[2] for k, v in d.items()]) for d in walks]
    print('Best walk per length:')
    for x in ([[k, v] for (k, v) in d.items() if v[2] == m[i]] for i, d in enumerate(walks)):
        print(x)


part_one('testinput1.txt', 30)
part_one('input1.txt', 30)
part_two('testinput1.txt', 26)
part_two('input1.txt', 26) # ran for 40 minutes, but did get the right answer: [[((20, 6, 1, 52, 46), (38, 42, 41, 37, 14, 4)), (25, 23, 2304)]]
