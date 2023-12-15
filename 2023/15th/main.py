def main():
    with open('2023/15th/inputs.txt') as file:
        inputs = file.read().split(',')
        result = 0
        for input in inputs:
            value = 0
            for char in input:
                value += ord(char)
                value *= 17
                value %= 256
            result += value
        print(result)



def main2():
    with open('2023/15th/inputs.txt') as file:
        inputs = file.read().split(',')
        boxes = {}
        for input in inputs:
            if "=" in input:
                label, lens = input.split('=')
                box = 0
                for char in label:
                    box += ord(char)
                    box *= 17
                    box %= 256
                if boxes.get(box):
                    if len(list(filter(lambda x: x[0] == label, boxes[box]))) > 0:
                        index = boxes[box].index(list(filter(lambda x: x[0] == label, boxes[box]))[0])
                        boxes[box][index] = (label, lens)
                    else:
                        boxes[box].append((label, lens))
                else:
                    boxes[box] = [(label, lens)]
            else:
                label = input.strip('-')
                box = 0
                for char in label:
                    box += ord(char)
                    box *= 17
                    box %= 256
                if boxes.get(box):
                    if len(list(filter(lambda x: x[0] == label, boxes[box]))) > 0:
                        boxes[box] = list(filter(lambda x: x[0] != label, boxes[box]))
        result = 0
        for box_index in boxes.keys():
                for slot_index in range(len(boxes[box_index])):
                    result += (box_index + 1) * (slot_index + 1) * int(boxes[box_index][slot_index][1])
        print(result)


main()
main2()
