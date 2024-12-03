import re
import functools


def main():
    with open('2024/3/inputs.txt') as file:
        lines = file.readlines()
        line = functools.reduce(lambda x, y: x + y, lines)
        instructions = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
        print(functools.reduce(lambda x, y: x + y, list(map(lambda x: int(x[0]) * int(x[1]), instructions))))


def main2():
    with open('2024/3/inputs.txt') as file:
        lines = file.readlines()
        line = functools.reduce(lambda x, y: x + y, lines)
        instructions = re.findall(r'(mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\))', line)
        enabled = True
        sum = 0
        for instruction in instructions:
            if instruction == 'do()':
                enabled = True
            elif instruction == 'don\'t()':
                enabled = False
            else:
                if enabled:
                    mul = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', instruction)[0]
                    sum += int(mul[0]) * int(mul[1])
        print(sum)


main()
main2()
