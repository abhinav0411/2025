from day1_part1 import codes

start = 50
no_of_zeros = 0
for code in codes:
    code_int = int(code[1:])
    while (code_int > 0):
        if code[0:1] == "L":
            start -= 1
        else:
            start += 1

        if start > 99:
            start = 0
        if start == 0:
            no_of_zeros += 1
        if start < 0:
            start = 99

        code_int -= 1

if __name__ == "__main__":
    print(no_of_zeros)