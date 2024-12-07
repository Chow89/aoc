def main():
    with open('2024/7/inputs.txt') as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        result = 0
        for line in lines:
            line = line.split(': ')
            designated_result = int(line[0].strip())
            numbers = list(map(int, line[1].split(' ')))
            num_combinations = 2 ** (len(numbers) -1)
            for i in range(num_combinations):
                binary = bin(i)[2:].rjust(len(numbers) - 1, '0')
                combination_sum = numbers[0]
                for idx, digit in enumerate(binary):
                    if digit == '0':
                        combination_sum += numbers[idx + 1]
                    elif digit == '1':
                        combination_sum *= numbers[idx + 1]
                if combination_sum == designated_result:
                    result += combination_sum
                    break
        print(result)


def to_base_3(n):
    if n == 0:
        return '0'
    digits = []
    while n:
        digits.append(str(n % 3))
        n //= 3
    return ''.join(digits[::-1])


def main2():
    with open('2024/7/inputs.txt') as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        result = 0
        for line in lines:
            line = line.split(': ')
            designated_result = int(line[0].strip())
            numbers = list(map(int, line[1].split(' ')))
            num_combinations = 3 ** (len(numbers) - 1)
            for i in range(num_combinations):
                base3number = to_base_3(i).rjust(len(numbers) - 1, '0')
                combination_sum = numbers[0]
                for idx, digit in enumerate(base3number):
                    if digit == '0':
                        combination_sum += numbers[idx + 1]
                    elif digit == '1':
                        combination_sum *= numbers[idx + 1]
                    elif digit == '2':
                        combination_sum = int(str(combination_sum) + str(numbers[idx + 1]))
                if combination_sum == designated_result:
                    result += combination_sum
                    break
        print(result)


main()
main2()
