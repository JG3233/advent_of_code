# part 1
# def read_input(file_name):
#     with open(file_name, 'r') as file:
#         return file.read().splitlines()
    
# def search_matrix(matrix):
#     matches = 0
#     word = 'XMAS'
#     for row in range(len(matrix)):
#         for col in range(len(matrix[row])):
#             if 'X' in matrix[row][col]:
#                 # forwards
#                 if col+3 < len(matrix[row]):
#                     temp_word = matrix[row][col] + matrix[row][col+1] + matrix[row][col+2] + matrix[row][col+3]
#                     if temp_word == word:
#                         matches += 1
#                 # backwards
#                 if col-3 >= 0:
#                     temp_word = matrix[row][col] + matrix[row][col-1] + matrix[row][col-2] + matrix[row][col-3]
#                     if temp_word == word:
#                         matches += 1
#                 # down
#                 if row+3 < len(matrix):
#                     temp_word = matrix[row][col] + matrix[row+1][col] + matrix[row+2][col] + matrix[row+3][col]
#                     if temp_word == word:
#                         matches += 1
#                 #up
#                 if row-3 >= 0:
#                     temp_word = matrix[row][col] + matrix[row-1][col] + matrix[row-2][col] + matrix[row-3][col]
#                     if temp_word == word:
#                         matches += 1
#                 #down and forwards
#                 if col+3 < len(matrix[row]) and row+3 < len(matrix):
#                     temp_word = matrix[row][col] + matrix[row+1][col+1] + matrix[row+2][col+2] + matrix[row+3][col+3]
#                     if temp_word == word:
#                         matches += 1
#                 #down and backwards
#                 if col-3 >= 0 and row+3 < len(matrix):
#                     temp_word = matrix[row][col] + matrix[row+1][col-1] + matrix[row+2][col-2] + matrix[row+3][col-3]
#                     if temp_word == word:
#                         matches += 1
#                 #up and forwards
#                 if col+3 < len(matrix[row]) and row-3 >= 0:
#                     temp_word = matrix[row][col] + matrix[row-1][col+1] + matrix[row-2][col+2] + matrix[row-3][col+3]
#                     if temp_word == word:
#                         matches += 1
#                 #up and backwards
#                 if col-3 >= 0 and row-3 >= 0:
#                     temp_word = matrix[row][col] + matrix[row-1][col-1] + matrix[row-2][col-2] + matrix[row-3][col-3]
#                     if temp_word == word:
#                         matches += 1
#     return matches 

# matrix = read_input('input4.txt')
# print(search_matrix(matrix))
# part 2    
def read_input2(file_name):
    with open(file_name, 'r') as file:
        return file.read().splitlines()
    
def search_matrix2(matrix):
    matches = 0
    word = 'MAS'
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if 'M' in matrix[row][col]:
                # forwards and downwards
                if col+2 < len(matrix[row]) and row+2 < len(matrix):
                    temp_word = matrix[row][col] + matrix[row+1][col+1] + matrix[row+2][col+2]
                    if temp_word == word:
                        # check second mas
                        if (matrix[row+2][col] == 'M' and matrix[row][col+2] == 'S') or (matrix[row+2][col] == 'S' and matrix[row][col+2] == 'M'):
                            matches += 1
                            print(f'{temp_word} match found at {row}, {col}')
                # forwards and upwards
                if col+2 < len(matrix[row]) and row-2 >= 0:
                    temp_word = matrix[row][col] + matrix[row-1][col+1] + matrix[row-2][col+2]
                    if temp_word == word:
                        # check second mas
                        if (matrix[row-2][col] == 'M' and matrix[row][col+2] == 'S') or (matrix[row-2][col] == 'S' and matrix[row][col+2] == 'M'):
                            matches += 1
                            print(f'{temp_word} match found at {row}, {col}')
                # backwards and downwards
                if col-2 >= 0 and row+2 < len(matrix):
                    temp_word = matrix[row][col] + matrix[row+1][col-1] + matrix[row+2][col-2]
                    if temp_word == word:
                        # check second mas
                        if (matrix[row+2][col] == 'M' and matrix[row][col-2] == 'S') or (matrix[row+2][col] == 'S' and matrix[row][col-2] == 'M'):
                            matches += 1
                            print(f'{temp_word} match found at {row}, {col}')
                # backwards and upwards
                if col-2 >= 0 and row-2 >= 0:
                    temp_word = matrix[row][col] + matrix[row-1][col-1] + matrix[row-2][col-2]
                    if temp_word == word:
                        # check second mas
                        if (matrix[row-2][col] == 'M' and matrix[row][col-2] == 'S') or (matrix[row-2][col] == 'S' and matrix[row][col-2] == 'M'):
                            matches += 1
                            print(f'{temp_word} match found at {row}, {col}')
    return matches 

matrix = read_input2('input4.txt')
print(search_matrix2(matrix)/2)