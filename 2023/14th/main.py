import copy


def rollN(grid, x, y):
    if x != 0 and grid[x-1][y] == '.':
        grid[x][y] = '.'
        grid[x-1][y] = 'O'
        rollN(grid, x-1, y)


def rollW(grid, x, y):
    if y != 0 and grid[x][y - 1] == '.':
        grid[x][y] = '.'
        grid[x][y - 1] = 'O'
        rollW(grid, x, y - 1)


def rollS(grid, x, y):
    if x != len(grid)-1 and grid[x+1][y] == '.':
        grid[x][y] = '.'
        grid[x+1][y] = 'O'
        rollS(grid, x+1, y)


def rollE(grid, x, y):
    if y != len(grid[x])-1 and grid[x][y+1] == '.':
        grid[x][y] = '.'
        grid[x][y+1] = 'O'
        rollE(grid, x, y+1)


def rollNorth(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == 'O':
                rollN(grid, x, y)


def rollSouth(grid):
    for x in range(len(grid) - 1, -1, -1):
        for y in range(len(grid[x])):
            if grid[x][y] == 'O':
                rollS(grid, x, y)


def rollWest(grid):
    for y in range(len(grid[0])):
        for x in range(len(grid)):
            if grid[x][y] == 'O':
                rollW(grid, x, y)


def rollEast(grid):
    for y in range(len(grid[0]) - 1, -1, -1):
        for x in range(len(grid)):
            if grid[x][y] == 'O':
                rollE(grid, x, y)


def main():
    with open('2023/14th/inputs.txt') as file:
        grid = list(map(list, file.read().split()))
        rollNorth(grid)

        result = 0
        rows = len(grid)
        for line in grid:
            result += line.count('O') * rows
            rows -= 1
        print(result)


def main2():
    with open('2023/14th/inputs.txt') as file:
        grid = list(map(list, file.read().split()))
        cycles = 1000000000
        seen = []
        grids = []

        for i in range(cycles):
            rollNorth(grid)
            rollWest(grid)
            rollSouth(grid)
            rollEast(grid)
            if grid in seen:
                break
            seen.append(copy.deepcopy(grid))
            grids.append(copy.deepcopy(grid))

        first_seen = grids.index(grid)
        cycle_length = len(grids) - first_seen
        grid = grids[(1000000000 - first_seen) % cycle_length]

        result = 0
        rows = len(grid)
        for line in grid:
            result += line.count('O') * rows
            rows -= 1
        print(result)



main()
main2()
