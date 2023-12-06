def main():
    with open('2023/6th/inputs.txt') as file:
        lines = file.readlines()
        times = list(map(lambda x: int(x.strip()), list(filter(lambda x: x != '', lines[0].split(': ')[1].split(' ')))))
        distances = list(map(lambda x: int(x.strip()), list(filter(lambda x: x != '', lines[1].split(': ')[1].split(' ')))))
        result = 1
        for i in range(0, len(distances)):
            distance = distances[i]
            time = times[i]
            best_times = 0
            for ms in range(1, time):
                time_needed = distance / ms
                if time_needed + ms < time:
                    best_times += 1
            result *= best_times
        print(result)



def main2():
    with open('2023/6th/inputs.txt') as file:
        lines = file.readlines()
        time = int(''.join(list(filter(lambda x: x != '', lines[0].split(': ')[1].split(' ')))))
        distance = int(''.join(list(filter(lambda x: x != '', lines[1].split(': ')[1].split(' ')))))
        result = 0
        for ms in range(1, time):
            time_needed = distance / ms
            if time_needed + ms < time:
                result += 1
        print(result)


main()
main2()
