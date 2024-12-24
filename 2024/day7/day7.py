# part 1
def read_calibrations(file):
    calibrations = []
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            target, numbers = line.split(':')
            numbers = numbers.split()
            calibrations.append((target, numbers))
    return calibrations

from itertools import product

def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i, op in enumerate(operators):
        if op == '+':
            result += numbers[i + 1]
        elif op == '*':
            result *= numbers[i + 1]
        else:  # op == '&' (concatenation)
            result = int(str(result) + str(numbers[i + 1]))
    return result

def evaluate_calibration(calibration):
    target, numbers = calibration
    numbers = [int(number) for number in numbers]
    target = int(target)
    
    # Add '&' to possible operators
    possible_ops = list(product(['+', '*', '&'], repeat=len(numbers)-1))
    
    for ops in possible_ops:
        if evaluate_expression(numbers, ops) == target:
            return target
    
    return None

def sum_true_numbers(target_numbers):
    sum = 0
    for number in target_numbers:
        sum += number
    return sum

calibrations = read_calibrations('input7.txt')

print(calibrations)

target_numbers = []
for calibration in calibrations:
    result = evaluate_calibration(calibration)
    if result:
        target_numbers.append(result)

print(sum_true_numbers(target_numbers))
