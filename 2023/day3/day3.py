def read_file_to_matrix(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            # Remove newline character and convert line to list of characters
            row = list(line.strip())
            matrix.append(row)
    return matrix

# Read the file
matrix = read_file_to_matrix('input3.txt')

# Example usage:
# Access element at row 0, column 0
# print(matrix[0][0])

# Print dimensions
# print(f"Rows: {len(matrix)}, Columns: {len(matrix[0])}")

# go through each row and each element in the row
# if the element is a symbol, not a number or '.', add it to a list
symbols = []
numbers = []
number_found = False
for index_of_row, row in enumerate(matrix):
    for index_of_element, element in enumerate(row):
        if element not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']:
            symbols.append((element, (index_of_row, index_of_element)))
        if numbers and index_of_element in range(numbers[-1][1][1], numbers[-1][1][2]+1):
            continue
        if element in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            # check the adjacent values until non-number is found
            number_found = element
            for i in range(index_of_element + 1, len(row)):
                if row[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    number_found += row[i]
                    if i == len(row):
                        numbers.append((int(number_found), (index_of_row, index_of_element, i - 1)))
                        print('a', (int(number_found), (index_of_row, index_of_element, i - 1)))
                        if matrix[row + 1]:
                            row = row + 1
                            index_of_element = 0
                            break
                        else:
                            break
                else:
                    print('b', (int(number_found), (index_of_row, index_of_element, i - 1)))
                    numbers.append((int(number_found), (index_of_row, index_of_element, i - 1)))
                    if i == len(row):
                        print('c',(int(number_found), (index_of_row, index_of_element, i - 1)))
                        numbers.append((int(number_found), (index_of_row, index_of_element, i - 1)))
                        if matrix[row + 1]:
                            row = row + 1
                            index_of_element = 0
                            break
                        else:
                            break
                    else:
                        element = row[i]
                        index_of_element = i + 1
                        break
        # else:
        #     if number_found:
        #         numbers.append((int(number_found), (index_of_row, index_of_element)))
        #         element = row[i]
        #         index_of_element = i
        #         continue

print(symbols)
print(numbers)

nums_to_sum = []
for symbol in symbols:
    for num in numbers:
        # directly next door
        if symbol[1][0] == num[1][0] and (symbol[1][1] + 1 == num[1][1] or symbol[1][1] - 1 == num[1][2]):
            nums_to_sum.append(num[0])
            print('a', num[0], symbol, num)
        if symbol[1][0] - 1 == num[1][0] and (symbol[1][1] in range(num[1][1] - 1, num[1][2] + 2)):
            nums_to_sum.append(num[0])
            print('b', num[0], symbol, num)
        if symbol[1][0] + 1 == num[1][0] and (symbol[1][1] in range(num[1][1] - 1, num[1][2] + 2)):
            nums_to_sum.append(num[0])
            print('c', num[0], symbol, num)

print(nums_to_sum)
sum = sum(nums_to_sum)
print(sum)
