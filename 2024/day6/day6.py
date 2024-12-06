# # part 1
# import time

# def read_map(file_path):
#     with open(file_path, 'r') as file:
#         return [line.strip() for line in file.readlines()]

# def determine_moving_state(map):
#     for line in range(len(map)):
#         for char in range(len(map[line])):
#             if map[line][char] == '^':
#                 return 'up', (line, char)
#             elif map[line][char] == 'v':
#                 return 'down', (line, char)
#             elif map[line][char] == '<':
#                 return 'left', (line, char)
#             elif map[line][char] == '>':
#                 return 'right', (line, char)

# def trace_map(map):
#     travelled_map = [['.' for _ in range(len(map[0]))] for _ in range(len(map))]
#     moving_state, position = determine_moving_state(map)
#     travelled_map[position[0]][position[1]] = 'X'
#     in_map = True
#     while in_map:
#         if moving_state == 'up':
#             if position[0] - 1 >= 0:
#                 if map[position[0] - 1][position[1]] != '#':
#                     travelled_map[position[0] - 1][position[1]] = 'X'
#                     position = (position[0] - 1, position[1])
#                 elif map[position[0] - 1][position[1]] == '#':
#                     moving_state = 'right'
#             else:
#                 in_map = False
#         elif moving_state == 'down':
#             if position[0] + 1 < len(map):
#                 if map[position[0] + 1][position[1]] != '#':
#                     travelled_map[position[0] + 1][position[1]] = 'X'
#                     position = (position[0] + 1, position[1])
#                 elif map[position[0] + 1][position[1]] == '#':
#                     moving_state = 'left'
#             else:
#                 in_map = False
#         elif moving_state == 'left':
#             if position[1] - 1 >= 0:
#                 if map[position[0]][position[1] - 1] != '#':
#                     travelled_map[position[0]][position[1] - 1] = 'X'
#                     position = (position[0], position[1] - 1)
#                 elif map[position[0]][position[1] - 1] == '#':
#                     moving_state = 'up'
#             else:
#                 in_map = False
#         elif moving_state == 'right':
#             if position[1] + 1 < len(map[0]):
#                 if map[position[0]][position[1] + 1] != '#':
#                     travelled_map[position[0]][position[1] + 1] = 'X'
#                     position = (position[0], position[1] + 1)
#                 elif map[position[0]][position[1] + 1] == '#':
#                     moving_state = 'down'
#             else:
#                 in_map = False
#     return travelled_map

# def count_travelled_map(travelled_map):
#     count = 0   
#     for line in travelled_map:
#         for char in line:
#             if char == 'X':
#                 count += 1
#     for line in travelled_map:
#         print(''.join(line))
#     return count

# map = read_map('input6.txt')
# print(count_travelled_map(trace_map(map)))

# part 2
# part 1
import time
moving_states = ['up', 'down', 'left', 'right']
def read_map2(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

def determine_moving_state2(map):
    for line in range(len(map)):
        for char in range(len(map[line])):
            if map[line][char] == '^':
                return 'up', (line, char)
            elif map[line][char] == 'v':
                return 'down', (line, char)
            elif map[line][char] == '<':
                return 'left', (line, char)
            elif map[line][char] == '>':
                return 'right', (line, char)

def trace_map2(map):
    travelled_map = [['.' for _ in range(len(map[0]))] for _ in range(len(map))]
    moving_state, position = determine_moving_state2(map)
    travelled_map[position[0]][position[1]] = moving_state
    in_map = True
    loop = False
    while in_map:
        if moving_state == 'up':
            if position[0] - 1 >= 0:
                if map[position[0] - 1][position[1]] != '#':
                    loop = loop_check(travelled_map, (position[0] - 1, position[1]), moving_state)
                    travelled_map[position[0] - 1][position[1]] = moving_state
                    position = (position[0] - 1, position[1])
                elif map[position[0] - 1][position[1]] == '#':
                    moving_state = 'right'
            else:
                in_map = False
        elif moving_state == 'down':
            if position[0] + 1 < len(map):
                if map[position[0] + 1][position[1]] != '#':
                    loop = loop_check(travelled_map, (position[0] + 1, position[1]), moving_state)
                    travelled_map[position[0] + 1][position[1]] = moving_state
                    position = (position[0] + 1, position[1])
                elif map[position[0] + 1][position[1]] == '#':
                    moving_state = 'left'
            else:
                in_map = False
        elif moving_state == 'left':
            if position[1] - 1 >= 0:
                if map[position[0]][position[1] - 1] != '#':
                    loop = loop_check(travelled_map, (position[0], position[1] - 1), moving_state)
                    travelled_map[position[0]][position[1] - 1] = moving_state
                    position = (position[0], position[1] - 1)
                elif map[position[0]][position[1] - 1] == '#':
                    moving_state = 'up'
            else:
                in_map = False
        elif moving_state == 'right':
            if position[1] + 1 < len(map[0]):
                if map[position[0]][position[1] + 1] != '#':
                    loop = loop_check(travelled_map, (position[0], position[1] + 1), moving_state)
                    travelled_map[position[0]][position[1] + 1] = moving_state
                    position = (position[0], position[1] + 1)
                elif map[position[0]][position[1] + 1] == '#':
                    moving_state = 'down'
            else:
                in_map = False
        if loop:
            break
        
    return travelled_map, loop

def loop_check(travelled_map, position, moving_state):
    if travelled_map[position[0]][position[1]] == moving_state:
        # print(travelled_map[position[0]][position[1]], moving_state)
        return True
    return False

def count_travelled_map2(travelled_map):
    count = 0   
    for line in travelled_map:
        for char in line:
            if char in moving_states:
                count += 1
    # for line in travelled_map:
    #     print(''.join(line))
    return count

def add_obstacle2(map, row, char):
    new_map = map.copy()
    new_map[row] = new_map[row][:char] + '#' + new_map[row][char+1:]
    return new_map

map = read_map2('input6.txt')
loops = 0
for row in range(len(map)):
    for char in range(len(map[row])):
        if map[row][char] == '.':
            new_map = add_obstacle2(map, row, char)
            travelled_map, loop = trace_map2(new_map)
            if loop:
                loops += 1

print(loops)