def main():
    with open('2025/6/inputs.txt') as file:
        lines = list(zip(*list(map(lambda l: l.strip().split(), file.readlines()))))
        total = 0
        for line in lines:
            if line[-1] == '+':
                total += sum(map(int, line[:-1]))
            elif line[-1] == '*':
                prod = 1
                for num in map(int, line[:-1]):
                    prod *= num
                total += prod
        print(total)


def main2():
    with open('2025/6/inputs.txt') as file:
        lines = list(map(lambda l: l.strip(), file.readlines()))



main()
main2()
