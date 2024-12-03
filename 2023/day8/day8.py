# # part 1
# def read_file(file_path):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         directions = lines[0].strip().split(' ')[0]
#         nodes = {}
#         for line in lines[1:]:
#             line = line.strip()
#             if '=' in line:
#                 line = line.split('=')
#                 temp = line[1].split(',')
#                 nodes[line[0].strip()] = (temp[0][2:].strip(), temp[1][:-1].strip())
#         return directions, nodes
    
# def follow_directions(directions, nodes):
#     current_node = 'AAA'
#     steps = 0
#     while current_node != 'ZZZ':
#         for direction in directions:
#             if direction == 'L':
#                 print(nodes[current_node][0])
#                 current_node = nodes[current_node][0]
#             else:
#                 print(nodes[current_node][1])
#                 current_node = nodes[current_node][1]
#             steps += 1
#     return steps
        
            
# directions, nodes = read_file('day8/input8.txt')
# print(directions, nodes)
# print(follow_directions(directions, nodes))


# part 2
def read_file2(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        directions = lines[0].strip().split(' ')[0]
        nodes = {}
        for line in lines[1:]:
            line = line.strip()
            if '=' in line:
                line = line.split('=')
                temp = line[1].split(',')
                nodes[line[0].strip()] = (temp[0][2:].strip(), temp[1][:-1].strip())
        return directions, nodes
    
def follow_directions2(directions, nodes):
    current_nodes = [node for node in nodes if node[-1] == 'A']
    end_nodes = [node for node in nodes if node[-1] == 'Z']
    print('starting with', current_nodes, 'ending with', end_nodes)
    steps = 0
    while not check_winner(current_nodes, end_nodes):
        for index, node in enumerate(current_nodes):
            for direction in directions:
                if direction == 'L':
                    # print(nodes[current_nodes[index]][0])
                    current_nodes[index] = nodes[current_nodes[index]][0]
                else:
                    # print(nodes[current_nodes[index]][1])
                    current_nodes[index] = nodes[current_nodes[index]][1]
                steps += 1
    return steps/len(current_nodes)
        
def check_winner(current_nodes, end_nodes):
    for node in current_nodes:
        if node not in end_nodes:
            return False
    return True
            
directions, nodes = read_file2('day8/input8.txt')
# print(directions, nodes)
print(follow_directions2(directions, nodes))