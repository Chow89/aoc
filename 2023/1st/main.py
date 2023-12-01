import re
import functools

def main():
    with open('2023/1st/inputs.txt') as file:
        lines = file.readlines()
        numbers = []
        for line in lines:
            linenumbers = []
            for char in line:
                if char.isdigit():
                    linenumbers.append(char)
            numbers.append(linenumbers[0] + linenumbers[-1])
        print(functools.reduce(lambda a, b: int(a) + int(b), numbers))


def main2():
    with open('2023/1st/inputs.txt') as file:
        lines = file.readlines()
        numbers = []
        for line in lines:
            linenumbers = []
            for i in range(0, len(line)):
                if line[i].isdigit():
                    linenumbers.append(line[i])
                if line[i:].startswith('one'):
                    linenumbers.append('1')
                if line[i:].startswith('two'):
                    linenumbers.append('2')
                if line[i:].startswith('three'):
                    linenumbers.append('3')
                if line[i:].startswith('four'):
                    linenumbers.append('4')
                if line[i:].startswith('five'):
                    linenumbers.append('5')
                if line[i:].startswith('six'):
                    linenumbers.append('6')
                if line[i:].startswith('seven'):
                    linenumbers.append('7')
                if line[i:].startswith('eight'):
                    linenumbers.append('8')
                if line[i:].startswith('nine'):
                    linenumbers.append('9')
            numbers.append(linenumbers[0] + linenumbers[-1])
        print(functools.reduce(lambda a, b: int(a) + int(b), numbers))


main()
main2()