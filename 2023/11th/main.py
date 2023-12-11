def main():
    with open('2023/11th/inputs.txt') as file:
        lines = file.readlines()
        empty_rows = []
        empty_cols = []
        for row in range(len(lines)):
            r = lines[row].strip()
            if len(list(filter(lambda x: x == '.', r))) == len(r):
                empty_rows.append(row)
        transposed_data = list(zip(*lines))
        for col in range(len(transposed_data)):
            c = transposed_data[col]
            if len(list(filter(lambda x: x == '.', c))) == len(c):
                empty_cols.append(col)
        positions = []
        for x in range(len(lines)):
            for y in range(len(lines[x])):
                if lines[x][y] == '#':
                    expanded_x = x + len(list(filter(lambda a: a < x, empty_rows)))
                    expanded_y = y + len(list(filter(lambda a: a < y, empty_cols)))
                    positions.append((expanded_x, expanded_y))
        result = 0
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                result += abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1])
        print(result)


def main2():
    with open('2023/11th/inputs.txt') as file:
        lines = file.readlines()
        empty_rows = []
        empty_cols = []
        for row in range(len(lines)):
            r = lines[row].strip()
            if len(list(filter(lambda x: x == '.', r))) == len(r):
                empty_rows.append(row)
        transposed_data = list(zip(*lines))
        for col in range(len(transposed_data)):
            c = transposed_data[col]
            if len(list(filter(lambda x: x == '.', c))) == len(c):
                empty_cols.append(col)
        positions = []
        for x in range(len(lines)):
            for y in range(len(lines[x])):
                if lines[x][y] == '#':
                    expanded_x = x + (999999 * len(list(filter(lambda a: a < x, empty_rows))))
                    expanded_y = y + (999999 * len(list(filter(lambda a: a < y, empty_cols))))
                    positions.append((expanded_x, expanded_y))
        result = 0
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                result += abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1])
        print(result)


main()
main2()
