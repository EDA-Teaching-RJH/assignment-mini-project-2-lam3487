import random

class Game:
    def __init__(self):
        self.players = []
        self.Deck = []

    def PlayGame(self):
        self.Deck = Deck()
        self.Deck.CreateDeck()
        self.Deck.ShuffleDeck()
        self.Hand = self.Deal()

    def Deal(self):
        for i in range(2):
            for player in self.players:
                cards = self.Deck.Cards.pop()
                player.Hand.append(cards)
    
    def Hit(self, player):
        print("s")

    def DeckTest(self):
        self.Deck = []
        self.Deck = Deck()
        deck = self.Deck.CreateDeck()
        deck = self.Deck.ShuffleDeck()
        for n, card in enumerate(deck):
            print(deck[n])
        

    def DealTest(self):
        self.Deck = []
        self.Deck = Deck()
        deck = self.Deck.CreateDeck()
        deck = self.Deck.ShuffleDeck()
        self.Hand = []
        hand = self.Deal()
        print(hand)
        
class Deck:
    Suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
    Values = ["ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king"]

    def __init__(self):
        self.Cards = []

    def __len__(self):
        return len(self.Cards)
    
    def CreateDeck(self):
        for Suit in self.Suits:
            for Value in self.Values:
                self.Cards.append(Card(Suit, Value))
        return(self.Cards)
     
    def ShuffleDeck(self):
        random.shuffle(self.Cards)
        return(self.Cards)
    
class Card:
    def __init__(self, Suit, Value):
        self.Suit = Suit
        self.Value = Value
    
    def __str__(self):
        return str(f"{self.Value} of {self.Suit}")

    def GetCardScore(self):
        if self.Value == "jack" or self.Value == "queen" or self.Value == "king":
            return 10
        if self.Value in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            return(self.Value)
        if self.Value == "ace":
            return 1
        
class Player:
    def __init__(self):
        self.Hand = []

    def GetHandScore(self):
        HandScore = 0
        for i in range(len(self.Hand)):
            HandScore = HandScore + self.GetCardScore()

class Human(Player):

class Dealer(Player):

def main():
    game = Game()
    game.DealTest()

main()