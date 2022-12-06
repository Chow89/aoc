def main():
    with open('6th/inputs.txt') as file:
        line = file.readlines()[0]
        for i in range(0, len(line)):
            if len(set(line[i:i + 4])) == len(line[i:i + 4]):
                print(i + 4)
                break


def main2():
    with open('6th/inputs.txt') as file:
        line = file.readlines()[0]
        for i in range(0, len(line)):
            if len(set(line[i:i + 14])) == len(line[i:i + 14]):
                print(i + 14)
                break


main()
main2()