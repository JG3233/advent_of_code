# # part 1
# import re

# def read_input(file_path):
#     with open(file_path, 'r') as file:
#         file_content = file.read()
#         return re.findall(r'mul\(([\d]+),([\d]+)\)', file_content)

# def mul(instances):
#     total = 0
#     for a, b in instances:
#         total += int(a) * int(b)
#     return total

# instances = read_input('input3.txt')
# print(mul(instances))

# part 2
import re

def read_input2(file_path):
    with open(file_path, 'r') as file:
        file_content = file.read()
        do_matches = re.finditer(r"do\(\)", file_content)
        dont_matches = re.finditer(r"don't\(\)", file_content)
        return do_matches, dont_matches, file_content

def get_slices(do_matches, dont_matches):
    slices = []
    dont_matches_list = list(dont_matches)
    current_dont_match = dont_matches_list[0].start()
    slices.append((0,current_dont_match))
    for do_match in do_matches:
        if do_match.start() > current_dont_match:
            for dont_match in dont_matches_list:
                if dont_match.start() > do_match.start():
                    slices.append((do_match.start(), dont_match.start()))
                    current_dont_match = dont_match.start()
                    break
    slices.append((do_match.start(),None))
    return slices

def mul2(slices, file_content):
    total = 0
    for a, b in slices:
        instances = re.findall(r'mul\(([\d]+),([\d]+)\)', file_content[a:b])
        for a, b in instances:
            total += int(a) * int(b)
    return total

do_matches, dont_matches, file_content = read_input2('input3.txt')
slices = get_slices(do_matches, dont_matches)
print(slices)
print(mul2(slices, file_content))