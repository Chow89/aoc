def main():
    with open('3rd/inputs.txt') as file:
        lines = file.readlines()
        itemTypes = [];
        for line in lines:
            halfLength = int(len(line.strip()) / 2)
            first, second = line[:halfLength], line[halfLength:]
            for letter in first:
                if letter in second:
                    itemTypes.append(letter)
                    break
        sum = 0
        for char in itemTypes:
            if ord(char) >= 97:
                sum += ord(char) - 96
            else:
                sum += ord(char) - 38
        print(sum)

def main2():
    with open('3rd/inputs.txt') as file:
        lines = file.readlines()
        groups = int(len(lines) / 3)
        itemTypes = [];
        for i in range(0, groups):
            startLine = i * 3
            first = lines[startLine]
            second = lines[startLine + 1]
            third = lines[startLine + 2]
            for letter in first:
                if letter in second and letter in third:
                    itemTypes.append(letter)
                    break
        sum = 0
        for char in itemTypes:
            if ord(char) >= 97:
                sum += ord(char) - 96
            else:
                sum += ord(char) - 38
        print(sum)

main()
main2()