def is_mirrored(grid, x1, x2):
    if grid[x1] == grid[x2]:
        if x1 > 0 and x2 < len(grid) - 1:
            return is_mirrored(grid, x1 - 1, x2 + 1)
        else:
            return True
    return False


def is_mirrored2(grid, x1, x2, errors):
    for c in range(len(grid[x1])):
        if grid[x1][c] != grid[x2][c]:
            errors += 1

    if errors <= 1:
        if x1 > 0 and x2 < len(grid) - 1:
            return is_mirrored2(grid, x1 - 1, x2 + 1, errors)
        else:
            return errors == 1
    return False


def main():
    with open('2023/13th/inputs.txt') as file:
        result = 0
        blocks = file.read().split('\n\n')
        for grid in blocks:
            grid = grid.split('\n')
            mirrored_row = 0
            for i in range(1, len(grid)):
                if is_mirrored(grid, i - 1, i):
                    mirrored_row = i
                    break
            grid = list(zip(*grid))
            mirrored_col = 0
            for i in range(1, len(grid)):
                if is_mirrored(grid, i - 1, i):
                    mirrored_col = i
                    break
            result += 100 * mirrored_row + mirrored_col
        print(result)


def main2():
    with open('2023/13th/inputs.txt') as file:
        result = 0
        blocks = file.read().split('\n\n')
        for grid in blocks:
            grid = grid.split('\n')
            mirrored_row = 0
            for i in range(1, len(grid)):
                if is_mirrored2(grid, i - 1, i, 0):
                    mirrored_row = i
                    break

            mirrored_col = 0
            if mirrored_row == 0:
                grid = list(zip(*grid))
                for i in range(1, len(grid)):
                    if is_mirrored2(grid, i - 1, i, 0):
                        mirrored_col = i
                        break
            result += 100 * mirrored_row + mirrored_col
        print(result)


main()
main2()
