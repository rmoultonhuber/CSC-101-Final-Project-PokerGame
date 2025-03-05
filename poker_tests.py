from os.path import expanduser
from unittest import TestCase

import data
from data import shuffle
from poker_code import your_hand, dealer_hand

shuffled_deck = shuffle(data.deck)
print(shuffled_deck[:5])
class TestPoker(TestCase):

    def test_deal_hand1(self):
        length = 5
        test_hand = shuffled_deck[:5]
        self.assertEqual(len(test_hand),length)

    def test_deal_hand2(self):
        player_hand = shuffled_deck[:5]
        dealer_hand = shuffled_deck[5:10]
        self.assertEqual(len(player_hand),len(dealer_hand))

    def test_get_hand_value1(self):
        inpt = [data.Card('Clubs', '2'), data.Card('Clubs', '6'), data.Card('Spades', '2'), data.Card('Hearts', 'Jack'),data.Card('Diamonds', '4')]
        expected = "Your Hand is: Pair"
        result = your_hand(inpt)
        self.assertEqual(expected,result)

    def test_get_dealer_hand_value1(self):
        inpt = [data.Card('Clubs', '2'), data.Card('Clubs', '6'), data.Card('Spades', '2'), data.Card('Hearts', 'Jack'),data.Card('Diamonds', '4')]
        expected = "Dealer Hand is: Pair"
        result = dealer_hand(inpt)
        self.assertEqual(expected,result)

