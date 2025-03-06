from operator import truediv
from sys import exc_info

import data
from data import Card
from data import deck
from data import shuffle
from data import rank_order



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


def dealer_hand(hand:list[data.Card]):
    return f"Dealer Hand is: {hand_type(hand)}"

def your_hand(hand:list[data.Card]):
    return f"Your Hand is: {hand_type(hand)}"

def get_hand_value(hand:list[data.Card]):
    return hand_value[hand_type(hand)]

def get_dealer_hand_value(hand:list[data.Card]):
    return hand_value[hand_type(hand)]

def win_or_lose(player:list[data.Card],dealer:list[data.Card]):
    your_hand_value = get_hand_value(player)
    dealer_hand_value = get_dealer_hand_value(dealer)

    if dealer_hand_value > your_hand_value:
        return "You Lose"

    elif dealer_hand_value < your_hand_value:
        return "You Win"

    else:
        your_hand_value = sort_ranks(player)
        dealer_hand_value = sort_ranks(dealer)
        y_card = your_hand_value[0]
        d_card = dealer_hand_value[0]
        if y_card.get_rank() > d_card.get_rank():
            return "You Win By Tie Break"
        elif d_card.get_rank() > y_card.get_rank():

            return "You Lose By Tie Break"
        else:
            return "True Tie"


def betting(total:int, bet:int):
    if bet > total:
        print("You cannot bet more chips than you have.")
        return 0
    elif bet == total:
        print("Betting all in with:", bet, "chips")
        return bet
    else:
        print("Betting:", bet, "chips")
        return bet


def play_game(chips:int) -> int:
    shuffled_deck = shuffle(deck)
    winnings = 0

    player = shuffled_deck[:5]
    print("Your Hand is :", sort_ranks(player))

    dealer = shuffled_deck[5:10]
    bet = betting(chips, int(input("How Many Chips Would You Like To Bet?: ")))
    print("-----------------------------------------------------------")
    print(your_hand(player))
    print(dealer_hand(dealer))
    win_or_lose(player,dealer)


    if win_or_lose(player,dealer) == "True Tie":
        winnings = 0
        print("True Tie, Returning Bet")
    elif win_or_lose(player,dealer) == "You Win" or win_or_lose(player, dealer) == "You Win By Tie Break":
        winnings = winnings + bet
        print("Congrats, you won ", winnings, "chips.")
    elif win_or_lose(player, dealer) == "You Win By Tie Break":
        winnings = winnings + bet
        print("Won by Tie Break")
        print("Congrats, you won ", winnings, "chips.")
    elif win_or_lose(player, dealer) == "You Lose":
        winnings = winnings - bet
        print("You Lost ", abs(winnings), "chips.")
    elif win_or_lose(player, dealer) == "You Lose By Tie Break":
        winnings = winnings - bet
        print("Lost by Tie Break")
        print("You Lost ", abs(winnings), "chips.")
    else:
        print("An Error Occurred, Returning Bet")
        winnings = 0

    return winnings




def game_start():

    print("Welcome to High Score Poker")
    chips = 500
    print("You have", chips, "chips.")
    high_score = 0


    while chips > 0:
        winnings = play_game(chips)
        chips += winnings

        if chips > 500 and high_score == 0:
            high_score = chips
        elif chips > high_score:
            high_score = chips
        else:
            high_score = high_score
        print("You have", chips, "chips.")
        print("-----------------------------------------------------------")



    print("You Have Lost All Your Chips.")
    print("Thanks For Playing! Your High Score Was:", high_score)
    print("High Score Poker v0.3")
    print("Developed by Jeremy Lopanec, and Ruben Moulton Huber")











