def main():
    with open('2022/11th/inputs.txt') as file:
        lines = file.readlines()
        monkeys = []
        currentMonkey = None
        for line in lines:
            if line.strip().startswith('Monkey'):
                currentMonkey = {
                    "itemsInspected": 0,
                    "items": [],
                    "operation": [],
                    "divisor": 0,
                    "on": {
                        "true": 0,
                        "false": 0
                    }
                }
            elif line.strip().startswith('Starting'):
                items = list(map(lambda x: int(x.strip()), line.split(': ')[1].split(', ')))
                currentMonkey["items"] = items
            elif line.strip().startswith('Operation'):
                op = line.split(': ')[1].strip().split(' ')[2:]
                currentMonkey['operation'] = op
            elif line.strip().startswith('Test'):
                currentMonkey['divisor'] = int(line.split(' ')[-1])
            elif line.strip().startswith('If'):
                [_, case, _, _, _, target] = line.strip().split(' ')
                match case.strip(':'):
                    case "true":
                        currentMonkey['on']['true'] = int(target)
                    case "false":
                        currentMonkey['on']['false'] = int(target)
                        monkeys.append(currentMonkey)

        for round in range(0, 20):
            for monkey in monkeys:
                for item in monkey['items']:
                    monkey['itemsInspected'] += 1
                    if monkey['operation'][2] == 'old':
                        number = int(item)
                    else:
                        number = int(monkey['operation'][2])
                    newValue = 0
                    match monkey['operation'][1]:
                        case '+':
                            newValue = (item + number) // 3
                        case '*':
                            newValue = (item * number) // 3
                    if newValue % monkey['divisor'] == 0:
                        monkeys[monkey['on']['true']]['items'].append(newValue)
                    else:
                        monkeys[monkey['on']['false']]['items'].append(newValue)
                monkey['items'] = []
        orderedMonkeys = sorted(monkeys, key=lambda m: m['itemsInspected'], reverse=True)
        print(orderedMonkeys[0]['itemsInspected'] * orderedMonkeys[1]['itemsInspected'])


def main2():
    with open('2022/11th/inputs.txt') as file:
        lines = file.readlines()
        monkeys = []
        currentMonkey = None
        for line in lines:
            if line.strip().startswith('Monkey'):
                currentMonkey = {
                    "itemsInspected": 0,
                    "items": [],
                    "operation": [],
                    "divisor": 0,
                    "on": {
                        "true": 0,
                        "false": 0
                    }
                }
            elif line.strip().startswith('Starting'):
                items = list(map(lambda x: int(x.strip()), line.split(': ')[1].split(', ')))
                currentMonkey["items"] = items
            elif line.strip().startswith('Operation'):
                op = line.split(': ')[1].strip().split(' ')[2:]
                currentMonkey['operation'] = op
            elif line.strip().startswith('Test'):
                currentMonkey['divisor'] = int(line.split(' ')[-1])
            elif line.strip().startswith('If'):
                [_, case, _, _, _, target] = line.strip().split(' ')
                match case.strip(':'):
                    case "true":
                        currentMonkey['on']['true'] = int(target)
                    case "false":
                        currentMonkey['on']['false'] = int(target)
                        monkeys.append(currentMonkey)

        for round in range(0, 10000):
            for monkey in monkeys:
                for item in monkey['items']:
                    monkey['itemsInspected'] += 1
                    if monkey['operation'][2] == 'old':
                        number = int(item)
                    else:
                        number = int(monkey['operation'][2])
                    newValue = 0
                    match monkey['operation'][1]:
                        case '+':
                            newValue = item + number
                        case '*':
                            newValue = item * number
                    if newValue % monkey['divisor'] == 0:
                        monkeys[monkey['on']['true']]['items'].append(newValue)
                    else:
                        monkeys[monkey['on']['false']]['items'].append(newValue)
                monkey['items'] = []
        orderedMonkeys = sorted(monkeys, key=lambda m: m['itemsInspected'], reverse=True)
        print(orderedMonkeys[0]['itemsInspected'] * orderedMonkeys[1]['itemsInspected'])


main()
main2()
