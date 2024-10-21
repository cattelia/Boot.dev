import random

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        # We are going to use .index() here since the data we are using is so small.
        self.rank_index = RANKS.index(self.rank)
        self.suit_index = SUITS.index(self.suit)


    def __eq__(self, other):
        return True if other.rank_index == self.rank_index and other.suit_index == self.suit_index else False

    def __lt__(self, other):
        if self.rank_index < other.rank_index:
            return True
        elif self.rank_index == other.rank_index:
            if self.suit_index < other.suit_index:
                return True
            else:
                return False
        else:
            return False


    def __gt__(self, other):
        if self.rank_index > other.rank_index:
            return True
        elif self.rank_index == other.rank_index:
            if self.suit_index > other.suit_index:
                return True
            else:
                return False
        else:
            return False     


    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"