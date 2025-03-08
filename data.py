rank_order = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, "Jack":11, "Queen":12, "King":13, "Ace": 14}

import random

# Class initialization for the game.
# Created by Jeremy
class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


    # Creates the string representation of the Card objects
    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)

    # Creates string to describe card object when printing a Card.
    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

    # Allows comparison between cards
    def __eq__(self, other):
        return (other is self or
                type(other) == Card and
                self.suit == other.suit and
                self.rank == other.rank)

    # Allows poker.py to be able to get the rank of the Card.
    # Input = Card, Output = rank
    def get_rank(self):
        return rank_order[self.rank]

    # Allows poker.py to be able to get the rank of the Card.
    # Input = Card, Output = suit
    def get_suit(self):
        return self.suit


deck = [Card(suit, str(rank)) for rank in list(range(2,11)) + ["Jack", "Queen", "King", "Ace"] for suit in ["Spades", "Clubs", "Hearts", "Diamonds"]]

# Shuffles a deck of 52 cards randomly.
# Input = deck, Output = deck
# Created by Jeremy, modified by Ruben
def shuffle(list):
        random.shuffle(deck)
        print("Deck Shuffled")
        return deck



