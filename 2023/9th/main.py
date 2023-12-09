def main():
    with open('2023/9th/inputs.txt') as file:
        lines = file.readlines()
        result = 0
        for line in lines:
            triangle = [list(map(int, line.split()))]
            while len(list(filter(lambda x: x != 0, triangle[-1]))) > 1:
                diffs = []
                for i in range(len(triangle[-1]) - 1):
                    diffs.append(triangle[-1][i + 1] - triangle[-1][i])
                triangle.append(diffs)

            last_row = [0]
            for diffs in reversed(triangle):
                last_row = [*diffs, diffs[-1] + last_row[-1]]

            result += last_row[-1]
        print(result)


def main2():
    with open('2023/9th/inputs.txt') as file:
        lines = file.readlines()
        result = 0
        for line in lines:
            triangle = [list(map(int, line.split()))]
            while len(list(filter(lambda x: x != 0, triangle[-1]))) > 1:
                diffs = []
                for i in range(len(triangle[-1]) - 1):
                    diffs.append(triangle[-1][i + 1] - triangle[-1][i])
                triangle.append(diffs)

            last_row = [0]
            for diffs in reversed(triangle):
                last_row = [diffs[0] - last_row[0], *diffs]

            result += last_row[0]
        print(result)


main()
main2()
