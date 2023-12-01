def main():
    with open('2022/1st/inputs.txt') as file:
        lines = file.readlines()
        elv, elves = 0, [0]
        for line in lines:
            if line == '\n':
                elv += 1
                elves.append(0)
                continue
            elves[elv] += int(line)
        elves.sort(reverse=True)
        print("Top: " + str(elves[0]))
        print("Top 3: " + str(sum(elves[0:3])))


main()
