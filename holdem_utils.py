"""
# Functions for Texas Hold'em projects
"""
import random

# Function that generates random Hold'em starting hand.
def deal_hand():
    suit_dict = {0: 's', 1:'c', 2:'h', 3:'d'}
    idx_to_card = {0: "2", 1: "3", 2: "4", 3: "5", 4: "6", 5: "7", 6: "8", 7: "9", 8: "T", 9: "J", 10: "Q", 11: "K", 12: "A"}

    def match_card(num):
        value = idx_to_card[num%13]
        suit = suit_dict[num//13]     
        return f'{value}{suit}'

    card1_idx = random.randint(0, 51)
    while True:
        card2_idx = random.randint(0, 51)
        if card1_idx != card2_idx: break

    card1 = match_card(card1_idx)
    card2 = match_card(card2_idx)
    
    if card2_idx%13 > card1_idx%13:
        return f'{card2}{card1}'
    return f'{card1}{card2}'


# Function that randomly selects both the positions and game-tree position of two players.

def deal_pos():
    positions_dict = {0: "EP", 1: "MP", 2: "CO", 3: "BN", 4: "SB", 5: "BB"}
    tree_dict = {0: "Open", 1: "Facing Open", 2: "Facing 3Bet", 3: "Facing 4Bet"}
    
    pos1 = random.randint(0,5)
    while True:
        pos2 = random.randint(0,5)
        if pos1 != pos2: break
    tree = random.randint(0,3)
    
    if tree in [0, 2]:
        if pos1 > pos2:
            return (tree, positions_dict[pos2], positions_dict[pos1], tree_dict[tree])
    else:
        if pos1 < pos2:
            return (tree, positions_dict[pos2], positions_dict[pos1], tree_dict[tree])
    return (tree, positions_dict[pos1], positions_dict[pos2], tree_dict[tree])


# Function that determines whether a given hand is within a given hand range.
def in_range(hand, handrange): 
    if len(handrange) < 2:
        return False   
    
    if hand[1] == hand[3]:
        hand = f'{hand[0]}{hand[2]}s'
    else:
        hand = f'{hand[0]}{hand[2]}'
        
    hand_list = handrange.split(",")
    
    for entry in hand_list:  
        if entry.split(':')[0] == hand:
            return True
    return False