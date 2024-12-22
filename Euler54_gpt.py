from collections import Counter

def card_value(card):
    """Returns the value of the card for comparison."""
    values = '23456789TJQKA'
    return values.index(card[0])

def hand_rank(hand):
    """Returns a value representing the rank of the hand."""
    # Sort the hand by card value
    sorted_hand = sorted(hand, key=card_value)
    value_counts = Counter(card[0] for card in sorted_hand)
    
    # Get counts and values, sorted by count first, then card value
    values_by_count = sorted(value_counts.items(), 
                           key=lambda x: (-x[1], -card_value(x[0])))
    counts = [count for _, count in values_by_count]
    values = [value for value, _ in values_by_count]

    is_flush = len(set(card[1] for card in hand)) == 1
    
    # Check for straight using original card values
    card_values = sorted([card_value(card) for card in hand])
    is_straight = len(set(card_values)) == 5 and max(card_values) - min(card_values) == 4

    if is_straight and is_flush and 'A' in value_counts:
        return (10,)  # Royal Flush
    elif is_straight and is_flush:
        return (9, max(card_value(card) for card in hand))  # Straight Flush
    elif counts == [4, 1]:
        return (8, card_value(values[0]), card_value(values[1]))  # Four of a Kind
    elif counts == [3, 2]:
        return (7, card_value(values[0]), card_value(values[1]))  # Full House
    elif is_flush:
        return (6,) + tuple(sorted([card_value(card) for card in hand], reverse=True))  # Flush
    elif is_straight:
        return (5, max(card_value(card) for card in hand))  # Straight
    elif counts == [3, 1, 1]:
        return (4, card_value(values[0])) + tuple(sorted([card_value(c) for c in values[1:]], reverse=True))  # Three of a Kind
    elif counts == [2, 2, 1]:
        return (3, max(card_value(values[0]), card_value(values[1])), 
                min(card_value(values[0]), card_value(values[1])), 
                card_value(values[2]))  # Two Pair
    elif counts == [2, 1, 1, 1]:
        return (2, card_value(values[0])) + tuple(sorted([card_value(c) for c in values[1:]], reverse=True))  # One Pair
    else:
        return (1,) + tuple(sorted([card_value(card) for card in hand], reverse=True))  # High Card

def winner(hand1, hand2):
    """Returns True if Player 1 wins, False if Player 2 wins."""
    return hand_rank(hand1) > hand_rank(hand2)

def count_player_1_wins(filename):
    """Counts how many hands Player 1 wins."""
    player_1_wins = 0
    with open(filename, 'r') as file:
        for line in file:
            cards = line.strip().split()
            player_1_hand = cards[:5]
            player_2_hand = cards[5:]
            if winner(player_1_hand, player_2_hand):
                player_1_wins += 1
    return player_1_wins

# Example usage
wins = count_player_1_wins('p054_poker.txt')
print(f'Player 1 wins: {wins}')