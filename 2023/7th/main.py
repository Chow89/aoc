from enum import Enum


class Category(Enum):
    HIGH_CARD = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_OF_A_KIND = 3
    FULL_HOUSE = 4
    FOUR_OF_A_KIND = 5
    FIVE_OF_A_KIND = 6


def translate(input):
    translated_hand = []
    for card in input[0]:
        if card == 'A':
            translated_hand.append(14)
        elif card == 'K':
            translated_hand.append(13)
        elif card == 'Q':
            translated_hand.append(12)
        elif card == 'J':
            translated_hand.append(11)
        elif card == 'T':
            translated_hand.append(10)
        else:
            translated_hand.append(int(card))
    return translated_hand, input[1]


def translate2(input):
    translated_hand = []
    for card in input[0]:
        if card == 'A':
            translated_hand.append(14)
        elif card == 'K':
            translated_hand.append(13)
        elif card == 'Q':
            translated_hand.append(12)
        elif card == 'J':
            translated_hand.append(1)
        elif card == 'T':
            translated_hand.append(10)
        else:
            translated_hand.append(int(card))
    return translated_hand, input[1]


def categorize(input):
    hand = sorted(input[0])
    if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
        return input[0], input[1], Category.FIVE_OF_A_KIND
    elif hand[0] == hand[1] == hand[2] == hand[3] or hand[1] == hand[2] == hand[3] == hand[4]:
        return input[0], input[1], Category.FOUR_OF_A_KIND
    elif (hand[0] == hand[1] == hand[2] and hand[3] == hand[4]) or (hand[0] == hand[1] and hand[2] == hand[3] == hand[4]):
        return input[0], input[1], Category.FULL_HOUSE
    elif hand[0] == hand[1] == hand[2] or hand[1] == hand[2] == hand[3] or hand[2] == hand[3] == hand[4]:
        return input[0], input[1], Category.THREE_OF_A_KIND
    elif (hand[0] == hand[1] and hand[2] == hand[3]) or (hand[0] == hand[1] and hand[3] == hand[4]) or (hand[1] == hand[2] and hand[3] == hand[4]):
        return input[0], input[1], Category.TWO_PAIR
    elif hand[0] == hand[1] or hand[1] == hand[2] or hand[2] == hand[3] or hand[3] == hand[4]:
        return input[0], input[1], Category.PAIR
    else:
        return input[0], input[1], Category.HIGH_CARD


def categorize2(input):
    hand = sorted(input[0])
    num_joker = hand.count(1)
    if num_joker == 4 or num_joker == 5:
        return input[0], input[1], Category.FIVE_OF_A_KIND
    elif num_joker == 3:
        if hand[3] == hand[4]:
            return input[0], input[1], Category.FIVE_OF_A_KIND
        else:
            return input[0], input[1], Category.FOUR_OF_A_KIND
    elif num_joker == 2:
        if hand[2] == hand[3] == hand[4]:
            return input[0], input[1], Category.FIVE_OF_A_KIND
        elif hand[2] == hand[3] or hand[3] == hand[4]:
            return input[0], input[1], Category.FOUR_OF_A_KIND
        else:
            return input[0], input[1], Category.THREE_OF_A_KIND
    elif num_joker == 1:
        if hand[1] == hand[2] == hand[3] == hand[4]:
            return input[0], input[1], Category.FIVE_OF_A_KIND
        elif hand[1] == hand[2] == hand[3] or hand[2] == hand[3] == hand[4]:
            return input[0], input[1], Category.FOUR_OF_A_KIND
        elif hand[1] == hand[2] and hand[3] == hand[4]:
            return input[0], input[1], Category.FULL_HOUSE
        elif hand[1] == hand[2] or hand[2] == hand[3] or hand[3] == hand[4]:
            return input[0], input[1], Category.THREE_OF_A_KIND
        else:
            return input[0], input[1], Category.PAIR
    else:
        if hand[0] == hand[1] == hand[2] == hand[3] == hand[4]:
            return input[0], input[1], Category.FIVE_OF_A_KIND
        elif hand[0] == hand[1] == hand[2] == hand[3] or hand[1] == hand[2] == hand[3] == hand[4]:
            return input[0], input[1], Category.FOUR_OF_A_KIND
        elif (hand[0] == hand[1] == hand[2] and hand[3] == hand[4]) or (
                hand[0] == hand[1] and hand[2] == hand[3] == hand[4]):
            return input[0], input[1], Category.FULL_HOUSE
        elif hand[0] == hand[1] == hand[2] or hand[1] == hand[2] == hand[3] or hand[2] == hand[3] == hand[4]:
            return input[0], input[1], Category.THREE_OF_A_KIND
        elif (hand[0] == hand[1] and hand[2] == hand[3]) or (hand[0] == hand[1] and hand[3] == hand[4]) or (
                hand[1] == hand[2] and hand[3] == hand[4]):
            return input[0], input[1], Category.TWO_PAIR
        elif hand[0] == hand[1] or hand[1] == hand[2] or hand[2] == hand[3] or hand[3] == hand[4]:
            return input[0], input[1], Category.PAIR
        else:
            return input[0], input[1], Category.HIGH_CARD


def sort(data):
    grouped_data = [[], [], [], [], [], [], []]
    sorted_list = []
    for entry in data:
        grouped_data[entry[2].value].append(entry)
    for group in grouped_data:
        group.sort(key=lambda x: x[0])
        sorted_list.extend(group)
    return sorted_list


def main():
    with open('2023/7th/inputs.txt') as file:
        lines = file.readlines()
        data = []
        for line in lines:
            hand, bet = line.split(' ')
            data.append((hand, int(bet)))
        data = list(map(lambda x: translate(x), data))
        data = list(map(lambda x: categorize(x), data))
        data = sort(data)
        result = 0
        for i in range(len(data)):
            result += data[i][1] * (i + 1)
        print(result)


def main2():
    with open('2023/7th/inputs.txt') as file:
        lines = file.readlines()
        data = []
        for line in lines:
            hand, bet = line.split(' ')
            data.append((hand, int(bet)))
        data = list(map(lambda x: translate2(x), data))
        data = list(map(lambda x: categorize2(x), data))
        data = sort(data)
        result = 0
        for i in range(len(data)):
            result += data[i][1] * (i + 1)
        print(result)


main()
main2()
