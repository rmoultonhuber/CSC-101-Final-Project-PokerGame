rank_order = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, "Jack":11, "Queen":12, "King":13, "Ace": 14}

import random

class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank



    def __repr__(self):
        return "{} of {}".format(self.rank, self.suit)

    def __str__(self):
        return "{} of {}".format(self.rank, self.suit)

    def __eq__(self, other):
        return (other is self or
                type(other) == Card and
                self.suit == other.suit and
                self.rank == other.rank)

    def get_rank(self):
        return rank_order[self.rank]

    def get_suit(self):
        return self.suit


deck = [Card(suit, str(rank)) for rank in list(range(2,11)) + ["Jack", "Queen", "King", "Ace"] for suit in ["Spades", "Clubs", "Hearts", "Diamonds"]]

def shuffle(list):
        random.shuffle(deck)
        print("Deck Shuffled")
        return deck


