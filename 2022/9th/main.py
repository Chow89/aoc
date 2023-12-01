def main():
    with open('2022/9th/inputs.txt') as file:
        lines = file.readlines()
        head = {"x": 0, "y": 0}
        tail = {"x": 0, "y": 0}
        tailPositions = ['0-0']
        for line in lines:
            [direction, steps] = line.strip().split(' ')
            for i in range(0, int(steps)):
                match direction:
                    case "R":
                        head['x'] += 1
                        if (head['x'] - tail['x']) > 1:
                            tail['x'] += 1
                            if head['y'] > tail['y']:
                                tail['y'] += 1
                            elif head['y'] < tail['y']:
                                tail['y'] -= 1
                            tailPositions.append(str(tail['x']) + '-' + str(tail['y']))
                    case "L":
                        head['x'] -= 1
                        if (tail['x'] - head['x']) > 1:
                            tail['x'] -= 1
                            if head['y'] > tail['y']:
                                tail['y'] += 1
                            elif head['y'] < tail['y']:
                                tail['y'] -= 1
                            tailPositions.append(str(tail['x']) + '-' + str(tail['y']))
                    case "U":
                        head['y'] += 1
                        if (head['y'] - tail['y']) > 1:
                            tail['y'] += 1
                            if head['x'] > tail['x']:
                                tail['x'] += 1
                            elif head['x'] < tail['x']:
                                tail['x'] -= 1
                            tailPositions.append(str(tail['x']) + '-' + str(tail['y']))
                    case "D":
                        head['y'] -= 1
                        if (tail['y'] - head['y']) > 1:
                            tail['y'] -= 1
                            if head['x'] > tail['x']:
                                tail['x'] += 1
                            elif head['x'] < tail['x']:
                                tail['x'] -= 1
                            tailPositions.append(str(tail['x']) + '-' + str(tail['y']))
        print(len(set(tailPositions)))


def main2():
    with open('2022/9th/inputs.txt') as file:
        lines = file.readlines()
        for line in lines:
            pass


main()
main2()