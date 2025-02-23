from operator import truediv
from data import Card
from data import deck
from data import shuffle
from data import rank_order
# from hand import Hand


def sort_ranks(hand:list[Card]):
    hand.sort(key=lambda card: card.get_rank(), reverse=True)
    return hand


def hand_type(hand:list[Card]):
    hand = sort_ranks(hand)
    #figures out if the len of the amount of suits in set are only 1 or not
    if_flush = len(set(card.suit for card in hand)) == 1
    #checks to see all values are in descending order
    rank_values = [card.get_rank() for card in hand]
    if_straight = all(rank_values[i] - 1 == rank_values[i + 1] for i in range(4)) or rank_values == [14,5,4,3,2]
                                                                                #end bit checks for low straight


    rank_counts = {}
    for card in hand:
        value = card.get_rank()
        if value in rank_counts:
            rank_counts[value] += 1
        else:
            rank_counts[value] = 1

    sorted_rank_counts = sorted(rank_counts.values(), reverse=True)

    if sorted_rank_counts == [1, 1, 1, 1, 1]:
        if if_straight and if_flush and rank_counts == {10:1, 11:1, 12:1, 13:1, 14:1}:
            return "Royal Flush"
        if if_straight and if_flush:
            return "Straight Flush"
        if if_flush:
            return "Flush"
        if if_straight or rank_counts == {2:1, 3:1, 4:1, 5:1, 14:1}:
            return "Straight"
        return f"High {hand[0].rank}"

    if sorted_rank_counts == [4, 1]:
        return "Four of a Kind"
    if sorted_rank_counts == [3, 2]:
        return "Full House"
    if sorted_rank_counts == [3, 1, 1]:
        return "Three of a Kind"
    if sorted_rank_counts == [2, 2, 1]:
        return "Two Pair"
    if sorted_rank_counts == [2, 1, 1, 1]:
        return "Pair"
    return "Unknown hand"

hand = shuffle(deck)[:5]
print(hand_type(hand))



