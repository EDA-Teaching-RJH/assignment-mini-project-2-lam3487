import random

class Game:
    def __init__(self):
        self.Deck = []
    def Test(self):
        self.Deck = []
        self.Deck = Deck()
        deck = self.Deck.CreateDeck()
        for n, card in enumerate(deck):
            print(deck[n])
        
class Deck:
    Suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    Values = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]

    def __init__(self):
        self.Cards = []

    def __len__(self):
        return len(self.cards)
    
    def CreateDeck(self):
        for Suit in self.Suits:
            for Value in self.Values:
                self.Cards.append(Card(Suit, Value))
        return(self.Cards)

class Card:
    def __init__(self, Suit, Value):
        self.Suit = Suit
        self.Value = Value
    
    def __str__(self):
        return str(f"{self.Value} of {self.Suit}")
    
def main():
    game = Game()
    game.Test()

main()