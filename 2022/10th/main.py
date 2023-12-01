def main():
    with open('2022/10th/inputs.txt') as file:
        lines = file.readlines()
        cycle = 0
        register = 1
        sum = 0
        for line in lines:
            if line.startswith('noop'):
                cycle += 1
                if (cycle - 20) % 40 == 0:
                    sum += cycle * register
            else:
                cycle += 1
                if (cycle - 20) % 40 == 0:
                    sum += cycle * register
                cycle += 1
                if (cycle - 20) % 40 == 0:
                    sum += cycle * register
                value = int(line.strip().split(' ')[1])
                register += value
        print(sum)


def main2():
    with open('2022/10th/inputs.txt') as file:
        lines = file.readlines()
        cycle = 0
        register = 1
        output = ''
        for line in lines:
            if line.startswith('noop'):
                cycle %= 40
                cycle += 1
                if cycle - 1 in [register - 1, register, register + 1]:
                    output += '#'
                else:
                    output += '.'
            else:
                cycle %= 40
                cycle += 1
                if cycle - 1 in [register - 1, register, register + 1]:
                    output += '#'
                else:
                    output += '.'
                cycle %= 40
                cycle += 1
                if cycle - 1 in [register - 1, register, register + 1]:
                    output += '#'
                else:
                    output += '.'
                value = int(line.strip().split(' ')[1])
                register += value

        for row in range(0, 6):
            start = row * 40
            print(output[start:start + 40])

main()
main2()
