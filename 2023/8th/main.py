def main():
    with open('2023/8th/inputs.txt') as file:
        lines = file.readlines()
        instructions = lines[0].strip()
        data = {}
        for line in lines[2:]:
            source = line.split('=')[0].strip()
            target = line.split('=')[1].strip()[1:-1].split(', ')
            data[source] = {'L': target[0], 'R': target[1]}
        current_node = 'AAA'
        steps = 0
        while current_node != 'ZZZ':
            instruction = instructions[steps % len(instructions)]
            current_node = data[current_node][instruction]
            steps += 1
        print(steps)



def main2():
    with open('2023/8th/inputs.txt') as file:
        lines = file.readlines()
        instructions = lines[0].strip()
        data = {}
        for line in lines[2:]:
            source = line.split('=')[0].strip()
            target = line.split('=')[1].strip()[1:-1].split(', ')
            data[source] = {'L': target[0], 'R': target[1]}
        current_nodes = list(filter(lambda x: x[-1] == 'A', list(data.keys())))
        steps = 0
        while len(list(filter(lambda x: x[-1] == 'Z', current_nodes))) != len(current_nodes):
            targets = []
            instruction = instructions[steps % len(instructions)]
            for node in current_nodes:
                targets.append(data[node][instruction])
            steps += 1
            current_nodes = targets
        print(steps)


main()
main2()
