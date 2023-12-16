def main():
    with open('2023/16th/inputs.txt') as file:
        seen = []
        next = [(0, 0, 'l')]
        grid = list(map(list, file.read().split()))
        while len(next) > 0:
            x, y, src_direction = next.pop(0)
            seen.append((x, y, src_direction))
            if grid[y][x] == '.':
                if src_direction == 'l' and x < len(grid[y]) - 1:
                    if (x + 1, y, 'l') not in seen:
                        next.append((x + 1, y, 'l'))
                elif src_direction == 'r' and x > 0:
                    if (x - 1, y, 'r') not in seen:
                        next.append((x - 1, y, 'r'))
                elif src_direction == 'u' and y < len(grid) - 1:
                    if (x, y + 1, 'u') not in seen:
                        next.append((x, y + 1, 'u'))
                elif src_direction == 'd' and y > 0:
                    if (x, y - 1, 'd') not in seen:
                        next.append((x, y - 1, 'd'))
            elif grid[y][x] == '/':
                if src_direction == 'l' and y > 0:
                    if (x, y - 1, 'd') not in seen:
                        next.append((x, y - 1, 'd'))
                elif src_direction == 'r' and y < len(grid) - 1:
                    if (x, y + 1, 'u') not in seen:
                        next.append((x, y + 1, 'u'))
                elif src_direction == 'u' and x > 0:
                    if (x - 1, y, 'r') not in seen:
                        next.append((x - 1, y, 'r'))
                elif src_direction == 'd' and x < len(grid[y]) - 1:
                    if (x + 1, y, 'l') not in seen:
                        next.append((x + 1, y, 'l'))
            elif grid[y][x] == '\\':
                if src_direction == 'l' and y < len(grid) - 1:
                    if (x, y + 1, 'u') not in seen:
                        next.append((x, y + 1, 'u'))
                elif src_direction == 'r' and y > 0:
                    if (x, y - 1, 'd') not in seen:
                        next.append((x, y - 1, 'd'))
                elif src_direction == 'u' and x < len(grid[y]) - 1:
                    if (x + 1, y, 'l') not in seen:
                        next.append((x + 1, y, 'l'))
                elif src_direction == 'd' and x > 0:
                    if (x - 1, y, 'r') not in seen:
                        next.append((x - 1, y, 'r'))
            elif grid[y][x] == '-':
                if src_direction == 'l' and x < len(grid[y]) - 1:
                    if (x + 1, y, 'l') not in seen:
                        next.append((x + 1, y, 'l'))
                elif src_direction == 'r' and x > 0:
                    if (x - 1, y, 'r') not in seen:
                        next.append((x - 1, y, 'r'))
                elif src_direction in 'du':
                    if x < len(grid[y]) - 1:
                        if (x + 1, y, 'l') not in seen:
                            next.append((x + 1, y, 'l'))
                    if x > 0:
                        if (x - 1, y, 'r') not in seen:
                            next.append((x - 1, y, 'r'))
            elif grid[y][x] == '|':
                if src_direction == 'd' and y > 0:
                    if (x, y - 1, 'd') not in seen:
                        next.append((x, y - 1, 'd'))
                elif src_direction == 'u' and y < len(grid) - 1:
                    if (x, y + 1, 'u') not in seen:
                        next.append((x, y + 1, 'u'))
                elif src_direction in 'rl':
                    if y < len(grid) - 1:
                        if (x, y + 1, 'u') not in seen:
                            next.append((x, y + 1, 'u'))
                    if y > 0:
                        if (x, y - 1, 'd') not in seen:
                            next.append((x, y - 1, 'd'))

        seen = list(map(lambda x: (x[0], x[1]), seen))
        print(len(set(seen)))


