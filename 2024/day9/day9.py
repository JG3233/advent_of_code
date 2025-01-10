# # part 1
# import math

# def read_disk_map(filename):
#     full_map = []
#     with open(filename, 'r') as f:
#         for i, char in enumerate(f.read()):
#             if i % 2 == 0:
#                 index = math.floor(i / 2)
#                 for j in range(int(char)):
#                     full_map.append(str(index))
#             else:
#                 for j in range(int(char)):
#                     full_map.append('.')
#         return full_map

# def rearrange_map(full_map):
#     map_copy = full_map
#     for i in range(len(map_copy)):
#         if map_copy[i] == '.':
#             for j in range(len(map_copy)-1, i, -1):
#                 if map_copy[j] != '.':
#                     map_copy[i] = map_copy[j]
#                     map_copy[j] = '.'
#                     break
#     return map_copy

# def calc_checksum(map_copy):
#     return sum(int(map_copy[i]) * i for i in range(len(map_copy)) if map_copy[i] != '.')

# og_map = read_disk_map('input9.txt')
# print(og_map)
# fixed_map = rearrange_map(og_map)
# print(fixed_map)
# checksum = calc_checksum(fixed_map)
# print(checksum)

# part 2
import math

def read_disk_map(filename):
    full_map = []
    with open(filename, 'r') as f:
        for i, char in enumerate(f.read()):
            if i % 2 == 0:
                index = math.floor(i / 2)
                for j in range(int(char)):
                    full_map.append(str(index))
            else:
                for j in range(int(char)):
                    full_map.append('.')
        return full_map

def rearrange_map(full_map):
    # start from the end of the list and find the first set of contiguous digits and the length of the set
    map_copy = full_map
    checked_indices = []
    for i in range(len(map_copy)-1, 0, -1):
        copy_found = False
        if map_copy[i] != '.' and map_copy[i] not in checked_indices:
            set_length = 0
            set_start = map_copy[i]
            set_start_index = i
            for j in range(i-1, 0, -1):
                if map_copy[j] != set_start:
                    set_length = i - j  
                    set_start_index = j + 1
                    copy_found = True
                    checked_indices.append(set_start)
                    break
        if copy_found:
            # print(set_start, set_start_index, set_length, map_copy[set_start_index:set_start_index+set_length])
            # find the first set of '.'s that are at least as long as the set of digits
            for k in range(0, i):
                if map_copy[k] == '.':
                    period_length = 0
                    for j in range(k, i):
                        if map_copy[j] != '.':
                            period_length = j - k
                            break
                    # print(period_length)
                    if period_length >= set_length:
                        #swap the set of digits with the set of '.'s
                        for j in range(set_length):
                            map_copy[k+j] = map_copy[set_start_index+j]
                            map_copy[set_start_index+j] = '.'
                        break
        # print(map_copy)
    return map_copy

def calc_checksum(map_copy):
    return sum(int(map_copy[i]) * i for i in range(len(map_copy)) if map_copy[i] != '.')

og_map = read_disk_map('input9.txt')
print(og_map)
fixed_map = rearrange_map(og_map)
print(fixed_map)
checksum = calc_checksum(fixed_map)
print(checksum)