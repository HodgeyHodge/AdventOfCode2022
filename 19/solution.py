import math

live_blueprints = [
    (3, 4, (4, 18), (3,  8)),
    (2, 4, (4, 20), (3, 14)),
    (4, 4, (2, 11), (4,  8)),
    (3, 3, (2, 19), (2, 20)),
    (4, 3, (4,  8), (3,  7)),
    (3, 4, (2, 11), (2, 10)),
    (2, 3, (3, 16), (2, 11)),
    (4, 3, (4,  6), (3, 11)),
    (4, 4, (4,  8), (2, 15)),
    (4, 4, (4, 17), (2, 13)),
    (2, 4, (4, 15), (2, 15)),
    (2, 4, (3, 20), (2, 17)),
    (4, 4, (4, 12), (4, 19)),
    (2, 3, (3, 11), (2, 16)),
    (3, 4, (3, 16), (3, 14)),
    (4, 4, (3,  9), (3,  7)),
    (2, 3, (2, 16), (2,  9)),
    (3, 3, (2, 14), (3, 17)),
    (4, 4, (4, 16), (2, 15)),
    (2, 4, (4, 16), (4, 17)),
    (3, 3, (3, 16), (3,  9)),
    (3, 3, (4, 19), (4,  7)),
    (3, 3, (3, 19), (3, 19)),
    (3, 3, (3,  8), (2, 12)),
    (2, 2, (2,  7), (2, 14)),
    (4, 3, (2, 13), (2, 10)),
    (3, 4, (2, 20), (4,  7)),
    (2, 3, (2, 14), (3,  8)),
    (4, 4, (3,  5), (3, 18)),
    (3, 3, (3, 16), (3, 20))
] 

test_blueprints = [
    (4, 2, (3, 14), (2,  7)),
    (2, 3, (3,  8), (3, 12))
]

def explore_blueprint(time_limit, blueprint):
    best = 0
    operations = [('', 0, (1, 0, 0), (0, 0, 0, 0))]

    for operation in operations:
        if operation[3][3] + 0.5 * (time_limit - operation[1]) * (time_limit - operation[1] + 1) <= best:
            continue
    
        if operation[2][0] < max(blueprint[0], blueprint[1], blueprint[2][0], blueprint[3][0]):
            time_to_complete = 1 + max(0, math.ceil((blueprint[0] - operation[3][0]) / operation[2][0]))
            if operation[1] + time_to_complete <= time_limit:
                operations.append([
                    operation[0] + 'R',
                    operation[1] + time_to_complete,
                    (operation[2][0] + 1, operation[2][1], operation[2][2]),
                    (
                        operation[3][0] + operation[2][0] * time_to_complete - blueprint[0],
                        operation[3][1] + operation[2][1] * time_to_complete,
                        operation[3][2] + operation[2][2] * time_to_complete,
                        operation[3][3]
                    )
                ])
    
        if operation[2][1] < blueprint[2][1]:
            time_to_complete = 1 + max(0, math.ceil((blueprint[1] - operation[3][0]) / operation[2][0]))
            if operation[1] + time_to_complete <= time_limit:
                operations.append([
                    operation[0] + 'C',
                    operation[1] + time_to_complete,
                    (operation[2][0], operation[2][1] + 1, operation[2][2]),
                    (
                        operation[3][0] + operation[2][0] * time_to_complete - blueprint[1],
                        operation[3][1] + operation[2][1] * time_to_complete,
                        operation[3][2] + operation[2][2] * time_to_complete,
                        operation[3][3]
                    )
                ])
        
        if operation[2][2] < blueprint[3][1] and operation[2][1] > 0:
            time_to_complete = 1 + max(
                0,
                math.ceil((blueprint[2][0] - operation[3][0]) / operation[2][0]),
                math.ceil((blueprint[2][1] - operation[3][1]) / operation[2][1]),
            )
            if operation[1] + time_to_complete <= time_limit:
                operations.append([
                    operation[0] + 'B',
                    operation[1] + time_to_complete,
                    (operation[2][0], operation[2][1], operation[2][2] + 1),
                    (
                        operation[3][0] + operation[2][0] * time_to_complete - blueprint[2][0],
                        operation[3][1] + operation[2][1] * time_to_complete - blueprint[2][1],
                        operation[3][2] + operation[2][2] * time_to_complete,
                        operation[3][3]
                    )
                ])
    
        if operation[2][2] > 0:
            time_to_complete = 1 + max(
                0,
                math.ceil((blueprint[3][0] - operation[3][0]) / operation[2][0]),
                math.ceil((blueprint[3][1] - operation[3][2]) / operation[2][2]),
            )
            if operation[1] + time_to_complete <= time_limit:
                operations.append([
                    operation[0] + 'G',
                    operation[1] + time_to_complete,
                    (operation[2][0], operation[2][1], operation[2][2]),
                    (
                        operation[3][0] + operation[2][0] * time_to_complete - blueprint[3][0],
                        operation[3][1] + operation[2][1] * time_to_complete,
                        operation[3][2] + operation[2][2] * time_to_complete - blueprint[3][1],
                        operation[3][3] + (time_limit - time_to_complete - operation[1])
                    )
                ])
                best = max(best, operation[3][3]+ (time_limit - time_to_complete - operation[1]))
    
    return best


# part one

print(explore_blueprint(24, test_blueprints[0]))
print(explore_blueprint(24, test_blueprints[1]))

for b in live_blueprints:
    print(explore_blueprint(24, b))

# part two

print(explore_blueprint(32, test_blueprints[0]))
print(explore_blueprint(32, test_blueprints[1]))

print(explore_blueprint(32, live_blueprints[0]))
print(explore_blueprint(32, live_blueprints[1]))
print(explore_blueprint(32, live_blueprints[2]))



