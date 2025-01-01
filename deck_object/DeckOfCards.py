# import random module
import random as rd

# Create Card class
class Card():
    # give attributes to the Card class
    def __init__(self, face, suit, value):
        self.face = face
        self.suit = suit
        self.value = value
    
    # Create a string representation of a card 
    def __str__(self):
        return self.face + " of " + self.suit + ", value: " + str(self.value)

# Create a DeckOfCards class
class DeckOfCards():
    # give attributes to the DeckOfCards class
    def __init__(self):
        self.deck = []
        self.faces = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        self.suits = ["Clubs", "Diamonds", "Spades", "Hearts"]
        self.values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.card_inx = -1 # top of deck, NOTE: when user draws a card it will add 1 and they'll draw the first card.
        
        # append 52 card objects to the deck
        for suit in self.suits:
            for i in range(len(self.faces)):
                self.deck.append(Card(self.faces[i], suit, self.values[i]))
    
    # method that prints the entire deck
    def print_deck(self):
        for card in self.deck:
            print(card.face, "of", card.suit, end=", ")
        print("---")
    
    # method that shuffles the entire deck  
    def shuffle_deck(self):
        rd.shuffle(self.deck)
        self.card_inx = -1 # reset to drawing from top of deck
        
    # method that simulates grabbing a card off the top of a deck
    def get_card(self):
        self.card_inx += 1
        return self.deck[self.card_inx]
