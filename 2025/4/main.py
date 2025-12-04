def main():
    with open('2025/4/inputs.txt') as file:
        lines = list(map(lambda l: l.strip(), file.readlines()))
        directions = [(1,1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        movables = 0
        for i in range(len(lines)):
            for j in range(len(lines[0])):
                if lines[i][j] != '@':
                    continue
                count = 0
                for direction in directions:
                    x = i + direction[0]
                    y = j + direction[1]
                    if 0 <= x < len(lines) and 0 <= y < len(lines[0]):
                        if lines[x][y] == '@':
                            count += 1
                if count < 4:
                    movables += 1
        print(movables)



def main2():
    with open('2025/4/inputs.txt') as file:
        lines = list(map(lambda l: list(l.strip()), file.readlines()))
        directions = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
        total = 0
        while True:
            movables = 0
            for i in range(len(lines)):
                for j in range(len(lines[0])):
                    if lines[i][j] != '@':
                        continue
                    count = 0
                    for direction in directions:
                        x = i + direction[0]
                        y = j + direction[1]
                        if 0 <= x < len(lines) and 0 <= y < len(lines[0]):
                            if lines[x][y] == '@':
                                count += 1
                    if count < 4:
                        movables += 1
                        total += 1
                        lines[i][j] = '.'
            if movables == 0:
                break
        print(total)





main()
main2()
