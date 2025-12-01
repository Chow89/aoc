def main():
    with open('2025/1/inputs.txt') as file:
        lines = map(lambda l: l.strip(), file.readlines())
        pos = 50
        zeros = 0
        for line in lines:
            if line[0] == 'L':
                pos -= int(line[1:])
            else:
                pos += int(line[1:])
            if pos % 100 == 0:
                zeros += 1
        print(zeros)


def main2():
    with open('2025/1/inputs.txt') as file:
        lines = map(lambda l: l.strip(), file.readlines())
        pos = 50
        zeros = 0
        for line in lines:
            number = int(line[1:])
            fullturns = number // 100
            zeros += fullturns
            number = number % 100
            if line[0] == 'L':
                if pos != 0 and pos - number <= 0:
                    zeros += 1
                pos = pos - number
            else:
                if pos + number >= 100:
                    zeros += 1
                pos = pos + number

            pos = pos % 100
        print(zeros)


main()
main2()
