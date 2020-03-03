class Card(object):
    
    # Encoding for suits: 0 - spades, 1 - hearts, 2 - diamonds, 3 - clubs
    # Encoding for values: 11 - jack, 12 - queen, 13 - king, 1 - ace
    
    suits = {0: "spades", 1: "hearts", 2: "diamonds", 3: "clubs"}
    vals = {1: "ace", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7",
            8: "8", 9: "9", 10: "10", 11: "J", 12: "Q", 13: "K"}
    
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
        
    def __repr__(self):
        return f"{vals[self.val]} of {suits[self.suit]}"
        
        
class Deck(object):
    
    import random
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for val in range(1,14):
                self.cards.append(Card(suit, val))
                
    def shuffle(self):
        random.shuffle(self.cards)
        
    def draw(self, N):
        drawn = []
        for i in range(N):
            drawn.append(self.suit.pop())
        return drawn
        

class Player(object):
    
    def __init__(self, deck, hand_size):
        self.deck = deck
        self.hand = self.deck.draw(hand_size)
        
    def shuffle_deck(self):
        self.deck.shuffle()
        
    def pick_cards_from_deck(self, N):
        self.hand += self.deck.draw(N)
        
    def discard(self, N):
        discard = []
        for i in range(N):
            discard.append(self.hand.pop())
            