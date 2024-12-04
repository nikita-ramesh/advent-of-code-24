def part_one(f):
    safe_count = 0
    for line in f:
        l = [int(e) for e in line.strip().split()]
        is_valid, _ = check_list(l)
        if is_valid:
            safe_count += 1
    return safe_count

def part_two(f):
    safe_count = 0
    for line in f:
        l = [int(e) for e in line.strip().split()]
        is_valid, critical_points = check_list(l)
        if is_valid:
            safe_count += 1
        else:
            for critical_point in critical_points:
                l_copy = l[:]
                l_copy.pop(critical_point)
                is_copy_valid, _ = check_list(l_copy)
                if is_copy_valid:
                    safe_count += 1
                    break
    return safe_count

def check_list(l: list[int]) -> tuple[bool, set[int]]:
    is_increasing = True
    is_decreasing = True
    critical_points = set()
    # check if its increasing in valid way
    for i in range(1, len(l)):
        if (l[i-1] >= l[i]) or (abs(l[i-1] - l[i])) > 3 or (abs(l[i-1] - l[i])) < 1:
            is_increasing = False
            critical_points.add(i-1)
            critical_points.add(i)
            break
    # check if it's decreasing in valid way
    for i in range(1, len(l)):
        if (l[i-1] <= l[i]) or (abs(l[i-1] - l[i])) > 3 or (abs(l[i-1] - l[i])) < 1:
            is_decreasing = False
            critical_points.add(i-1)
            critical_points.add(i)
            break
    return (is_increasing or is_decreasing, critical_points)

def main():
    f = open("inputs/input2.txt", "r")
    print("AOC Day 2 Part One:", part_one(f))
    f.seek(0)
    print("AOC Day 2 Part Two:", part_two(f))

if __name__ == "__main__":
    main()
