#  # part 1
# def read_hand_stats(file):
#     with open(file, 'r') as f:
#         lines = f.readlines()
#         hands = [line.split() for line in lines]
#     return hands

# def calc_hand_stats(hands):
#     five_of_a_kind = []
#     four_of_a_kind = []
#     full_house = []
#     three_of_a_kind = []
#     two_pair = []
#     pair = []
#     high_card = []
#     for hand in hands:
#         cards = hand[0]
#         hand_set = list(set(cards))
#         if len(hand_set) == 1:
#             five_of_a_kind.append(hand)
#         elif len(hand_set) == 2:
#             found = False
#             for card in hand_set:
#                 if cards.count(card) == 4:
#                     four_of_a_kind.append(hand)
#                     found = True
#             if not found:
#                 full_house.append(hand)
#         elif len(hand_set) == 3:
#             found = False
#             for card in hand_set:
#                 if cards.count(card) == 3:
#                     three_of_a_kind.append(hand)
#                     found = True
#             if not found:
#                 two_pair.append(hand)
#         elif len(hand_set) == 4:
#             pair.append(hand)
#         else:
#             high_card.append(hand)
            
#     return sort_hands(high_card) + sort_hands(pair) + sort_hands(two_pair) + sort_hands(three_of_a_kind) + sort_hands(full_house) + sort_hands(four_of_a_kind) + sort_hands(five_of_a_kind)

# def sort_hands(hands):
#     card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
#                    '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    
#     def compare_hands(hand):
#         return [card_values[card] for card in hand[0]]
    
#     return sorted(hands, key=compare_hands)
    

# def calc_hands(ordered_hands):
#     score = 0
#     for index, hand in enumerate(ordered_hands):
#         # print(hand, index)
#         score += int(hand[1]) * (index + 1)
#     return score

# # print(read_hand_stats('input7.txt'))
# ordered_hands = calc_hand_stats(read_hand_stats('input7.txt'))
# print(ordered_hands)
# print(calc_hands(ordered_hands))

 # part 2
def read_hand_stats2(file):
    with open(file, 'r') as f:
        lines = f.readlines()
        hands = [line.split() for line in lines]
    return hands

def calc_hand_stats2(hands):
    five_of_a_kind = []
    four_of_a_kind = []
    full_house = []
    three_of_a_kind = []
    two_pair = []
    pair = []
    high_card = []
    for hand in hands:
        cards = hand[0]
        jacks = cards.count('J')
        cards = cards.replace('J', '')
        hand_set = list(set(cards))
        if len(hand_set) == 1 or jacks == 5:
            five_of_a_kind.append(hand)
        elif len(hand_set) == 2:
            if jacks == 0:
                found = False
                for card in hand_set:
                    if cards.count(card) == 4:
                        four_of_a_kind.append(hand)
                        found = True
                if not found:
                    full_house.append(hand)
            elif jacks == 1:
                found = False
                for card in hand_set:
                    if cards.count(card) == 3:
                        four_of_a_kind.append(hand)
                        found = True
                if not found:
                    full_house.append(hand)
            else:
                four_of_a_kind.append(hand)
        elif len(hand_set) == 3:
            if jacks == 0:
                found = False
                for card in hand_set:
                    if cards.count(card) == 3:
                        three_of_a_kind.append(hand)
                        found = True
                if not found:
                    two_pair.append(hand)
            else:
                three_of_a_kind.append(hand)
        elif len(hand_set) == 4:
            pair.append(hand)
        else:
            high_card.append(hand)
            
    return sort_hands2(high_card) + sort_hands2(pair) + sort_hands2(two_pair) + sort_hands2(three_of_a_kind) + sort_hands2(full_house) + sort_hands2(four_of_a_kind) + sort_hands2(five_of_a_kind)

def sort_hands2(hands):
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, 
                   '9': 9, 'T': 10, 'J': 1, 'Q': 12, 'K': 13, 'A': 14}
    
    def compare_hands(hand):
        return [card_values[card] for card in hand[0]]
    
    return sorted(hands, key=compare_hands)
    

def calc_hands2(ordered_hands):
    score = 0
    for index, hand in enumerate(ordered_hands):
        # print(hand, index)
        score += int(hand[1]) * (index + 1)
    return score

# print(read_hand_stats('input7.txt'))
ordered_hands = calc_hand_stats2(read_hand_stats2('input7.txt'))
# print(ordered_hands)
print(calc_hands2(ordered_hands))