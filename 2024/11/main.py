from functools import cache

@cache
def count(number, steps):
    if steps == 0:
        return 1
    elif number == 0:
        return count(1, steps - 1)
    elif len(str(number)) % 2 == 0:
        mid = len(str(number)) // 2
        return count(int(str(number)[:mid]), steps - 1) + count(int(str(number)[mid:]), steps - 1)
    else:
        return count(number * 2024, steps - 1)


def main():
    with open('2024/11/inputs.txt') as file:
        numbers = list(map(int, file.readline().strip().split()))
        total = 0
        for number in numbers:
            total += count(number, 25)
        print(total)


def main2():
    with open('2024/11/inputs.txt') as file:
        numbers = list(map(int, file.readline().strip().split()))
        total = 0
        for number in numbers:
            total += count(number, 75)
        print(total)


main()
main2()
