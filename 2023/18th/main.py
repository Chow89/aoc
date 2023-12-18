def main():
    with open('2023/18th/inputs.txt') as file:
        lines = file.readlines()
        positions = [(0, 0)]
        for line in lines:
            direction, distance, _ = list(map(lambda x: x.strip(), line.split(' ')))
            for step in range(int(distance)):
                current_position = positions[-1]
                if direction == 'R':
                    positions.append((current_position[0] + 1, current_position[1]))
                elif direction == 'L':
                    positions.append((current_position[0] - 1, current_position[1]))
                elif direction == 'U':
                    positions.append((current_position[0], current_position[1] - 1))
                elif direction == 'D':
                    positions.append((current_position[0], current_position[1] + 1))
        positions = set(positions)
        max_x = max(positions, key=lambda x: x[0])[0]
        min_x = min(positions, key=lambda x: x[0])[0]
        max_y = max(positions, key=lambda x: x[1])[1]
        min_y = min(positions, key=lambda x: x[1])[1]
        result = len(positions)
        next = [(1, 1)]     # assumeing that (1, 1) is always in the grid
        seen = set()
        while len(next) > 0:
            x, y = next.pop()
            seen.add((x, y))
            if (x + 1, y) not in positions and (x + 1, y) not in seen and x + 1 <= max_x:
                next.append((x + 1, y))
            if (x - 1, y) not in positions and (x - 1, y) not in seen and x - 1 >= min_x:
                next.append((x - 1, y))
            if (x, y + 1) not in positions and (x, y + 1) not in seen and y + 1 <= max_y:
                next.append((x, y + 1))
            if (x, y - 1) not in positions and (x, y - 1) not in seen and y - 1 >= min_y:
                next.append((x, y - 1))

        result += len(seen)
        print(result)


def main2():
    with open('2023/18th/inputs.txt') as file:
        lines = file.readlines()
        positions = [(0, 0)]
        for line in lines:
            _, _, color = line.split(' ')
            color = color.strip()[2:-1]
            distance = int(color[:5], 16)
            direction = color[5:]
            for step in range(int(distance)):
                current_position = positions[-1]
                if direction == '0':
                    positions.append((current_position[0] + 1, current_position[1]))
                elif direction == '2':
                    positions.append((current_position[0] - 1, current_position[1]))
                elif direction == '3':
                    positions.append((current_position[0], current_position[1] - 1))
                elif direction == '1':
                    positions.append((current_position[0], current_position[1] + 1))
        positions = set(positions)
        max_x = max(positions, key=lambda x: x[0])[0]
        min_x = min(positions, key=lambda x: x[0])[0]
        max_y = max(positions, key=lambda x: x[1])[1]
        min_y = min(positions, key=lambda x: x[1])[1]
        result = len(positions)
        next = [(1, 1)]  # assumeing that (1, 1) is always in the grid
        seen = set()
        while len(next) > 0:
            x, y = next.pop()
            seen.add((x, y))
            if (x + 1, y) not in positions and (x + 1, y) not in seen and x + 1 <= max_x:
                next.append((x + 1, y))
            if (x - 1, y) not in positions and (x - 1, y) not in seen and x - 1 >= min_x:
                next.append((x - 1, y))
            if (x, y + 1) not in positions and (x, y + 1) not in seen and y + 1 <= max_y:
                next.append((x, y + 1))
            if (x, y - 1) not in positions and (x, y - 1) not in seen and y - 1 >= min_y:
                next.append((x, y - 1))

        result += len(seen)
        print(result)


main()
main2()
