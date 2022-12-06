def main():
    with open('5th/inputs.txt') as file:
        lines = file.readlines()
        stacks = [[], [], [], [], [], [], [], [], []]
        instructions = False
        for line in lines:
            if line == '\n':
                stacks.insert(0, [])
                instructions = True;
            elif not instructions:
                crates = line[1::4]
                if crates[0] != '1':
                    for i in range(0, len(crates)):
                        if crates[i] != ' ':
                            stacks[i].insert(0, crates[i])
            else:
                _, elements, _, origin, _, destination = line.split(' ')
                elements = int(elements)
                origin = int(origin)
                destination = int(destination)
                for i in range(0, elements):
                    element = stacks[origin].pop()
                    stacks[destination].append(element)
        for stack in stacks[1:]:
            print(stack.pop(), end='')
        print()



def main2():
    with open('5th/inputs.txt') as file:
        lines = file.readlines()
        stacks = [[], [], [], [], [], [], [], [], []]
        instructions = False
        for line in lines:
            if line == '\n':
                stacks.insert(0, [])
                instructions = True;
            elif not instructions:
                crates = line[1::4]
                if crates[0] != '1':
                    for i in range(0, len(crates)):
                        if crates[i] != ' ':
                            stacks[i].insert(0, crates[i])
            else:
                _, elements, _, origin, _, destination = line.split(' ')
                elements = int(elements)
                origin = int(origin)
                destination = int(destination)
                for i in range(0, elements):
                    element = stacks[origin].pop(i - elements)
                    stacks[destination].append(element)
        for stack in stacks[1:]:
            print(stack.pop(), end='')


main()
main2()