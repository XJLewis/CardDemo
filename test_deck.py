import unittest
from deck_hand import Deck

class TestDeck(unittest.TestCase):

    def setUp(self):
        self.deck = Deck()

    def test_generate_deck(self):
        self.assertEqual(len(self.deck.cards), 52)

    def test_shuffle_deck(self):
        original_order = self.deck.cards[:]
        self.deck.shuffle()
        self.assertNotEqual(original_order, self.deck.cards)

    def test_draw_card(self):
        card = self.deck.draw_card()
        self.assertEqual(len(self.deck.cards), 51)
        self.assertIsInstance(card, PlayingCard)

    def test_draw_from_empty_deck(self):
        for _ in range(52):
            self.deck.draw_card()
        with self.assertRaises(ValueError):
            self.deck.draw_card()

if __name__ == "__main__":
    unittest.main()
