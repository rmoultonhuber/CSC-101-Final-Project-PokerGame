from operator import truediv
from data import Card
from data import deck
from data import shuffle
from data import rank_order

shuffled_deck = shuffle(deck)
hand = shuffled_deck[:5]
deal_hand = shuffled_deck[5:10]

hand_value = {f'High Card':1, 'Pair':2, 'Two Pair':3, 'Three of a Kind':4, 'Straight':5, 'Flush':6, 'Full House':7,
              'Four of a Kind':8, 'Straight Flush':9, 'Royal Flush':10}



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
        elif if_straight and if_flush:
            return "Straight Flush"
        elif if_flush:
            return "Flush"
        elif if_straight or rank_counts == {2:1, 3:1, 4:1, 5:1, 14:1}:
            return "Straight"
        else:
            return "High Card"



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


def dealer_hand():
    return f"Dealer Hand is: {hand_type(deal_hand)}"

def your_hand():
    return f"Your Hand is: {hand_type(hand)}"

def get_hand_value():
    return hand_value[hand_type(hand)]

def get_dealer_hand_value():
    return hand_value[hand_type(deal_hand)]

def win_or_lose():
    your_hand_value = get_hand_value()
    dealer_hand_value = get_dealer_hand_value()

    if dealer_hand_value > your_hand_value:
        return "You Lose"

    elif dealer_hand_value < your_hand_value:
        return "You Win"

    else:
        print("It's a Draw, Performing Tie Breaker")
        your_hand_value = sort_ranks(hand)
        dealer_hand_value = sort_ranks(deal_hand)
        y_card = your_hand_value[0]
        d_card = dealer_hand_value[0]
        if y_card.rank > d_card.rank:
            return "You Win"
        elif d_card.get_rank() > y_card.get_rank():
            return "You Lose"
        return "True Tie"




print(your_hand())
print(dealer_hand())
print(win_or_lose())




