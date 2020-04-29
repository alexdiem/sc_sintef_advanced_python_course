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
    
    def __init__(self, name, deck, hand_size):
        self._name = name
        self.deck = deck
        self.hand = self.deck.draw(hand_size)
        
    def get_name(self):
        return self._name
        
    def shuffle_deck(self):
        self.deck.shuffle()
        
    def pick_cards_from_deck(self, N):
        self.hand += self.deck.draw(N)
        
    def discard(self, N):
        for i in range(N):
            self.hand.pop()
            
    def __repr__(self):
        return f"{self._name}'s hand is " + str(self.hand)    


class CardGame(object):
    def __init__(self, players, deck):
        self.players = players
        self.deck = deck
        self.playground = []
        self.leading_suit = -1
    
    def play_round(self):
        self.leading_suit = -1
        is_first_player = True
        for player in self.players:
            card = player.play_card(self, self.leading_suit)
            if is_first_player:
                self.leading_suit = card.suit
            
            is_first_player = False
        self.playground = []


class Hearts(CardGame):
    def __init__(self, players, deck):
        super().__init__(players, deck)
        self.tricks = []
        
        
    def win_trick(self):
        highest_card = self.playground[0]
        winning_player = 0
        for i in range(1, len(self.playground)):
            if highest_card.trumped(self.leading_suit, self.playground[i]):
                highest_card = self.playground[i]
                winning_player = i
        self.tricks.append[i]
        
        
    def play_round(self):
        super().__init__(players, deck)
        self.win_trick()
            

class OhHell(CardGame):
    pass