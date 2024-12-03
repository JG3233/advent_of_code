# part 1
import re

def read_almanac(filename):
    maps = []
    seeds = []
    with open(filename, 'r') as file:
        map = []
        for line in file:
            if line.startswith('seeds'):
                seeds = [int(num) for num in line.split(':')[1].split()]
                print(seeds)
            elif re.search(r'map', line):
                if map:
                    maps.append(map)
                map = []
            elif not re.search(r'[0-9]', line):
                continue
            else:
                map.append(line.strip())
        maps.append(map)
    return maps, seeds

def process_map(map, seeds):
    new_seeds = []
    for seed_range in seeds:
        if isinstance(seed_range, range):
            print('RANGE')
            for seed in seed_range:
                # print(seed)
                for line in map:
                    keys = [int(num) for num in line.split()]
                    if seed in range(keys[1], keys[1] + keys[2]):
                        # print(seed, keys)
                        seed = keys[0] + seed - keys[1]
                        break
                new_seeds.append(seed)
        else:
            seed = seed_range
            for line in map:
                keys = [int(num) for num in line.split()]
                if seed in range(keys[1], keys[1] + keys[2]):
                    # print(seed, keys)
                    seed = keys[0] + seed - keys[1]
                    break
            new_seeds.append(seed)
    return new_seeds

def calc_seeds(seeds):
    new_seeds = []
    for i in range (0, len(seeds)):
        if i == 0 or i % 2 == 0:
            new_seeds.append(range(seeds[i], seeds[i] + seeds[i+1]))
        else:
            continue
    return new_seeds

maps, seeds = read_almanac('input5.txt')
seeds = calc_seeds(seeds)
# print(seeds)
# print(maps)
for map in maps:
    seeds = process_map(map, seeds)
    print(seeds)

min_seed = min(seeds)
print(min_seed)