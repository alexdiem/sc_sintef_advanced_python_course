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
        return f"{self.vals[self.val]} of {self.suits[self.suit]}"
        
        
class Deck(object):
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for val in range(1,14):
                self.cards.append(Card(suit, val))
                
    def __len__(self):
        return len(self.cards)
                
    def shuffle(self):
        import random
        random.shuffle(self.cards)
        print(f"The deck has been shuffled.")
        
    def draw(self, N):
        drawn = []
        for i in range(N):
            drawn.append(self.cards.pop())
        return drawn
    
    def see_cards(self):
        print(self.cards)
        

class Player(object):
    
    def __init__(self, deck, hand_size):
        self.deck = deck
        self.hand = self.deck.draw(hand_size)
        
    def shuffle_deck(self):
        self.deck.shuffle()
        
    def pick_cards_from_deck(self, N):
        self.hand += self.deck.draw(N)
        
    def discard(self, N):
        for i in range(N):
            self.hand.pop()
            

            