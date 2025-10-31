
def parse_txt():
    pass

map_val_score = {
    '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14
}

def compare_hands(hand1: list, hand2: list) -> int:
    hand1_score = calculate(hand1)
    hand2_score = calculate(hand2)
    pass

def calculate(hand: list) -> int:
    pass

def has_pair(hand: list) -> str:
    '''
    return 0 if no pair else, returns the value of the pair
    '''
    sorted_hand = sorted(hand, key=lambda card: map_val_score[card[0]])
    for i in range(len(sorted_hand) - 1):
        if sorted_hand[i][0] == sorted_hand[i+1][0]:
            return sorted_hand[i][0]
        
def has_two_pair(hand: list) -> tuple:
    '''
    return 0 if no two pair else, returns the values of the two pair
    '''
    first_pair = has_pair(hand)
    if first_pair == 0:
        return 0
    hand_no_first_pair = [card for card in hand if card[0] != first_pair]
    print(hand_no_first_pair)
    sorted_hand = sorted(hand_no_first_pair , key=lambda card: map_val_score[card[0]])

    for i in range(len(sorted_hand) - 1):
        if sorted_hand[i][0] == sorted_hand[i+1][0]:
            return (first_pair, sorted_hand[i][0])
        
def has_three_of_a_kind(hand: list) -> str:
    '''
    return 0 if no three of a kind else, returns the value of the pair
    '''
    sorted_hand = sorted(hand, key=lambda card: card[0])
    for i in range(len(sorted_hand) - 2):
        if sorted_hand[i][0] == sorted_hand[i+1][0] == sorted_hand[i+2][0]:
            return sorted_hand[i][0]

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
        sorted_hand = sorted(hand, key=lambda card: card[0])
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
    
def has_four_of_a_kind(hand: list) -> tuple:
    '''
    return 0 if no four of a kind else, returns the value of the four of a kind
    '''

    sorted_hand = sorted(hand, key=lambda card: card[1])

    if sorted_hand[0][0] == sorted_hand[3][0] or sorted_hand[0][0] == sorted_hand[3][0]:
        return sorted_hand[0][0]
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
        
print(has_straight_flush(['JC', 'QC', 'KC', 'AC', '9C']))