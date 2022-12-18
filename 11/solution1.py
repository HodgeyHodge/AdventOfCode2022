from math import floor

class Monkey:
    def __init__(self, items, operation, base, true_recipient, false_recipient):
        self.items = items
        self.operation = operation
        self.base = base
        self.true_recipient = true_recipient
        self.false_recipient = false_recipient
        self.inspections = 0
    
    def __repr__(self):
        return f'<{self.items}, {self.inspections}>'
    
    def receive(self, item):
        self.items.append(item)
    
    def test(self, item):
        return item % self.base == 0

def test_monkeys():
    return [
        Monkey([79, 98], lambda x: x * 19, 23, 2, 3),
        Monkey([54, 65, 75, 74], lambda x: x + 6, 19, 2, 0),
        Monkey([79, 60, 97], lambda x: x * x, 13, 1, 3),
        Monkey([74], lambda x: x + 3, 17, 0, 1)
    ]

def live_monkeys():
    return [
        Monkey([59, 74, 65, 86], lambda x: x * 19, 7, 6, 2),
        Monkey([62, 84, 72, 91, 68, 78, 51], lambda x: x + 1, 2, 2, 0),
        Monkey([78, 84, 96], lambda x: x + 8, 19, 6, 5),
        Monkey([97, 86], lambda x: x * x, 3, 1, 0),
        Monkey([50], lambda x: x + 6, 13, 3, 1),
        Monkey([73, 65, 69, 65, 51], lambda x: x * 17, 11, 4, 7),
        Monkey([69, 82, 97, 93, 82, 84, 58, 63], lambda x: x + 5, 5, 5, 7),
        Monkey([81, 78, 82, 76, 79, 80], lambda x: x + 3, 17, 3, 4)
    ]

def iterate(modulus, diminishing_worry):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.inspections += 1
            if diminishing_worry:
                updated_item = floor(monkey.operation(item) / 3)
            else:
                updated_item = monkey.operation(item) % modulus # this is the trick
            if monkey.test(updated_item):
                monkeys[monkey.true_recipient].receive(updated_item)
            else:
                monkeys[monkey.false_recipient].receive(updated_item)
        monkey.items = []

# part one

monkeys = test_monkeys()
print(monkeys)
for i in range(20):
    iterate(None, True)
    print(f'iteration {i + 1}')
    print(monkeys)

monkeys = live_monkeys()
print(monkeys)
for i in range(20):
    iterate(2 * 3 * 5 * 7 * 11 * 13 * 17 * 19, True)
    print(f'iteration {i + 1}')
    print(monkeys)

# part two

monkeys = test_monkeys()
print(monkeys)
for i in range(10000):
    iterate(13 * 17 * 19 * 23, False)
    if i % 100 == 99:
        print(f'iteration {i + 1}')
print(monkeys)

monkeys = live_monkeys()
print(monkeys)
for i in range(10000):
    iterate(2 * 3 * 5 * 7 * 11 * 13 * 17 * 19, False)
    if i % 100 == 99:
        print(f'iteration {i + 1}')
print(monkeys)