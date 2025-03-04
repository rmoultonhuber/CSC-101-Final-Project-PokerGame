from unittest import TestCase

from poker_code import shuffled_deck


class TestPoker(TestCase):

    def test_deal_hand(self):
        length = 5
        test_hand = shuffled_deck[:5]
        self.assertEqual(len(test_hand),length)


    def

