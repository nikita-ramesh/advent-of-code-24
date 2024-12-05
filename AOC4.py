WORD_FRONT = ['X', 'M', 'A', 'S']
WORD_BACK = WORD_FRONT[::-1]
WORD_MAS = ['M', 'A', 'S']

def part_one(f):
    matrix = f.readlines()
    matrix = [e.strip() for e in matrix]
    count = 0
    count += count_vertical(WORD_FRONT, matrix)
    count += count_vertical(WORD_BACK, matrix)
    count += count_horizontal(WORD_FRONT, matrix)
    count += count_horizontal(WORD_BACK, matrix)
    count += count_left_diagonal(WORD_FRONT, matrix)
    count += count_left_diagonal(WORD_BACK, matrix)
    count += count_right_diagonal(WORD_FRONT, matrix)
    count += count_right_diagonal(WORD_BACK, matrix)
    return count

def part_two(f):
    matrix = f.readlines()
    matrix = [e.strip() for e in matrix]
    count = count_cross_mas(WORD_MAS, matrix)
    return count

# Helper functions for part one.
def count_vertical(word, matrix):
    count = 0
    for row in range(len(matrix)-3):
        for col in range(len(matrix[0])):
            if all(matrix[row+x][col] == word[x] for x in range(4)):
                count += 1
    return count

def count_horizontal(word, matrix):
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])-3):
            if all(matrix[row][col+x] == word[x] for x in range(4)):
                count += 1
    return count

def count_left_diagonal(word, matrix):
    count = 0
    for row in range(len(matrix)-3):
        for col in range(len(matrix[0])-3):
            if all(matrix[row+x][col+x] == word[x] for x in range(4)):
                count += 1
    return count

def count_right_diagonal(word, matrix):
    count = 0
    for row in range(len(matrix)-3):
        for col in range(3, len(matrix[0])):
            if all(matrix[row+x][col-x] == word[x] for x in range(4)):
                count += 1
    return count

# Helper functions for part two.
def count_cross_mas(word, matrix):
    count = 0
    rev_word = word[::-1]
    for row in range(len(matrix)-2):
        for col in range(len(matrix[0])-2):
            if (all(matrix[row+x][col+x] == word[x] for x in range(3)) or all(matrix[row+x][col+x] == rev_word[x] for x in range(3))) and ((all(matrix[row + x][col + y] == word[x] for x, y in zip(range(2, -1, -1), range(3)))) or (all(matrix[row + x][col + y] == rev_word[x] for x, y in zip(range(2, -1, -1), range(3))))):
                count += 1
    return count

def main():
    f = open("inputs/input4.txt", "r")
    total = part_one(f)
    print("AOC Day 4 Part One:", total)
    f.seek(0)
    total = part_two(f)
    print("AOC Day 4 Part Two:", total)

if __name__ == "__main__":
    main()
