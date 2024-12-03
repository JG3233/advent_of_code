# part 1
# def read_input(file_path):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         return [list(map(int, line.split())) for line in lines]

# def determine_safety(input_list):
#     safety_score = 0
#     for level in input_list:
#         #decreasing
#         if level[0] > level[1]:
#             safe = True 
#             for i in range(0, len(level) - 1):
#                 if level[i] <= level[i+1] or level[i] > level[i+1] + 3:
#                     safe = False
#                     break
#             if safe:
#                 print(level)
#                 safety_score += 1
#         #increasing
#         elif level[0] < level[1]:
#             safe = True
#             for i in range(0, len(level) - 1):
#                 if level[i] >= level[i+1] or level[i] < level[i+1] - 3:
#                     safe = False
#                     break
#             if safe:
#                 print(level)
#                 safety_score += 1
#         else:
#             continue
#     return safety_score

# print(read_input('input2.txt'))
# print(determine_safety(read_input('input2.txt')))


# part 2
def read_input2(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        return [(list(map(int, line.split())), len(line.split())) for line in lines]

def determine_safety(level, is_decreasing):
    for i in range(0, len(level) - 1):
        if is_decreasing:
            if level[i] <= level[i+1] or level[i] > level[i+1] + 3:
                return False
        else:
            if level[i] >= level[i+1] or level[i] < level[i+1] - 3:
                return False
    return True

def score_safety(input_list):
    safety_score = 0
    for level_pair in input_list:
        level = level_pair[0]
        
        if level[0] > level[1]:
            if determine_safety(level, True):
                print(level)
                safety_score += 1
            elif len(level) == level_pair[1]:
                for i in range(len(level)):
                    new_level = level.copy()
                    new_level.pop(i)
                    if determine_safety(new_level, True):
                        print(new_level)
                        safety_score += 1
                    else:
                        continue
        elif level[0] < level[1]:
            if determine_safety(level, False):
                print(level)
                safety_score += 1
            elif len(level) == level_pair[1]:
                for i in range(len(level)):
                    new_level = level.copy()
                    new_level.pop(i)
                    if determine_safety(new_level, False):
                        print(new_level)
                        safety_score += 1
                    else:
                        continue
    
    return safety_score

print(read_input2('input2.txt'))
print(score_safety(read_input2('input2.txt')))
