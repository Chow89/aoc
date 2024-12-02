def main():
    with open('2024/1/inputs.txt') as file:
        lines = file.readlines()
        l1 = []
        l2 = []
        sum = 0
        for line in lines:
            values = list(filter(lambda x: x != '', line.strip().split(' ')))
            l1.append(int(values[0]))
            l2.append(int(values[1]))
        l1.sort()
        l2.sort()
        for i in range(len(l1)):
            sum += abs(l1[i] - l2[i])
        print(sum)


def main2():
    with open('2024/1/inputs.txt') as file:
        lines = file.readlines()
        l1 = []
        l2 = []
        sum = 0
        for line in lines:
            values = list(filter(lambda x: x != '', line.strip().split(' ')))
            l1.append(int(values[0]))
            l2.append(int(values[1]))
        for i in range(len(l1)):
            count = len(list(filter(lambda x: x == l1[i], l2)))
            sum += l1[i] * count
        print(sum)


main()
main2()
