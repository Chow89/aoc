import copy


def main():
    with open('2023/19th/inputs.txt') as file:
        workflows, parts = file.read().split('\n\n')
        data = {}
        for workflow in workflows.splitlines():
            name, conditons = workflow[:-1].split('{')
            for condition in conditons.split(','):
                if ':' in condition:
                    c, next = condition.split(':')
                    if '<' in c:
                        field, value = c.split('<')
                        if name in data:
                            data[name].append((field, int(value), 'L', next))
                        else:
                            data[name] = [(field, int(value), 'L', next)]
                    else:
                        field, value = c.split('>')
                        if name in data:
                            data[name].append((field, int(value), 'G', next))
                        else:
                            data[name] = [(field, int(value), 'G', next)]
                else:
                    data[name].append(condition)

        accepted = []
        for part in parts.splitlines():
            values = part[1:-1].split(',')
            props = {}
            for value in values:
                field, v = value.split('=')
                props[field] = int(v)
            workflow = copy.deepcopy(data['in'])
            while workflow:
                for instruction in workflow:
                    if type(instruction) == tuple:
                        field, value, op, next = instruction
                        if op == 'L':
                            if value > props[field]:
                                if next == 'A':
                                    accepted.append(props)
                                    workflow = None
                                    break
                                if next == 'R':
                                    workflow = None
                                    break
                                workflow = copy.deepcopy(data[next])
                                break
                        else:
                            if value < props[field]:
                                if next == 'A':
                                    workflow = None
                                    accepted.append(props)
                                    break
                                if next == 'R':
                                    workflow = None
                                    break
                                workflow = copy.deepcopy(data[next])
                                break
                    else:
                        if instruction == 'A':
                            workflow = None
                            accepted.append(props)
                            break
                        if instruction == 'R':
                            workflow = None
                            break
                        workflow = copy.deepcopy(data[instruction])
                        break
        result = 0
        for a in accepted:
            result += a['x'] + a['m'] + a['a'] + a['s']
        print(result)


def main2():
    with open('2023/19th/inputs.txt') as file:
        lines = file.readlines()


main()
main2()
