import functools


def is_adjacent(grid, row, column):
    # check top left (-1, -1)
    if row > 0 and column > 0:
        if not grid[row - 1][column - 1].isdigit() and grid[row - 1][column - 1] != '.':
            return True
    # check top center (0, -1)
    if row > 0:
        if not grid[row - 1][column].isdigit() and grid[row - 1][column] != '.':
            return True
    # check top right (1, -1)
    if row > 0 and column < len(grid[row]) - 1:
        if not grid[row - 1][column + 1].isdigit() and grid[row - 1][column + 1] != '.':
            return True
    # check center left (-1, 0)
    if column > 0:
        if not grid[row][column - 1].isdigit() and grid[row][column - 1] != '.':
            return True
    # check center right (1, 0)
    if column < len(grid[row]) - 1:
        if not grid[row][column + 1].isdigit() and grid[row][column + 1] != '.':
            return True
    # check bottom left (-1, 1)
    if row < len(grid) - 1 and column > 0:
        if not grid[row + 1][column - 1].isdigit() and grid[row + 1][column - 1] != '.':
            return True
    # check bottom center (0, 1)
    if row < len(grid) - 1:
        if not grid[row + 1][column].isdigit() and grid[row + 1][column] != '.':
            return True
    # check bottom right (1, 1)
    if row < len(grid) - 1 and column < len(grid[row]) - 1:
        if not grid[row + 1][column + 1].isdigit() and grid[row + 1][column + 1] != '.':
            return True
    return False


def find_adjacent_gear(grid, row, column):
    # check top left (-1, -1)
    if row > 0 and column > 0:
        if grid[row - 1][column - 1] == '*':
            return [row - 1, column - 1]
    # check top center (0, -1)
    if row > 0:
        if grid[row - 1][column] == '*':
            return [row - 1, column]
    # check top right (1, -1)
    if row > 0 and column < len(grid[row]) - 1:
        if grid[row - 1][column + 1] == '*':
            return [row - 1, column + 1]
    # check center left (-1, 0)
    if column > 0:
        if grid[row][column - 1] == '*':
            return [row, column - 1]
    # check center right (1, 0)
    if column < len(grid[row]) - 1:
        if grid[row][column + 1] == '*':
            return [row, column + 1]
    # check bottom left (-1, 1)
    if row < len(grid) - 1 and column > 0:
        if grid[row + 1][column - 1] == '*':
            return [row + 1, column - 1]
    # check bottom center (0, 1)
    if row < len(grid) - 1:
        if grid[row + 1][column] == '*':
            return [row + 1, column]
    # check bottom right (1, 1)
    if row < len(grid) - 1 and column < len(grid[row]) - 1:
        if grid[row + 1][column + 1] == '*':
            return [row + 1, column + 1]
    return []


def main():
    with open('2023/3rd/inputs.txt') as file:
        lines = file.readlines()
        numbers = []
        grid = []
        for line in lines:
            grid.append(line.strip() + '.')
        for row in range(len(grid)):
            current_string = ''
            is_current_number_adjacent = False
            for column in range(len(grid[row])):
                if grid[row][column].isdigit():
                    current_string += grid[row][column]
                    if is_adjacent(grid, row, column):
                        is_current_number_adjacent = True
                    if column == len(grid[row]) - 1:
                        numbers.append(int(current_string))
                else:
                    if current_string != '' and is_current_number_adjacent:
                        numbers.append(int(current_string))
                    is_current_number_adjacent = False
                    current_string = ''
        print(functools.reduce(lambda a, b: a + b, numbers))


def main2():
    with open('2023/3rd/inputs.txt') as file:
        lines = file.readlines()
        numbers = {}
        grid = []
        for line in lines:
            grid.append(line.strip() + '.')
        for row in range(len(grid)):
            current_string = ''
            is_current_number_adjacent = False
            number_gear_position = []
            for column in range(len(grid[row])):
                if grid[row][column].isdigit():
                    current_string += grid[row][column]
                    current_gear_position = find_adjacent_gear(grid, row, column)
                    if len(current_gear_position) > 0:
                        is_current_number_adjacent = True
                        number_gear_position = current_gear_position
                    if column == len(grid[row]) - 1 and len(number_gear_position) > 0:
                        key = str(number_gear_position[0]) + '.' + str(number_gear_position[1])
                        if key in numbers:
                            numbers[key].append(int(current_string))
                        else:
                            numbers[key] = [int(current_string)]
                else:
                    if current_string != '' and is_current_number_adjacent and len(number_gear_position) > 0:
                        key = str(number_gear_position[0]) + '.' + str(number_gear_position[1])
                        if key in numbers:
                            numbers[key].append(int(current_string))
                        else:
                            numbers[key] = [int(current_string)]
                    is_current_number_adjacent = False
                    current_string = ''
        result = 0
        for key in numbers:
            if len(numbers[key]) == 2:
                result += (numbers[key][0] * numbers[key][1])
        print(result)


main()
main2()
