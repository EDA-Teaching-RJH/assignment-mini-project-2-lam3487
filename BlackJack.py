import random

class Game:
    def __init__(self):
        self.players = []
        self.Deck = []

    def PlayGame(self):
        self.Deck = Deck()
        self.Deck.CreateDeck()
        self.Deck.ShuffleDeck()
        player = Human(100)
        dealer = Dealer()
        self.players = [player, dealer]
        self.Deck.CreateDeck()
        self.Deck.ShuffleDeck()
        while True:
            if self.players[0].chips == 0:
                print("you have no more chips to play with")
                break
            self.playerBet = player.Bet()
            self.Deal()
            print("the dealers cards are ")
            dealer.ShowHand()
            dealer.GetHandScore
            print("\nyour cards are ")
            player.ShowHand()
            player.GetHandScore
            self.Choice(player)
            if player.IsBust == False:
                print("test")


    def Deal(self):
        for i in range(2):
            for player in self.players:
                cards = self.Deck.Cards.pop(1)
                player.Hand.append(cards)
        return(player.Hand)
            
    def Hit(self, player):
        card = self.Deck.Cards.pop()
        player.Hand.append(card)
        print("\nyour cards are ")
        player.ShowHand()
        self.CheckIfBust(player)

    
    def Choice(self, player):
        choice = input("would you like to hit or stand? H/S ")
        if choice.upper() == "H":
            self.Hit(player)
        if choice.upper() == "S":
            print("test")

    def CheckIfBust(self, player):
        if player.IsBust:
            if isinstance(player, Human):
                print("you've gone bust")
                self.Lose()
            if isinstance(player, Dealer):
                print("you've won this time")
                player.chips == player.chips + (player.chips * 2)
                print(f"you now have {player.chips} chips")
                self.playerBet = 0

    def Lose(self):
        print("The house has won")

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
        player = Human()
        self.Hand = []
        self.Hand = Game()
        deck = self.Deck.CreateDeck()
        deck = self.Deck.ShuffleDeck()
        hand = self.Deal()
        for n, card in enumerate(hand):
            print(hand[n])
        
    
        
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
     
    def ShuffleDeck(self):
        random.shuffle(self.Cards)
        return(self.Cards)
    
class Card:
    def __init__(self, Suit, Value):
        self.Suit = Suit
        self.Value = Value
    
    def __str__(self):
        return str(f"{self.Value} of {self.Suit}")

    @property
    def GetCardScore(self):
        if self.Value == "jack" or self.Value == "queen" or self.Value == "king":
            return 10
        if self.Value in ["2", "3", "4", "5", "6", "7", "8", "9", "10"]:
            return int(self.Value)
        if self.Value == "ace":
            return 1
        
class Player:
    def __init__(self):
        self.Hand = []

    @property
    def GetHandScore(self):
        HandScore = 0
        for i, card in enumerate(self.Hand):
            HandScore = HandScore + card.GetCardScore
        print(f"the card total is: {HandScore}")
        return HandScore
    
    def ShowHand(self):
        for n, card in enumerate(self.Hand):
            print(str(self.Hand[n]))
    
    @property
    def IsBust(self):
        if self.GetHandScore > 21:
            return True
    

class Human(Player):
    def __init__(self, chips):
        super().__init__()
        self.Hand = []
        self.chips = chips
    
    def Bet(self):
        bet = int(input(f"you have {self.chips} chips how many would you like to bet?"))
        if bet > 0 and bet <= self.chips:
            self.chips = self.chips - bet
            return bet
        else:
            print("you are unable to bet this many chips, please try again")
            self.Bet()

class Dealer(Player):
    def __init__(self):
        super().__init__()
        self.Hand = []

def main():
    game = Game()
    game.PlayGame()



main()