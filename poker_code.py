from operator import truediv
from sys import exc_info

import data
from data import Card
from data import deck
from data import shuffle
from data import rank_order



hand_value = {f'High Card':1, 'Pair':2, 'Two Pair':3, 'Three of a Kind':4, 'Straight':5, 'Flush':6, 'Full House':7,
              'Four of a Kind':8, 'Straight Flush':9, 'Royal Flush':10}


# Sorts a hand of five cards in order of descending rank.
# Input = list of Cards, Output = list of Cards
# Created by Jeremy
def sort_ranks(hand:list[Card]):
    hand.sort(key=lambda card: card.get_rank(), reverse=True)
    return hand


# Determines the highest type of the hand of the input hand.
# Input = list of Cards, Output = string
# Created by Jeremy
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
    return "Unknown Hand"


# Determines the type of hand held by the dealer.
# Input = list of Cards, Output = string
# Created by Jeremy, modified by Ruben
def dealer_hand(hand:list[data.Card]):
    return f"Dealer Hand is: {hand_type(hand)}"

# Determines the type of hand held by the player.
# Input = list of Cards, Output = string
# Created by Jeremy, modified by Ruben
def your_hand(hand:list[data.Card]):
    return f"Your Hand is: {hand_type(hand)}"

# Determines the hand value held by the player by finding its type in a dictionary of hand values.
# Input = list of Cards, Output = int
# Created by Jeremy, modified by Ruben
def get_hand_value(hand:list[data.Card]):
    return hand_value[hand_type(hand)]

# Compares the hand values of the dealer and the player and determines who wins the round.
# Input = Two lists of Cards, Output = string
# Created by Jeremy, modified by Ruben
def win_or_lose(player:list[data.Card],dealer:list[data.Card]):
    your_hand_value = get_hand_value(player)
    dealer_hand_value = get_hand_value(dealer)

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


# Determines if the bet is a valid amount that the player has. Will display a special message if the bet is all in.
# Input = two ints, output = int
# Created by Ruben
def betting(total:int, bet:int):
    if bet > total:
        print("You cannot bet more chips than you have.")
        return 0
    elif bet == total:
        print("Betting all in with:", bet, "chips")
        return bet

    elif bet < 0:
        print("You cannot bet negative chips, setting bet to 0")
        return 0

    else:
        print("Betting:", bet, "chips")
        return bet


# The main game function, call necessary functions to determine who wins the round.
# If player wins, awards the player with double the bet, if the dealer wins the player loses the bet,
# if there is a tie, returns the bet to the player.
# Input = int, output = int
# Created by Ruben, modified by Jeremy
def play_game(chips:int) -> int:
    shuffled_deck = shuffle(deck)
    winnings = 0

    player = shuffled_deck[:5]
    print("Your Hand is :", sort_ranks(player))

    dealer = shuffled_deck[5:10]
    try:
        bet = betting(chips, int(input("How Many Chips Would You Like To Bet?: ")))

    except ValueError:
        print("Please only input a number for your bet.")
        print("Setting bet as 0 chips.")
        bet = 0

    print("-----------------------------------------------------------")
    print(your_hand(player))
    print(dealer_hand(dealer))
    win_or_lose(player,dealer)


    if win_or_lose(player,dealer) == "True Tie":
        winnings = 0
        print("Returning Bet")
    elif win_or_lose(player,dealer) == "You Win":
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



# The main game controller. THis functions initializes the game and calls the play_game function until the player runs out of chips.
# When the player is out, it displays the high score for the game.
# Created by Ruben, modified by Jeremy
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
    print("High Score Poker v0.5")
    print("Developed by Jeremy Lopanec, and Ruben Moulton Huber")











