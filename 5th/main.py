def main():
    with open('5th/inputs.txt') as file:
        lines = file.readlines()
        stacks = [[''],
                  ['H','B','V','W','N','M','L','P'],
                  ['M','Q','H'],
                  ['N','D','B','G','F','Q','M','L'],
                  ['Z','T','F','Q','M','W','G'],
                  ['M','T','H','P'],
                  ['C','B','M','J','D','H','G','T'],
                  ['M','N','B','F','V','R'],
                  ['P','L','H','M','R','G','S'],
                  ['P','D','B','C','N']
                  ]
        instructions = False
        for line in lines:
            if line == '\n':
                instructions = True;
            elif not instructions:
                continue
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
        stacks = [[''],
                  ['H','B','V','W','N','M','L','P'],
                  ['M','Q','H'],
                  ['N','D','B','G','F','Q','M','L'],
                  ['Z','T','F','Q','M','W','G'],
                  ['M','T','H','P'],
                  ['C','B','M','J','D','H','G','T'],
                  ['M','N','B','F','V','R'],
                  ['P','L','H','M','R','G','S'],
                  ['P','D','B','C','N']
                  ]
        instructions = False
        for line in lines:
            if line == '\n':
                instructions = True;
            elif not instructions:
                continue
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