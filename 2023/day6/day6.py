# part 1
def read_race_stats(file):
    races = []
    with open(file, 'r') as f:
        lines = f.readlines()
        times = [int(num) for num in lines[0].split(':')[1].split()]
        distances = [int(num) for num in lines[1].split(':')[1].split()]
    for i in range(0, len(times)):
        races.append([times[i], distances[i]])
    return races

def calc_time(stats):
    total_winning_times = []
    for race in stats:
        record_distance = race[1]
        time = race[0]
        winning_times =[]
        for i in range(0, time):
            this_distance = i * (time - i)
            if this_distance > record_distance:
                winning_times.append((i, this_distance))
        total_winning_times.append(winning_times)
    return total_winning_times

races = read_race_stats('input6.txt')
winning_times = calc_time(races)
print(winning_times)
sum_winning_times = len(winning_times[0])
for j in range(1, len(winning_times)):
    sum_winning_times = sum_winning_times * len(winning_times[j])

print(sum_winning_times)

# part 2
def read_race_stats2(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        times = [str(num) for num in lines[0].split(':')[1].split()]
        distances = [str(num) for num in lines[1].split(':')[1].split()]
    total_time = ''
    for time in times:
        total_time += time
    total_distance = ''
    for distance in distances:
        total_distance += distance
    return int(total_time), int(total_distance)

def calc_time2(time, record_distance):
    winning_times =[]
    for i in range(0, time):
        this_distance = i * (time - i)
        if this_distance > record_distance:
            winning_times.append((i, this_distance))
    winning_times.append(winning_times)
    return winning_times

time,distance = read_race_stats2('input6.txt')
print(time, distance)
winning_times = calc_time2(time, distance)
# will print an extra since the list is so long, subtract accordingly
print(len(winning_times) - 1)
