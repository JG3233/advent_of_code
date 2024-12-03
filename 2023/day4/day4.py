# part 1
def read_file_to_card_details(filename):
    card_details = []
    with open(filename, 'r') as file:
        card_number = 1
        for line in file:
            # Remove newline character and convert line to list of characters
            contents = line.split(':')
            winning_numbers, player_numbers = contents[1].split('|')
            winning_numbers = [int(num) for num in winning_numbers.split()]
            player_numbers = [int(num) for num in player_numbers.split()]
            card_details.append((card_number, winning_numbers, player_numbers))
            card_number += 1
    return card_details

def check_cards_for_win(card_details):
    total_score = 0
    for card in card_details:
        score = 0
        for number in card[2]:
            if number in card[1]:
                if score == 0:
                    score = 1
                else:
                    score *= 2
        total_score += score
    return total_score
# Read the file
# card_details = read_file_to_card_details('input4.txt')
# print(card_details)
# print(check_cards_for_win(card_details))

# part 2
def read_file_to_card_details2(filename):
    card_details = {}
    with open(filename, 'r') as file:
        card_number = 1
        for line in file:
            # Remove newline character and convert line to list of characters
            contents = line.split(':')
            winning_numbers, player_numbers = contents[1].split('|')
            winning_numbers = [int(num) for num in winning_numbers.split()]
            player_numbers = [int(num) for num in player_numbers.split()]
            card_details[card_number] = [winning_numbers, player_numbers, 1]
            card_number += 1
    return card_details

def check_cards_for_win2(card_details):
    for card, values in card_details.items():
        for i in range(values[2]):
            copies_won = 0
            # print(card, values)
            for number in values[1]:
                if number in values[0]:
                    copies_won += 1
            # print(copies_won)
            for i in range(copies_won):
                # print(card_details[card + 1 + i][2])
                card_details[card + 1 + i][2] += 1
    return card_details
        

card_details = read_file_to_card_details2('input4.txt')
# print(card_details)
final_details = check_cards_for_win2(card_details)
final_card_count = 0
for card, values in final_details.items():
    final_card_count += values[2]
print(final_card_count)

