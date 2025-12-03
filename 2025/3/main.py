def main():
    with open('2025/3/inputs.txt') as file:
        lines = file.readlines()
        sum = 0
        for line in lines:
            highestNumber = max(map(int, list(line.strip()[:-1])))
            firstPosition = line.index(str(highestNumber))
            highestNumberBehind = max(map(int, line.strip()[firstPosition + 1:]))
            sum += int(str(highestNumber) + str(highestNumberBehind))
        print(sum)



def main2():
    with open('2025/3/inputs.txt') as file:
        lines = list(map(lambda l: l.strip(), file.readlines()))
        sum = 0
        for line in lines:
            highestNumber = ''
            position = 0
            for o in range(0, 12):
                windowStart = max(o, position)
                windowEnd = len(line) - 12 + len(highestNumber) + 1
                currentNumber = 0
                for i in range(windowStart, windowEnd):
                    if int(line[i]) > currentNumber:
                        currentNumber = int(line[i])
                highestNumber = highestNumber + str(currentNumber)
                position = line.index(str(currentNumber), windowStart) + 1
            sum += int(highestNumber)
        print(sum)






main()
main2()
