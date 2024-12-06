def findPath(guard_positions, area, obstructions):
    out_of_area = False
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    while not out_of_area:
        current_guard_position = guard_positions[-1]
        direction = directions[0]
        if current_guard_position[0] < 0 or current_guard_position[0] >= len(area) or current_guard_position[1] < 0 or \
                current_guard_position[1] >= len(area[0]):
            guard_positions = guard_positions[:-1]
            out_of_area = True
        elif (current_guard_position[0] + direction[0], current_guard_position[1] + direction[1]) in obstructions:
            directions = directions[1:] + directions[:1]
        else:
            guard_positions.append((current_guard_position[0] + direction[0], current_guard_position[1] + direction[1]))
    return guard_positions

def main():
    with open('2024/6/inputs.txt') as file:
        area = list(map(lambda x: x.strip(), file.readlines()))
        obstructions = []
        guard_positions = []
        for i in range(len(area)):
            for j in range(len(area[i])):
                if area[i][j] == '#':
                    obstructions.append((i, j))
                if area[i][j] == '^':
                    guard_positions.append((i, j))
        guard_positions = findPath(guard_positions, area, obstructions)
        print(len(set(guard_positions)))


def main2():
    with open('2024/6/inputs.txt') as file:
        area = list(map(lambda x: x.strip(), file.readlines()))
        loop_obstructions = []
        obstructions = []
        start_position = None
        for i in range(len(area)):
            for j in range(len(area[i])):
                if area[i][j] == '#':
                    obstructions.append((i, j))
                if area[i][j] == '^':
                    start_position = (i, j, -1, 0)

        guard_positions = findPath([(start_position[0], start_position[1])], area, obstructions)
        guard_positions = set(filter(lambda x: (x[0], x[1]) != (start_position[0], start_position[1]), guard_positions))

        for position in guard_positions:
            path = [start_position]
            out_of_area = False
            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            while not out_of_area:
                direction = directions[0]
                current_guard_position = (path[-1][0], path[-1][1], direction[0], direction[1])
                if current_guard_position[0] < 0 or current_guard_position[0] >= len(area) or current_guard_position[1] < 0 or current_guard_position[1] >= len(area[0]):
                    path = path[:-1]
                    out_of_area = True
                elif (current_guard_position[0] + direction[0], current_guard_position[1] + direction[1]) in obstructions + [position]:
                    directions = directions[1:] + directions[:1]
                elif (current_guard_position[0] + direction[0], current_guard_position[1] + direction[1], direction[0], direction[1]) in path:
                    loop_obstructions.append(position)
                    break
                else:
                    path.append((current_guard_position[0] + direction[0], current_guard_position[1] + direction[1], direction[0], direction[1]))
        print(len(set(loop_obstructions)))


main()
main2()
