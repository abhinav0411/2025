from day3_part1 import battery

def solve():
    answer = 0
    jolts = 0
    working = battery[:]
    for index in range(11):
        digit = max(working[:index - 11])
        working = working[working.index(digit) + 1:]
        jolts += (jolts * 10) + int(digit)
    jolts += (jolts  * 10) + int(max(working))
    answer += jolts
    return answer

if __name__ == "__main__":
    answer = solve()
    print(answer)