def main():
    with open('2024/9/inputs.txt') as file:
        line = file.readline().strip()
        disk = []
        file_id = 0
        for idx, digit in enumerate(line):
            if idx % 2 == 0:
                disk.extend([file_id] * int(digit))
                file_id += 1
            else:
                disk.extend([-1] * int(digit))

        empty_spaces = []
        for idx, file_id in enumerate(disk):
            if file_id == -1:
                empty_spaces.append(idx)

        for i in empty_spaces:
            while disk[-1] == -1:
                disk.pop()
            if len(disk) <= i:
                break
            disk[i] = disk.pop()

        result = 0
        for i in range(len(disk)):
            result += (i * int(disk[i]))
        print(result)


def main2():
    with open('2024/9/inputs.txt') as file:
        pass


main()
main2()
