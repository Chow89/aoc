def main():
    with open('4th/inputs.txt') as file:
        lines = file.readlines()
        i = 0
        for line in lines:
            [first, second] = line.split(',')
            [firstStart,firstEnd] = first.split('-')
            [secondStart,secondEnd] = second.split('-')
            if (int(firstStart) >= int(secondStart) and int(firstEnd) <= int(secondEnd)) or (int(firstStart) <= int(secondStart) and int(firstEnd) >= int(secondEnd)):
                i += 1
        print(i)

def main2():
    with open('4th/inputs.txt') as file:
        lines = file.readlines()
        i = 0
        for line in lines:
            [first, second] = line.split(',')
            [firstStart,firstEnd] = first.split('-')
            [secondStart,secondEnd] = second.split('-')
            if (int(firstEnd) >= int(secondStart) and int(firstStart) <= int(secondEnd)) or (int(secondEnd) >= int(firstStart) and int(secondStart) <= int(firstEnd)):
                i += 1
        print(i)


main()
main2()