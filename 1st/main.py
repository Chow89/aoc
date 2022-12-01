import requests

def main():
    with open('1st/inputs.txt') as file:
        lines = file.readlines()
        index = 0
        elves = [0]
        for line in lines:
            if line == '\n':
                index = index + 1
                elves.append(0)
                continue
            elves[index] = elves[index] + int(line)
        elves.sort(reverse=True)
        print("Top 1:")
        print(elves[0])
        print("Top 3 sum:")
        print(sum(elves[0:3]))

main()