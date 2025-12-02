from re import findall


def main():
    with open('2025/2/inputs.txt') as file:
        lines = file.readline()
        ranges = lines.split(',')
        summedIds = 0
        for r in ranges:
            start, end = tuple(map(int, r.split('-')))
            for i in range(start, end + 1):
                s = str(i)
                if len(s) % 2 != 0:
                    continue
                if s[:len(s)//2] == s[len(str(s))//2:]:
                    summedIds += i
        print(summedIds)


def main2():
    with open('2025/2/inputs.txt') as file:
        lines = file.readline()
        ranges = lines.split(',')
        summedIds = 0
        for r in ranges:
            start, end = tuple(map(int, r.split('-')))
            for i in range(start, end + 1):
                s = str(i)
                length = len(s)
                for l in range(1, length // 2 + 1):
                    pattern = s[:l]
                    if len(findall(pattern, s)) > 1 and len(findall(pattern, s)) * l == length:
                        summedIds += i
                        break
        print(summedIds)



main()
main2()
