def main():
    with open('2022/2nd/inputs.txt') as file:
        lines = file.readlines()
        sum = 0
        for line in lines:
            match line.strip():
                case "A X":
                    sum += 1 + 3
                case "A Y":
                    sum += 2 + 6
                case "A Z":
                    sum += 3 + 0
                case "B X":
                    sum += 1 + 0
                case "B Y":
                    sum += 2 + 3
                case "B Z":
                    sum += 3 + 6
                case "C X":
                    sum += 1 + 6
                case "C Y":
                    sum += 2 + 0
                case "C Z":
                    sum += 3 + 3
        print(sum)

def main2():
    with open('2022/2nd/inputs.txt') as file:
        lines = file.readlines()
        sum = 0
        for line in lines:
            match line.strip():
                case "A X":
                    sum += 3 + 0
                case "A Y":
                    sum += 1 + 3
                case "A Z":
                    sum += 2 + 6
                case "B X":
                    sum += 1 + 0
                case "B Y":
                    sum += 2 + 3
                case "B Z":
                    sum += 3 + 6
                case "C X":
                    sum += 2 + 0
                case "C Y":
                    sum += 3 + 3
                case "C Z":
                    sum += 1 + 6
        print(sum)


main()
main2()