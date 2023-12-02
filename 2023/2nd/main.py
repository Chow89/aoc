import re
import functools


def main():
    bag = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }
    with open('2023/2nd/inputs.txt') as file:
        lines = file.readlines()
        valid_games = []
        for line in lines:
            [game, results] = line.split(':')
            id = game.split(' ')[1]
            game_round_results = results.split(';')
            valid = True
            for round in game_round_results:
                cubes = round.split(',')
                for cube in cubes:
                    [number, color] = cube.strip().split(' ')
                    if bag[color] < int(number):
                        valid = False
            if valid:
                valid_games.append(id)
        print(functools.reduce(lambda a, b: int(a) + int(b), valid_games))


def main2():
    with open('2023/2nd/inputs.txt') as file:
        lines = file.readlines()
        result = 0
        for line in lines:
            results = line.split(':')[1]
            game_round_results = results.split(';')
            minimum = {
                'red': 0,
                'green': 0,
                'blue': 0,
            }
            for round in game_round_results:
                cubes = round.split(',')
                for cube in cubes:
                    [number, color] = cube.strip().split(' ')
                    if minimum[color] < int(number):
                        minimum[color] = int(number)
            result += minimum['red'] * minimum['green'] * minimum['blue']
        print(result)



main()
main2()