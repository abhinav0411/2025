from day2_part1 import list_ids

def part2():
    answer = 0
    for ids in list_ids:
        for num in range(ids[0], ids[1]+1):
            s = str(num)
            for i in range(2, len(s) + 1):
                if len(s) % i == 0 and s[:len(s) // i] * i == s:
                    answer += num
                    break


    return answer

#4174379265
if __name__ == "__main__":
    answer = part2()
    print(answer)