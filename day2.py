with open("inputs/input_2.txt") as input_two:
    positions = [(line.split()[0], int(line.split()[1])) for line in input_two.readlines()]

def part_1():
    d = 0
    h = 0
    for t, s in positions:
        if t == 'forward':
            h += s
        if t == 'up':
            d -= s
        if t == 'down':
            d += s
    return d * h

def part_2():
    d = 0
    h = 0
    a = 0
    for t, s in positions:
        if t == 'forward':
            h += s
            d += (a * s)
        if t == 'up':
            a -= s
        if t == 'down':
            a += s
    return d * h

print(f"Part 1 -> {part_1()}")
print(f"Part 2 -> {part_2()}")