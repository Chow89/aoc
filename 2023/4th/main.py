import functools


def main():
    with open('2023/4th/inputs.txt') as file:
        lines = file.readlines()
        points = 0
        for line in lines:
            cardpoints = 0
            winning_numbers, card_numbers = line.split(':')[1].strip().split('|')
            winning_numbers = list(map(lambda x: x.strip(), winning_numbers.strip().split(' ')))
            card_numbers = list(map(lambda x: x.strip(), card_numbers.strip().split(' ')))
            for winning_number in winning_numbers:
                if winning_number != '' and winning_number in card_numbers:
                    if cardpoints == 0:
                        cardpoints = 1
                    else:
                        cardpoints *= 2
            points += cardpoints
        print(points)


def main2():
    with open('2023/4th/inputs.txt') as file:
        lines = file.readlines()
        cards = []
        total_cards = 0
        for i in range(len(lines)):
            cards.append(i + 1)
            number_of_cards = len(list(filter(lambda n: n == (i + 1), cards)))
            total_cards += number_of_cards
            cards = list(filter(lambda n: n != (i + 1), cards))
            cardpoints = 0
            winning_numbers, card_numbers = lines[i].split(':')[1].strip().split('|')
            winning_numbers = list(map(lambda x: x.strip(), winning_numbers.strip().split(' ')))
            card_numbers = list(map(lambda x: x.strip(), card_numbers.strip().split(' ')))
            for winning_number in winning_numbers:
                if winning_number != '' and winning_number in card_numbers:
                    cardpoints += 1
            for repetation in range(number_of_cards):
                for p in range(i + 2, i + cardpoints + 2):
                    cards.append(p)
        print(total_cards)


main()
main2()
