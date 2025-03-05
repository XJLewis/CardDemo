import unittest
from deck_hand import Hand
from playing_card import PlayingCard

class TestHand(unittest.TestCase):

    def setUp(self):
        self.hand = Hand()
        self.card1 = PlayingCard("A", "Spades")
        self.card2 = PlayingCard("10", "Hearts")

    def test_add_card(self):
        self.hand.add_card(self.card1)
        self.assertEqual(len(self.hand.cards), 1)

    def test_display_hand(self):
        self.hand.add_card(self.card1)
        self.hand.add_card(self.card2)
        self.assertEqual(self.hand.display_hand(), "A of Spades, 10 of Hearts")

    def test_card_count(self):
        self.hand.add_card(self.card1)
        self.hand.add_card(self.card2)
        self.assertEqual(self.hand.card_count(), 2)

if __name__ == "__main__":
    unittest.main()
