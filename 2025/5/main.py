def main():
    with open('2025/5/inputs.txt') as file:
        lines = list(map(lambda l: l.strip(), file.readlines()))
        ranges = []
        ids  = []
        isRange = True
        for line in lines:
            if line == '':
                isRange = False
                continue
            if isRange:
                parts = line.split('-')
                ranges.append(range(int(parts[0]), int(parts[1]) + 1))
            else:
                ids.append(int(line))
        fresh = set()
        for i in ids:
            for r in ranges:
                if i in r:
                    fresh.add(i)
        print(len(fresh))


def main2():
    with open('2025/5/inputs.txt') as file:
        lines = list(map(lambda l: l.strip(), file.readlines()))
        ranges = []
        for line in lines:
            if line == '':
                break
            else:
                parts = line.split('-')
                ranges.append(range(int(parts[0]), int(parts[1]) + 1))

        fresh = set()
        for r in ranges:
            fresh.update(list(r))
        print(len(fresh))





main()
main2()
