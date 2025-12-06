from day4_part1 import paper_rolls, h, w


def check(row, col, paper_rolls):
    number = 0

    if row-1 >= 0 and col-1 >= 0 and paper_rolls[row-1][col-1] == "@":
        number += 1
    if row+1 < h and col+1 < w and paper_rolls[row+1][col+1] == "@":
        number += 1
    if row < h and col+1 < w and paper_rolls[row][col+1] == "@":
        number += 1
    if row < h and col-1 >= 0 and paper_rolls[row][col-1] == "@":
        number += 1
    if row+1 < h and col < w and paper_rolls[row+1][col] == "@":
        number += 1
    if row-1 >= 0 and col < w and paper_rolls[row-1][col] == "@":
        number += 1
    if row+1 < h and col-1 >= 0 and paper_rolls[row+1][col-1] == "@":
        number += 1
    if row-1 >= 0 and col+1 < w and paper_rolls[row-1][col+1] == "@":
        number += 1
    
    
    if number >= 4:
        return False
    
    return True


def change(paper_rolls):
    new_rolls = [[0 for _ in range(w)] for _ in range(h)]
    iteration_count = 0
    removed_rolls = 0

    for i in range(h):
        for j in range(w):
            if paper_rolls[i][j] == ".":
                new_rolls[i][j] = "."
                continue
            elif paper_rolls[i][j] == "x":
                new_rolls[i][j] = "."
                removed_rolls += 1

                continue
            else:
                if check(i, j, paper_rolls):
                    new_rolls[i][j] = "x"
                    iteration_count += 1
                
                else:
                    new_rolls[i][j] = "@"
    return new_rolls, iteration_count, removed_rolls


def solve():
    # check -> change -> check if all rolls are done -> repeat
    solved = True
    answer = 0
    initial = paper_rolls
    total_removed = 0

    
    while solved:
        new_rolls, iteration_count, total_removed = change(initial)
        if iteration_count == 0:
            break
        answer += total_removed
        initial = new_rolls
    return answer + 1

if __name__ == "__main__":
    answer = solve()

    print(answer)