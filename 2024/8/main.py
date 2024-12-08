def add_to_dict(symbol_map, i, j, value):
    if value not in symbol_map:
        symbol_map[value] = [(i, j)]
    else:
        symbol_map[value].append((i, j))

def main():
    with open('2024/8/inputs.txt') as file:
        grid = list(map(lambda x: x.strip(), file.readlines()))
        symbol_map = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != '.':
                    add_to_dict(symbol_map, i, j, grid[i][j])
        antinodes = set()
        for key in symbol_map:
            for i in range(len(symbol_map[key])):
                for j in range(i + 1, len(symbol_map[key])):
                    dx = symbol_map[key][i][0] - symbol_map[key][j][0]
                    dy = symbol_map[key][i][1] - symbol_map[key][j][1]
                    antinodes.add((symbol_map[key][i][0] + dx, symbol_map[key][i][1] + dy))
                    antinodes.add((symbol_map[key][j][0] - dx, symbol_map[key][j][1] - dy))
        antinodes = list(filter(lambda x: 0 <= x[0] < len(grid) and 0 <= x[1] < len(grid[0]), antinodes))
        print(len(antinodes))


def main2():
    with open('2024/8/inputs.txt') as file:
        grid = list(map(lambda x: x.strip(), file.readlines()))
        symbol_map = {}
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] != '.':
                    add_to_dict(symbol_map, i, j, grid[i][j])
        antinodes = set()
        for key in symbol_map:
            for i in range(len(symbol_map[key])):
                for j in range(i + 1, len(symbol_map[key])):
                    antinodes.add((symbol_map[key][i][0], symbol_map[key][i][1]))
                    antinodes.add((symbol_map[key][j][0], symbol_map[key][j][1]))
                    original_dx = symbol_map[key][i][0] - symbol_map[key][j][0]
                    original_dy = symbol_map[key][i][1] - symbol_map[key][j][1]
                    dx = original_dx
                    dy = original_dy
                    while True:
                        if 0 <= symbol_map[key][i][0] + dx < len(grid) and 0 <= symbol_map[key][i][1] + dy < len(grid[0]):
                            antinodes.add((symbol_map[key][i][0] + dx, symbol_map[key][i][1] + dy))
                            dx += original_dx
                            dy += original_dy
                        else:
                            break
                    dx = original_dx
                    dy = original_dy
                    while True:
                        if 0 <= symbol_map[key][j][0] - dx < len(grid) and 0 <= symbol_map[key][j][1] - dy < len(grid[0]):
                            antinodes.add((symbol_map[key][j][0] - dx, symbol_map[key][j][1] - dy))
                            dx += original_dx
                            dy += original_dy
                        else:
                            break

        print(len(antinodes))


main()
main2()
