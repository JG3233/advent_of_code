# # part 1

# def read_trails(filename):
#     """
#     Reads a text file and creates a 2D map where each location stores the value from the input file.

#     Args:
#         filename (str): The name of the text file to be read.

#     Returns:
#         list[list[int]]: A 2D list representing the map.
#     """

#     # Initialize an empty list to store the map data
#     trail_map = []
#     trailheads = []

#     try:
#         # Attempt to open the specified file in read mode
#         with open(filename, 'r') as file:
#             # Iterate over each line in the file
#             for index, line in enumerate(file):
#                 # Strip leading/trailing whitespaces
#                 row_values = [val for val in line.strip()]
#                 for row_index, num in enumerate(row_values):
#                     if num.isdigit() and int(num) == 0:
#                         trailheads.append((index, row_index))
#                 # Append the row values to the trail map
#                 trail_map.append(row_values)

#     except FileNotFoundError:
#         print(f"File '{filename}' not found.")
#         return None

#     return trail_map, trailheads

# def track_trails(current, trail_data, full_trails):
#     if trail_data[current[0]][current[1]].isdigit() and int(trail_data[current[0]][current[1]]) == 9:
#         print('YAY', full_trails, current, trail_data[current[0]][current[1]])
#         if current not in full_trails:
#             full_trails.append(current)
#         return full_trails
#     else:
#         print(current)
#         possible_steps = [(current[0], current[1]-1), (current[0], current[1]+1), (current[0]-1,current[1]), (current[0]+1,current[1])]
#         print(possible_steps)
#         for s in possible_steps:
#             if s[0] < 0 or s[1] < 0 or s[0] >= len(trail_data[0]) or s[1] >= len(trail_data[0]) or not trail_data[s[0]][s[1]].isdigit():
#                 continue
#             elif int(trail_data[s[0]][s[1]]) == int(trail_data[current[0]][current[1]]) + 1:
#                 print(s)
#                 full_trails = track_trails(s, trail_data, full_trails)
#             else:
#                 continue
#         return full_trails


# # Example usage:
# if __name__ == "__main__":
#     total_score = 0
#     filename = "input10.txt"
#     trail_data, trailheads = read_trails(filename)
    
#     if trail_data is not None:
#         print(trail_data)
#         print(trailheads)
#         for t in trailheads:
#             trail_score = track_trails(t, trail_data, [])
#             if trail_score:
#                 total_score += len(trail_score)
#         print(total_score)

# part 2

# part 1

def read_trails(filename):
    trail_map = []
    trailheads = []

    try:
        with open(filename, 'r') as file:
            for index, line in enumerate(file):
                row_values = [val for val in line.strip()]
                for row_index, num in enumerate(row_values):
                    if num.isdigit() and int(num) == 0:
                        trailheads.append((index, row_index))
                trail_map.append(row_values)

    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return None

    return trail_map, trailheads

def track_trails(current, trail_data, rating):
    if trail_data[current[0]][current[1]].isdigit() and int(trail_data[current[0]][current[1]]) == 9:
        print('YAY', rating, current, trail_data[current[0]][current[1]])
        return rating + 1
    else:
        print(current)
        possible_steps = [(current[0], current[1]-1), (current[0], current[1]+1), (current[0]-1,current[1]), (current[0]+1,current[1])]
        print(possible_steps)
        total_rating = 0
        for s in possible_steps:
            if s[0] < 0 or s[1] < 0 or s[0] >= len(trail_data[0]) or s[1] >= len(trail_data[0]) or not trail_data[s[0]][s[1]].isdigit():
                continue
            elif int(trail_data[s[0]][s[1]]) == int(trail_data[current[0]][current[1]]) + 1:
                print(s)
                total_rating += track_trails(s, trail_data, rating)
            else:
                continue
        return total_rating

if __name__ == "__main__":
    total_score = 0
    filename = "input10.txt"
    trail_data, trailheads = read_trails(filename)
    
    if trail_data is not None:
        print(trail_data)
        print(trailheads)
        for t in trailheads:
            trail_score = track_trails(t, trail_data, 0)
            if trail_score:
                total_score += trail_score
        print(total_score)