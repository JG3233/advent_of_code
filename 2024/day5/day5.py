# # part 1
# def read_input(file_name):
#     with open(file_name, 'r') as file:
#         file_content = file.read()
#         ordering_rules, print_jobs = file_content.split('\n\n')
#         ordering_rules = ordering_rules.split('\n')
#         print_jobs = print_jobs.split('\n')
#         rules_dict = {}
#         for rule in ordering_rules:
#             rule = rule.split('|')
#             if rule[0] not in rules_dict:
#                 rules_dict[rule[0]] = []
#             rules_dict[rule[0]].append(rule[1])
#         new_print_jobs_list = []
#         for job in print_jobs:
#             new_print_jobs = job.split(',')
#             new_print_jobs_list.append(new_print_jobs)
#         return rules_dict, new_print_jobs_list
        
# def determine_order(rules_dict, print_jobs):
#     correct_order   = []
#     for job in print_jobs:
#         out_of_order = False
#         for page in range(len(job)):
#             next_pages = job[page:]
#             for next_page in next_pages:
#                 if next_page in rules_dict and job[page] in rules_dict[next_page]:
#                     out_of_order = True
#                     break
#             if out_of_order:
#                 break
#         if not out_of_order:
#             correct_order.append(job)
#     return correct_order

# def calculate_score(correct_order):
#     score = 0
#     for job in correct_order:
#         score += int(job[int(len(job)/2)])
#     return score
        
# rules_dict, print_jobs = read_input('input5.txt')
# correct_order = determine_order(rules_dict, print_jobs)
# print(correct_order)
# print(calculate_score(correct_order))

# part 2
# part 1
def read_input(file_name):
    with open(file_name, 'r') as file:
        file_content = file.read()
        ordering_rules, print_jobs = file_content.split('\n\n')
        ordering_rules = ordering_rules.split('\n')
        print_jobs = print_jobs.split('\n')
        rules_dict = {}
        for rule in ordering_rules:
            rule = rule.split('|')
            if rule[0] not in rules_dict:
                rules_dict[rule[0]] = []
            rules_dict[rule[0]].append(rule[1])
        new_print_jobs_list = []
        for job in print_jobs:
            new_print_jobs = job.split(',')
            new_print_jobs_list.append(new_print_jobs)
        return rules_dict, new_print_jobs_list
        
def determine_order(rules_dict, print_jobs):
    correct_order   = []
    incorrect_order = []
    for job in print_jobs:
        out_of_order = False
        for page in range(len(job)):
            next_pages = job[page:]
            for next_page in next_pages:
                if next_page in rules_dict and job[page] in rules_dict[next_page]:
                    out_of_order = True
                    break
            if out_of_order:
                break
        if not out_of_order:
            correct_order.append(job)
        else:
            incorrect_order.append(job)
    return correct_order, incorrect_order

def reorder_incorrect_order(rules_dict, incorrect_order):
    for job in incorrect_order:
        out_of_order = True
        while out_of_order:
            out_of_order = False
            for page in range(len(job)):
                next_pages = job[page:]
                for next_page in next_pages:
                    if next_page in rules_dict and job[page] in rules_dict[next_page]:
                        actual_index = page + next_pages.index(next_page)
                        job[page], job[actual_index] = job[actual_index], job[page]
                        out_of_order = True
                        break
                if out_of_order:
                    break
            if not out_of_order:
                break
    return incorrect_order

def calculate_score(incorrect_order):
    score = 0
    for job in incorrect_order:
        score += int(job[int(len(job)/2)])
    return score
        
rules_dict, print_jobs = read_input('input5.txt')
correct_order, incorrect_order = determine_order(rules_dict, print_jobs)
reordered_incorrect_order = reorder_incorrect_order(rules_dict, incorrect_order)
print(reordered_incorrect_order)
print(calculate_score(reordered_incorrect_order))
