def main():
    with open('2023/11th/inputs.txt') as file:
        lines = file.readlines()
        data = []
        for row in lines:
            row = row.strip()
            data.append(row)
            if len(list(filter(lambda x: x == '.', row))) == len(row):
                data.append(row)
        transposed_data = list(zip(*data))
        data = []
        for row in transposed_data:
            data.append(row)
            if len(list(filter(lambda x: x == '.', row))) == len(row):
                data.append(row)
        data = list(zip(*data))
        positions = []
        for x in range(len(data)):
            for y in range(len(data[x])):
                if data[x][y] == '#':
                    positions.append((x, y))
        result = 0
        for i in range(len(positions)):
            for j in range (i + 1, len(positions)):
                result += abs(positions[i][0] - positions[j][0]) + abs(positions[i][1] - positions[j][1])
        print(result)


def main2():
    with open('2023/11th/inputs.txt') as file:
        lines = file.readlines()


main()
main2()
