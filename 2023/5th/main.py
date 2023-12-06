def main():
    with open('2023/5th/inputs.txt') as file:
        lines = file.readlines()
        seeds = list(map(lambda x: int(x), lines[0].split(':')[1].strip().split(' ')))
        current_map = ''
        data = {}
        for line in lines[2:]:
            if line == '\n':
                continue
            if line[0].isdigit():
                destination, source, rng = list(map(lambda x: int(x), line.strip().split(' ')))
                m = data.get(current_map)
                m.append([destination, source, rng])
            else:
                current_map = line.strip()[:-5]
                data.update({current_map: []})
        locations = []
        for seed in seeds:
            soil = seed
            for mapping in data.get('seed-to-soil'):
                if mapping[1] <= seed < mapping[1] + mapping[2]:
                    diff = mapping[0] - mapping[1]
                    soil = seed + diff

            fertilizer = soil
            for mapping in data.get('soil-to-fertilizer'):
                if mapping[1] <= soil < mapping[1] + mapping[2]:
                    diff = mapping[0] - mapping[1]
                    fertilizer = soil + diff

            water = fertilizer
            for mapping in data.get('fertilizer-to-water'):
                if mapping[1] <= fertilizer < mapping[1] + mapping[2]:
                    diff = mapping[0] - mapping[1]
                    water = fertilizer + diff

            light = water
            for mapping in data.get('water-to-light'):
                if mapping[1] <= water < mapping[1] + mapping[2]:
                    diff = mapping[0] - mapping[1]
                    light = water + diff

            temperature = light
            for mapping in data.get('light-to-temperature'):
                if mapping[1] <= light < mapping[1] + mapping[2]:
                    diff = mapping[0] - mapping[1]
                    temperature = light + diff

            humidity = temperature
            for mapping in data.get('temperature-to-humidity'):
                if mapping[1] <= temperature < mapping[1] + mapping[2]:
                    diff = mapping[0] - mapping[1]
                    humidity = temperature + diff

            location = humidity
            for mapping in data.get('humidity-to-location'):
                if mapping[1] <= humidity < mapping[1] + mapping[2]:
                    diff = mapping[0] - mapping[1]
                    location = humidity + diff
            locations.append(location)

        print(min(locations))



def main2():
    with open('2023/5th/inputs.txt') as file:
        lines = file.readlines()
        seed_ranges = list(map(lambda x: int(x), lines[0].split(':')[1].strip().split(' ')))
        number_of_ranges = int(len(seed_ranges) / 2)
        minlocation = 2**63 - 1

        current_map = ''
        data = {}
        for line in lines[2:]:
            if line == '\n':
                continue
            if line[0].isdigit():
                destination, source, rng = list(map(lambda x: int(x), line.strip().split(' ')))
                m = data.get(current_map)
                m.append([destination, source, rng])
            else:
                current_map = line.strip()[:-5]
                data.update({current_map: []})

        for i in range(number_of_ranges):
            start = seed_ranges[i * 2]
            end = start + seed_ranges[i * 2 + 1]
            for seed in range(start, end):

                soil = seed
                for mapping in data.get('seed-to-soil'):
                    if mapping[1] <= seed < mapping[1] + mapping[2]:
                        diff = mapping[0] - mapping[1]
                        soil = seed + diff

                fertilizer = soil
                for mapping in data.get('soil-to-fertilizer'):
                    if mapping[1] <= soil < mapping[1] + mapping[2]:
                        diff = mapping[0] - mapping[1]
                        fertilizer = soil + diff

                water = fertilizer
                for mapping in data.get('fertilizer-to-water'):
                    if mapping[1] <= fertilizer < mapping[1] + mapping[2]:
                        diff = mapping[0] - mapping[1]
                        water = fertilizer + diff

                light = water
                for mapping in data.get('water-to-light'):
                    if mapping[1] <= water < mapping[1] + mapping[2]:
                        diff = mapping[0] - mapping[1]
                        light = water + diff

                temperature = light
                for mapping in data.get('light-to-temperature'):
                    if mapping[1] <= light < mapping[1] + mapping[2]:
                        diff = mapping[0] - mapping[1]
                        temperature = light + diff

                humidity = temperature
                for mapping in data.get('temperature-to-humidity'):
                    if mapping[1] <= temperature < mapping[1] + mapping[2]:
                        diff = mapping[0] - mapping[1]
                        humidity = temperature + diff

                location = humidity
                for mapping in data.get('humidity-to-location'):
                    if mapping[1] <= humidity < mapping[1] + mapping[2]:
                        diff = mapping[0] - mapping[1]
                        location = humidity + diff
                if location < minlocation:
                    minlocation = location

        print(minlocation)


main()
main2()
