import random
from playing_card import PlayingCard

class Deck:
    """A deck of 52 playing cards"""
    
    def __init__(self):
        self.cards = self.generate_deck()

    def generate_deck(self):
        """Generates a full deck of 52 cards."""
        return [PlayingCard(rank, suit) for suit in PlayingCard.SUITS for rank in PlayingCard.RANKS]

    def shuffle(self):
        """Shuffles the deck."""
        random.shuffle(self.cards)

    def draw_card(self):
        """Draws a card from the deck."""
        if self.cards:
            return self.cards.pop()
        raise ValueError("No more cards in the deck.")

class Hand:
    """A player's hand of playing cards"""
    
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        """Adds a card to the hand."""
        self.cards.append(card)

    def display_hand(self):
        """Returns a string representation of the hand."""
        return ', '.join(str(card) for card in self.cards)

    def card_count(self):
        """Returns the number of cards in the hand."""
        return len(self.cards)
