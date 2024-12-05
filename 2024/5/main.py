def main():
    with open('2024/5/inputs.txt') as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        rules = lines[:lines.index('')]
        rules = list(map(lambda x: list(map(int, x.split('|'))), rules))
        updates = lines[lines.index('') + 1:]
        updates = list(map(lambda x: list(map(int, x.split(','))), updates))
        incorrect_updates = []
        for update in updates:
            for rule in rules:
                if rule[0] in update and rule[1] in update:
                    if update.index(rule[0]) > update.index(rule[1]):
                        incorrect_updates.append(update)
                        break
        correct_updates = list(filter(lambda x: x not in incorrect_updates, updates))
        sum = 0
        for update in correct_updates:
            sum += update[len(update) // 2]
        print(sum)


def reorder(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                update[update.index(rule[0])], update[update.index(rule[1])] = update[update.index(rule[1])], update[update.index(rule[0])]
                reorder(update, rules)
    return update


def main2():
    with open('2024/5/inputs.txt') as file:
        lines = list(map(lambda x: x.strip(), file.readlines()))
        rules = lines[:lines.index('')]
        rules = list(map(lambda x: list(map(int, x.split('|'))), rules))
        updates = lines[lines.index('') + 1:]
        updates = list(map(lambda x: list(map(int, x.split(','))), updates))
        result = []
        for update in updates:
            for rule in rules:
                if rule[0] in update and rule[1] in update:
                    if update.index(rule[0]) > update.index(rule[1]):
                        result.append(reorder(update, rules))
        sum = 0
        for update in result:
            sum += update[len(update) // 2]
        print(sum)


main()
main2()
