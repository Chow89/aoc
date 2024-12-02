def main():
    with open('2024/2/inputs.txt') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            values = list(map(int, line.strip().split(' ')))
            increasing = True
            decreasing = True
            difference = True
            for i in range(len(values) - 1):
                if values[i] > values[i + 1]:
                    increasing = False
                if values[i] < values[i + 1]:
                    decreasing = False
                if not(1 <= abs(values[i] - values[i + 1]) <= 3):
                    difference = False
            if (increasing or decreasing) and difference:
                count += 1
        print(count)


def main2():
    with open('2024/2/inputs.txt') as file:
        lines = file.readlines()
        count = 0
        for line in lines:
            values = list(map(int, line.strip().split(' ')))
            lists = [values, values[1:]]
            for i in range(1, len(values)):
                lists.append(values[:i] + values[i + 1:])
            safe = False
            for l in lists:
                increasing = True
                decreasing = True
                difference = True
                for i in range(len(l) - 1):
                    if l[i] > l[i + 1]:
                        increasing = False
                    if l[i] < l[i + 1]:
                        decreasing = False
                    if not (1 <= abs(l[i] - l[i + 1]) <= 3):
                        difference = False
                if (increasing or decreasing) and difference:
                    safe = True
            if safe:
                count += 1
        print(count)


main()
main2()
