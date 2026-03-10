map_val_score = {
    '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14
}

def high_card(hand: list) -> int:
    '''
    returns the total score of all cards
    '''
    sorted_hand = ['1H'] + sorted(hand, key=lambda card: -1 * map_val_score[card[0]]) + ['1H']
    total = 0
    for i in range(1, len(sorted_hand) - 1):
        if sorted_hand[i - 1][0] == sorted_hand[i][0] or sorted_hand[i + 1][0] == sorted_hand[i][0]:
            continue 
        total += total * 13 + int(map_val_score[sorted_hand[i][0]])

    return total

def has_pair(hand: list) -> str:
    '''
    return 0 if no pair else, returns the value of the pair
    '''
    sorted_hand = sorted(hand, key=lambda card: map_val_score[card[0]])
    for i in range(len(sorted_hand) - 1):
        if sorted_hand[i][0] == sorted_hand[i+1][0]:
            return sorted_hand[i][0]
    return 0
        
def has_two_pair(hand: list) -> tuple:
    '''
    return 0 if no two pair else, returns the values of the two pair (second_pair , first_pair)
    '''
    first_pair = has_pair(hand)
    if first_pair == 0:
        return 0
    hand_no_first_pair = [card for card in hand if card[0] != first_pair]
    sorted_hand = sorted(hand_no_first_pair , key=lambda card: map_val_score[card[0]])

    for i in range(len(sorted_hand) - 1):
        if sorted_hand[i][0] == sorted_hand[i+1][0]:
            return (sorted_hand[i][0], first_pair)
    return 0
        
def has_three_of_a_kind(hand: list) -> str:
    '''
    return 0 if no three of a kind else, returns the value of the pair
    '''
    sorted_hand = sorted(hand, key=lambda card: card[0])
    for i in range(len(sorted_hand) - 2):
        if sorted_hand[i][0] == sorted_hand[i+1][0] == sorted_hand[i+2][0]:
            return sorted_hand[i][0]
    return 0

def has_straight(hand: list) -> str:
    '''
    return 0 if no straight else, returns the highest value of the straight
    '''
    sorted_hand = sorted(hand, key=lambda card: map_val_score[card[0]])
    for i in range(len(sorted_hand) - 1):
        if map_val_score[sorted_hand[i][0]] + 1 != map_val_score[sorted_hand[i+1][0]]:
            return 0
    
    return sorted_hand[4][0]

def has_flush(hand: list) -> str:
    '''
    return 0 if no flush else, returns the highest value of the flush
    '''
    sorted_hand = sorted(hand, key=lambda card: card[1])

    if sorted_hand[0][1] == sorted_hand[4][1]:
        sorted_hand = sorted(hand, key=lambda card: map_val_score[card[0]])
        return sorted_hand[4][0]
    else:
        return 0

def has_full_house(hand: list) -> tuple:
    '''
    return 0 if no full house else, returns the values -> (three_of_a_kind, pair)
    '''
    three_of_a_kind_card = has_three_of_a_kind(hand)
    if three_of_a_kind_card == 0:
        return 0
    
    hand_no_three_of_a_kind = [card for card in hand if card[0] != three_of_a_kind_card]

    if len(hand_no_three_of_a_kind) < 2:
        return 0

    if hand_no_three_of_a_kind[0][0] == hand_no_three_of_a_kind[1][0]:
        return (three_of_a_kind_card, hand_no_three_of_a_kind[0][0])
    else:
        return 0
    
def has_four_of_a_kind(hand: list) -> str:
    '''
    return 0 if no four of a kind else, returns the value of the four of a kind
    '''
    sorted_hand = sorted(hand, key=lambda card: map_val_score[card[0]])

    if sorted_hand[0][0] == sorted_hand[3][0] or sorted_hand[1][0] == sorted_hand[4][0]:
        return sorted_hand[2][0]
    else:
        return 0 
    
def has_straight_flush(hand: list) -> str:
    straight = has_straight(hand)
    flush = has_flush(hand)
    if flush and straight:
        return flush if map_val_score[flush] > map_val_score[straight] else straight

    return 0

def has_royal_flush(hand: list) -> str:
    straight = has_straight(hand)
    flush = has_flush(hand)
    if flush and straight:
        highest_val =  flush if map_val_score[flush] > map_val_score[straight] else straight
        if highest_val == 'A':
            return 'A'

    return 0

map_hand_score = [
    (has_pair, 1000000), (has_two_pair, 2000000), (has_three_of_a_kind, 3000000), (has_straight, 4000000), (has_flush, 5000000),
    (has_full_house, 6000000), (has_four_of_a_kind, 8000000), (has_straight_flush, 9000000), (has_royal_flush, 10000000)
]

def calculate(hand: list) -> int:
    for rank in reversed(map_hand_score):
        result = rank[0](hand)
        if result != 0:
            if type(result) == tuple or rank[0] == has_full_house or rank[0] == has_two_pair:
                return rank[1] + map_val_score[result[0]] * 13 + map_val_score[result[1]] + high_card(hand)
            return rank[1] + map_val_score[result] * 13**4 + high_card(hand)

    return high_card(hand)
              
def compare_hands(hand1: list, hand2: list) -> int:
    hand1_score = calculate(hand1)
    hand2_score = calculate(hand2)
    print(hand1, hand1_score,   hand2, hand2_score)
    if hand1_score == hand2_score:
        return 0
    elif hand1_score > hand2_score:
        return 1
    else:
        return -1 
    
def parse_txt():
    counter = 0
    player_2 = 0
    with open('54_poker.txt', 'r') as file:
        for line_number, line in enumerate(file, 1):
            line_in_list = line.rstrip().split()
            hand1 = line_in_list[:5]
            hand2 = line_in_list[5:]
            result = compare_hands(hand1, hand2)
            if result == 1:
                counter += 1
            if result == -1:
                player_2 += 1

    print(counter)
    print(player_2)

# print(high_card(['6H', '6C', 'AC', 'KD', '2S']))
# print(high_card(['6H', '6C', 'AC', 'QD', 'JS']))
# print(high_card(['7H', '7C', '3C', '3D', '3S']))
parse_txt()