from unittest import TestCase
import data

class TestCard(TestCase):

    def test_Card_init(self):
        card = data.Card("Spades", "5")
        self.assertEqual("Spades", card.suit)
        self.assertEqual("5", card.rank)

    def test_Card_init_2(self):
        card = data.Card("Clubs", "King")
        self.assertNotEqual("Hearts", card.suit)
        self.assertEqual("King", card.rank)

    def test_Card_repr(self):
        card = data.Card("Diamonds", "Jack")
        self.assertEqual("Jack of Diamonds", repr(card))

    def test_Card_repr_2(self):
        card = data.Card("Hearts", "2")
        self.assertNotEqual("3 of Spades", repr(card))

    def test_Card_str(self):
        card = data.Card("Spades", "King")
        self.assertEqual("King of Spades", str(card))

    def test_Card_str_2(self):
        card = data.Card("Hearts", "9")
        self.assertNotEqual("4 of Clubs", repr(card))

