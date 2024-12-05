def part_one(f):
    l = f.read().strip().split("mul(")
    l = [e.strip().split(")")[0].split(",") for e in l]
    total = 0
    for e in l:
        if len(e) == 2 and e[0].isdigit() and e[1].isdigit():
            total += int(e[0]) * int(e[1])
    return total

def part_two(f):
    # Building the list of operations.
    l = f.read().strip().split("mul(")
    l = [e.strip().split(")") for e in l]
    total = 0
    ops_stack = []
    for e in l:
        vals = e[0].split(",")
        if len(vals) == 2 and vals[0].isdigit() and vals[1].isdigit():
            ops_stack.append((int(vals[0]), int(vals[1])))
        for x in e:
            if (x[-6:] == "don't("):
                ops_stack.append(False)
            elif (x[-3:] == "do("):
                ops_stack.append(True)

    # Filtering based on dos and don'ts.
    last_ops = True
    for i, ops in enumerate(ops_stack):
        if last_ops == False and isinstance(ops, tuple):
            ops_stack[i] = (0, 0)
        if ops == False:
            last_ops = False
        elif ops == True:
            last_ops = True

    # Calculating the total.
    total = sum([ops[0] * ops[1] for ops in ops_stack if isinstance(ops, tuple)])
    return total

def main():
    f = open("inputs/input3.txt", "r")
    total = part_one(f)
    print("AOC Day 3 Part One:", total)
    f.seek(0)
    total = part_two(f)
    print("AOC Day 3 Part Two:", total)

if __name__ == "__main__":
    main()