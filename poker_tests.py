from os.path import expanduser
from unittest import TestCase

import data
from data import shuffle
from poker_code import your_hand, dealer_hand, sort_ranks, hand_type, get_hand_value, win_or_lose, betting, play_game

shuffled_deck = shuffle(data.deck)

class TestPoker(TestCase):

    def test_sort_hands1(self):
        inpt = [data.Card('Clubs', '2'), data.Card('Clubs', '6'), data.Card('Spades', '2'),
                data.Card('Hearts', 'Jack'),data.Card('Diamonds', '4')]
        expected = [data.Card('Hearts','Jack'), data.Card('Clubs','6'), data.Card('Diamonds','4'),
                    data.Card('Clubs','2'), data.Card('Spades','2')]
        result = sort_ranks(inpt)
        self.assertEqual(expected,result)

    def test_sort_hands2(self):
        inpt = [data.Card('Clubs', '2'), data.Card('Clubs', '6')]
        expected = [data.Card('Clubs','6'),data.Card('Clubs','2')]
        result = sort_ranks(inpt)
        self.assertEqual(expected,result)

    def test_deal_hand1(self):
        length = 5
        test_hand = shuffled_deck[:5]
        self.assertEqual(len(test_hand),length)

    def test_deal_hand2(self):
        player_hand = shuffled_deck[:5]
        dealer_hand = shuffled_deck[5:10]
        self.assertEqual(len(player_hand),len(dealer_hand))

    def test_hand_type1(self):
        inpt = [data.Card('Clubs', '2'), data.Card('Clubs', '6'), data.Card('Spades', '2'),
                data.Card('Hearts', 'Jack'),data.Card('Diamonds', '4')]
        expected = "Pair"
        result = hand_type(inpt)
        self.assertEqual(expected,result)

    def test_hand_type2(self):
        inpt = [data.Card('Clubs', '2'), data.Card('Spades', '2')]
        expected = "Unknown Hand"
        result = hand_type(inpt)
        self.assertEqual(expected,result)

    def test_dealer_hand1(self):
        inpt = [data.Card('Clubs', '2'), data.Card('Clubs', '6'), data.Card('Spades', '2'),
                data.Card('Hearts', 'Jack'),data.Card('Diamonds', '4')]
        expected = "Dealer Hand is: Pair"
        result = dealer_hand(inpt)
        self.assertEqual(expected,result)

    def test_dealer_hand2(self):
        inpt = [data.Card('Clubs', '2'), data.Card('Clubs', '6'), data.Card('Spades', '8'),
                data.Card('Hearts', 'Jack'),data.Card('Diamonds', '4')]
        expected = "Dealer Hand is: High Card"
        result = dealer_hand(inpt)
        self.assertEqual(expected,result)

    def test_your_hand1(self):
        inpt = [data.Card('Clubs', '2'), data.Card('Clubs', '6'), data.Card('Spades', '2'),
                data.Card('Hearts', 'Jack'),data.Card('Diamonds', '4')]
        expected = "Your Hand is: Pair"
        result = your_hand(inpt)
        self.assertEqual(expected,result)

    def test_your_hand2(self):
        inpt = [data.Card('Clubs', '2'), data.Card('Clubs', '6'), data.Card('Spades', '8'),
                data.Card('Hearts', 'Jack'),data.Card('Diamonds', '4')]
        expected = "Your Hand is: High Card"
        result = your_hand(inpt)
        self.assertEqual(expected,result)

    def test_get_hand_value1(self):
        inpt = [data.Card('Clubs', '2'), data.Card('Clubs', '6'), data.Card('Spades', '2'),
                data.Card('Hearts', 'Jack'),data.Card('Diamonds', '4')]
        expected = 2
        result = get_hand_value(inpt)
        self.assertEqual(expected,result)

    def test_get_hand_value2(self):
        inpt = [data.Card('Clubs', '2'), data.Card('Clubs', '6'), data.Card('Spades', '8'),
                data.Card('Hearts', 'Jack'),data.Card('Diamonds', '4')]
        expected = 1
        result = get_hand_value(inpt)
        self.assertEqual(expected,result)

    def test_win_or_lose1(self):
        player = [data.Card('Clubs', '2'), data.Card('Clubs', '6'), data.Card('Spades', '2'),
                  data.Card('Hearts', 'Jack'),data.Card('Diamonds', '4')]
        dealer = [data.Card('Clubs', '2'), data.Card('Clubs', '6'), data.Card('Spades', '8'),
                  data.Card('Hearts', 'Jack'),data.Card('Diamonds', '4')]
        expected = win_or_lose(player,dealer)
        result = "You Win"
        self.assertEqual(expected,result)

    def test_win_or_lose2(self):
        player = [data.Card('Clubs', '4'), data.Card('Clubs', '6'), data.Card('Spades', '4'),
                  data.Card('Hearts', 'Jack'),data.Card('Diamonds', '7')]
        dealer = [data.Card('Clubs', '2'), data.Card('Clubs', '6'), data.Card('Spades', '2'),
                  data.Card('Hearts', 'Jack'),data.Card('Diamonds', '7')]
        expected = win_or_lose(player,dealer)
        result = "True Tie"
        self.assertEqual(expected,result)

    def test_win_or_lose3(self):
        player = [data.Card('Clubs', '4'), data.Card('Clubs', '6'), data.Card('Spades', '4'),
                  data.Card('Hearts', 'Jack'), data.Card('Diamonds', '7')]
        dealer = [data.Card('Clubs', '2'), data.Card('Clubs', '6'), data.Card('Spades', '2'),
                  data.Card('Hearts', 'Jack'), data.Card('Diamonds', 'King')]
        expected = win_or_lose(player, dealer)
        result = "You Lose By Tie Break"
        self.assertEqual(expected, result)

    def test_betting1(self):
        total = 500
        bet = 700
        expected = 0
        result = betting(total,bet)
        self.assertEqual(expected,result)

    def test_betting2(self):
        total = 500
        bet = -500
        expected = 0
        result = betting(total, bet)
        self.assertEqual(expected, result)

    def test_betting3(self):
        total = 500
        bet = 500
        expected = 500
        result = betting(total, bet)
        self.assertEqual(expected, result)

    def test_betting4(self):
        total = 500
        bet = 250
        expected = 250
        result = betting(total, bet)
        self.assertEqual(expected, result)