def main2():
    with open('2023/16th/inputs.txt') as file:
        grid = list(map(list, file.read().split()))
        starting_points = []
        for x in range(len(grid[0])):
            starting_points.append((x, 0, 'u'))
            starting_points.append((x, len(grid) - 1, 'd'))
        for y in range(len(grid)):
            starting_points.append((0, y, 'l'))
            starting_points.append((len(grid[0]) - 1, y, 'r'))

        m = 0
        for starting_point in starting_points:
            seen = []
            next = [starting_point]
            while len(next) > 0:
                x, y, src_direction = next.pop(0)
                seen.append((x, y, src_direction))
                if grid[y][x] == '.':
                    if src_direction == 'l' and x < len(grid[y]) - 1:
                        if (x + 1, y, 'l') not in seen:
                            next.append((x + 1, y, 'l'))
                    elif src_direction == 'r' and x > 0:
                        if (x - 1, y, 'r') not in seen:
                            next.append((x - 1, y, 'r'))
                    elif src_direction == 'u' and y < len(grid) - 1:
                        if (x, y + 1, 'u') not in seen:
                            next.append((x, y + 1, 'u'))
                    elif src_direction == 'd' and y > 0:
                        if (x, y - 1, 'd') not in seen:
                            next.append((x, y - 1, 'd'))
                elif grid[y][x] == '/':
                    if src_direction == 'l' and y > 0:
                        if (x, y - 1, 'd') not in seen:
                            next.append((x, y - 1, 'd'))
                    elif src_direction == 'r' and y < len(grid) - 1:
                        if (x, y + 1, 'u') not in seen:
                            next.append((x, y + 1, 'u'))
                    elif src_direction == 'u' and x > 0:
                        if (x - 1, y, 'r') not in seen:
                            next.append((x - 1, y, 'r'))
                    elif src_direction == 'd' and x < len(grid[y]) - 1:
                        if (x + 1, y, 'l') not in seen:
                            next.append((x + 1, y, 'l'))
                elif grid[y][x] == '\\':
                    if src_direction == 'l' and y < len(grid) - 1:
                        if (x, y + 1, 'u') not in seen:
                            next.append((x, y + 1, 'u'))
                    elif src_direction == 'r' and y > 0:
                        if (x, y - 1, 'd') not in seen:
                            next.append((x, y - 1, 'd'))
                    elif src_direction == 'u' and x < len(grid[y]) - 1:
                        if (x + 1, y, 'l') not in seen:
                            next.append((x + 1, y, 'l'))
                    elif src_direction == 'd' and x > 0:
                        if (x - 1, y, 'r') not in seen:
                            next.append((x - 1, y, 'r'))
                elif grid[y][x] == '-':
                    if src_direction == 'l' and x < len(grid[y]) - 1:
                        if (x + 1, y, 'l') not in seen:
                            next.append((x + 1, y, 'l'))
                    elif src_direction == 'r' and x > 0:
                        if (x - 1, y, 'r') not in seen:
                            next.append((x - 1, y, 'r'))
                    elif src_direction in 'du':
                        if x < len(grid[y]) - 1:
                            if (x + 1, y, 'l') not in seen:
                                next.append((x + 1, y, 'l'))
                        if x > 0:
                            if (x - 1, y, 'r') not in seen:
                                next.append((x - 1, y, 'r'))
                elif grid[y][x] == '|':
                    if src_direction == 'd' and y > 0:
                        if (x, y - 1, 'd') not in seen:
                            next.append((x, y - 1, 'd'))
                    elif src_direction == 'u' and y < len(grid) - 1:
                        if (x, y + 1, 'u') not in seen:
                            next.append((x, y + 1, 'u'))
                    elif src_direction in 'rl':
                        if y < len(grid) - 1:
                            if (x, y + 1, 'u') not in seen:
                                next.append((x, y + 1, 'u'))
                        if y > 0:
                            if (x, y - 1, 'd') not in seen:
                                next.append((x, y - 1, 'd'))

            seen = list(map(lambda x: (x[0], x[1]), seen))
            result = len(set(seen))
            m = max(result, m)
        print(m)

main()
main2()
