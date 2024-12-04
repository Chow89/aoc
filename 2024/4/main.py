def main():
    with open('2024/4/inputs.txt') as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        count = 0
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == 'X':
                    for d in directions:
                        if 0 <= i + d[0] < len(lines) and 0 <= j + d[1] < len(lines[i]) and lines[i + d[0]][j + d[1]] == 'M':
                            if 0 <= i + 2 * d[0] < len(lines) and 0 <= j + 2 * d[1] < len(lines[i]) and lines[i + 2 * d[0]][j + 2 * d[1]] == 'A':
                                if 0 <= i + 3 * d[0] < len(lines) and 0 <= j + 3 * d[1] < len(lines[i]) and lines[i + 3 * d[0]][j + 3 * d[1]] == 'S':
                                    count += 1
        print(count)


def main2():
    with open('2024/4/inputs.txt') as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        a = []
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == 'M':
                    for d in directions:
                        if 0 <= i + d[0] < len(lines) and 0 <= j + d[1] < len(lines[i]) and lines[i + d[0]][j + d[1]] == 'A':
                            if 0 <= i + 2 * d[0] < len(lines) and 0 <= j + 2 * d[1] < len(lines[i]) and lines[i + 2 * d[0]][j + 2 * d[1]] == 'S':
                                if 0 <= i + d[0] - d[0] < len(lines) and 0 <= j + d[1] + d[1] < len(lines[i]) and lines[i + d[0] - d[0]][j + d[1] + d[1]] == 'M':
                                    if 0 <= i + d[0] + d[0] < len(lines) and 0 <= j + d[1] - d[1] < len(lines[i]) and lines[i + d[0] + d[0]][j + d[1] - d[1]] == 'S':
                                        a.append((i + d[0], j + d[1]))
                                elif 0 <= i + d[0] - d[0] < len(lines) and 0 <= j + d[1] + d[1] < len(lines[i]) and lines[i + d[0] - d[0]][j + d[1] + d[1]] == 'S':
                                    if 0 <= i + d[0] + d[0] < len(lines) and 0 <= j + d[1] - d[1] < len(lines[i]) and lines[i + d[0] + d[0]][j + d[1] - d[1]] == 'M':
                                        a.append((i + d[0], j + d[1]))
        result = set(a)
        print(len(result))


main()
main2()
