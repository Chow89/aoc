def find_next_step(data, pos):
    x, y = pos
    # check left side
    if y > 0:
        if data[x][y - 1] in ('F', 'L', '-'):
            return x, y - 1
    # check right side
    if y < len(data[x]) - 1:
        if data[x][y + 1] in ('J', '7', '-'):
            return x, y + 1
    # check top
    if x > 0:
        if data[x - 1][y] in ('F', '7', '|'):
            return x - 1, y
    # check bottom
    if x < len(data) - 1:
        if data[x + 1][y] in ('J', 'L', '|'):
            return x + 1, y


def main():
    with open('2023/10th/inputs.txt') as file:
        lines = file.readlines()
        data = []
        for line in lines:
            data.append(line.strip())
        position_s = (0, 0)
        for x in range(len(data)):
            for y in range(len(data[x])):
                if data[x][y] == 'S':
                    position_s = (x, y)
                    break
        position = find_next_step(data, position_s)
        positions = [position_s, position]
        while position != position_s:
            x, y = position
            # go down or go right
            if data[x][y] == 'F':
                # go down
                if (x + 1, y) != positions[-2]:
                    position = (x + 1, y)
                # go right
                else:
                    position = (x, y + 1)
            # go down or go left
            elif data[x][y] == '7':
                # go down
                if (x + 1, y) != positions[-2]:
                    position = (x + 1, y)
                # go left
                else:
                    position = (x, y - 1)
            # go up or go right
            elif data[x][y] == 'L':
                # go up
                if (x - 1, y) != positions[-2]:
                    position = (x - 1, y)
                # go right
                else:
                    position = (x, y + 1)
            # go up or go left
            elif data[x][y] == 'J':
                # go up
                if (x - 1, y) != positions[-2]:
                    position = (x - 1, y)
                # go left
                else:
                    position = (x, y - 1)
            # go right or left
            elif data[x][y] == '-':
                # go right
                if (x, y + 1) != positions[-2]:
                    position = (x, y + 1)
                # go left
                else:
                    position = (x, y - 1)
            elif data[x][y] == '|':
                # go up
                if (x - 1, y) != positions[-2]:
                    position = (x - 1, y)
                # go down
                else:
                    position = (x + 1, y)
            else:
                pass
            positions.append(position)
        print(len(positions) // 2)


def main2():
    with open('2023/10th/inputs.txt') as file:
        lines = file.readlines()


main()
main2()
