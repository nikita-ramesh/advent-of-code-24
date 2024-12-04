def part_one(f):
    l1 = []
    l2 = []
    for line in f:
        l = line.strip().split()
        l1.append(l[0])
        l2.append(l[1])
    l1.sort()
    l2.sort()
    total = 0
    for i in range(len(l1)):
        total += abs(int(l1[i]) - int(l2[i]))
    return total, l1, l2

def part_two(f, l1, l2):
    occurences = {}
    for e in l2:
        if int(e) not in occurences:
            occurences[int(e)] = 1
        else:
            occurences[int(e)] += 1

    similarity = 0
    for e1 in l1:
        if int(e1) in occurences:
            similarity += int(e1) * int(occurences[int(e1)])

    return similarity

def main():
    f = open("inputs/input1.txt", "r")
    total, l1, l2 = part_one(f)
    print("AOC Day 1 Part One:", total)
    f.seek(0)
    similarity = part_two(f, l1, l2)
    print("AOC Day 1 Part Two:", similarity)

if __name__ == "__main__":
    main()
