from day5_part1 import fresh_ingredient


def solve():
    fresh_ingredient.sort()
    last = None
    answer = 0
    for low, high in fresh_ingredient:
        if last is None:
            last = (low, high)
        elif last[1] < low:
            answer += last[1] - last[0] + 1
            last = (low, high)
        else:
            last = (last[0], max(last[1], high))
        
    answer += last[1] - last[0] + 1

    return answer

if __name__ == "__main__":
    answer = solve()
    print(answer)