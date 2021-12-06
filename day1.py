with open("inputs/input_1.txt") as in_one:
    depths = [int(line) for line in in_one.readlines()]

decreasing = lambda depth_pair: depth_pair[0] < depth_pair[1]

def calculate(readings):
    return sum(map(decreasing, zip(readings, readings[1:])))

def part_1():
    return calculate(depths)

def part_2():
    windows = [sum((a, b, c)) for a, b, c in zip(depths, depths[1:], depths[2:])]
    return calculate(windows)

print(f"Part 1 -> {part_1()}")
print(f"Part 2 -> {part_2()}")