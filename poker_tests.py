from unittest import TestCase

from poker_code import shuffled_deck


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
        inpt = ["5 of hearts"]

        self.assertEqual()


