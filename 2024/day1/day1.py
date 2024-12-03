# part 1

# def read_input(file_path):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         left_list = []
#         right_list = []
#         for line in lines:
#             left, right = line.split()
#             left_list.append(int(left))
#             right_list.append(int(right))
#         return left_list, right_list

# def find_diffs(left_list, right_list):
#     diff = 0
#     for left, right in zip(left_list, right_list):
#         diff += abs(left - right)
#     return diff

# left_list, right_list = read_input('input1.txt')
## print(sorted(left_list))
## print(sorted(right_list))
# print(find_diffs(sorted(left_list), sorted(right_list)))

# part 2

def read_input2(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        left_list = []
        right_list = []
        for line in lines:
            left, right = line.split()
            left_list.append(int(left))
            right_list.append(int(right))
        return left_list, right_list

def find_similarities(left_list, right_list):
    similarity_score = 0
    for left in left_list:
        if left in right_list:
            similarity_score += left * right_list.count(left)
    return similarity_score

left_list, right_list = read_input2('input1.txt')
# print(sorted(left_list))
# print(sorted(right_list))
print(find_similarities(sorted(left_list), sorted(right_list)))
