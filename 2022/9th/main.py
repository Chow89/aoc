def moveKnot(k1, k2):
    if k1['x'] > k2['x'] and k1['y'] == k2['y']:
        k2['x'] += 1
    elif k1['x'] > k2['x'] and k1['y'] > k2['y']:
        k2['x'] += 1
        k2['y'] += 1
    elif k1['x'] > k2['x'] and k1['y'] < k2['y']:
        k2['x'] += 1
        k2['y'] -= 1
    elif k1['x'] < k2['x'] and k1['y'] == k2['y']:
        k2['x'] -= 1
    elif k1['x'] < k2['x'] and k1['y'] > k2['y']:
        k2['x'] -= 1
        k2['y'] += 1
    elif k1['x'] < k2['x'] and k1['y'] < k2['y']:
        k2['x'] -= 1
        k2['y'] -= 1
    elif k1['x'] == k2['x'] and k1['y'] > k2['y']:
        k2['y'] += 1
    elif k1['x'] == k2['x'] and k1['y'] < k2['y']:
        k2['y'] -= 1

def main():
    with open('2022/9th/inputs.txt') as file:
        lines = file.readlines()
        head = {"x": 0, "y": 0}
        tail = {"x": 0, "y": 0}
        tailPositions = []
        for line in lines:
            [direction, steps] = line.strip().split(' ')
            for i in range(0, int(steps)):
                match direction:
                    case "R":
                        head['x'] += 1
                        if (head['x'] - tail['x']) > 1:
                            moveKnot(head, tail)
                    case "L":
                        head['x'] -= 1
                        if (tail['x'] - head['x']) > 1:
                            moveKnot(head, tail)
                    case "U":
                        head['y'] += 1
                        if (head['y'] - tail['y']) > 1:
                            moveKnot(head, tail)
                    case "D":
                        head['y'] -= 1
                        if (tail['y'] - head['y']) > 1:
                            moveKnot(head, tail)
                tailPositions.append(str(tail['x']) + '-' + str(tail['y']))
        print(len(set(tailPositions)))


def main2():
    with open('2022/9th/inputs.txt') as file:
        lines = file.readlines()
        head = {"x": 0, "y": 0}
        knots = [head,
                 {"x": 0, "y": 0},
                 {"x": 0, "y": 0},
                 {"x": 0, "y": 0},
                 {"x": 0, "y": 0},
                 {"x": 0, "y": 0},
                 {"x": 0, "y": 0},
                 {"x": 0, "y": 0},
                 {"x": 0, "y": 0},
                 {"x": 0, "y": 0}
                 ]
        tailPositions = []
        for line in lines:
            [direction, steps] = line.strip().split(' ')
            for i in range(0, int(steps)):
                match direction:
                    case "R":
                        head['x'] += 1
                        for k in range(0, len(knots) - 1):
                            if knots[k]['x'] - knots[k + 1]['x'] > 1 or abs(knots[k]['y'] - knots[k + 1]['y']) > 1:
                                moveKnot(knots[k], knots[k + 1])
                    case "L":
                        head['x'] -= 1
                        for k in range(0, len(knots) - 1):
                            if knots[k + 1]['x'] - knots[k]['x'] > 1 or abs(knots[k + 1]['y'] - knots[k]['y']) > 1:
                                moveKnot(knots[k], knots[k + 1])
                    case "U":
                        head['y'] += 1
                        for k in range(0, len(knots) - 1):
                            if knots[k]['y'] - knots[k + 1]['y'] > 1 or abs(knots[k]['x'] - knots[k + 1]['x']) > 1:
                                moveKnot(knots[k], knots[k + 1])
                    case "D":
                        head['y'] -= 1
                        for k in range(0, len(knots) - 1):
                            if knots[k + 1]['y'] - knots[k]['y'] > 1 or abs(knots[k + 1]['x'] - knots[k]['x']) > 1:
                                moveKnot(knots[k], knots[k + 1])
                tailPositions.append(str(knots[-1]['x']) + '-' + str(knots[-1]['y']))
        print(len(set(tailPositions)))


main()
main2()