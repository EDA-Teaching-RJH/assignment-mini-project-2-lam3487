import random

class Game:
    def __init__(self):
        self.players = []
        self.Deck = []
        self.PlayerTurn = True

    def PlayGame(self):
        self.Deck = Deck()
        self.Deck.CreateDeck()
        self.Deck.ShuffleDeck()
        player = Human(100)
        dealer = Dealer()
        Active = True
        PlayerTurn = False
        self.players = [player, dealer]
        self.Deck.CreateDeck()
        self.Deck.ShuffleDeck()
        while Active == True:
            if player.chips == 0:
                print("you have no more chips to play with")
                break
            self.playerBet = Human.Bet(player)
            self.Deal()
            print("the dealers cards are ")
            dealer.RevealHand()
            print("\nyour cards are ")
            player.ShowHand(player)
            player.GetHandScore
            self.Choice(player)
            if not player.IsBust:
                print("\nthe dealers cards are: ")
                dealer.ShowHand(player)
                while PlayerTurn == False:
                    if dealer.GetHandScore < 17:
                        print("\nthe dealer hits")
                        self.Hit(dealer)
                        PlayerTurn = True
                    if dealer.GetHandScore > 17 and not dealer.IsBust:
                        print("\nthe dealer stands")
                        PlayerTurn = True
                self.Compare(player, dealer)
                Again = self.PlayAgain()
                if Again:
                    Active = False
                else:
                    self.ResetPlayers()
                    PlayerTurn = True

            

    def Deal(self):
        for i in range(2):
            for player in self.players:
                cards = self.Deck.Cards.pop(1)
                player.Hand.append(cards)
        return(player.Hand)
            
    def Hit(self, player):
        card = self.Deck.Cards.pop()
        player.Hand.append(card)
        print(f"\nthe cards are ")
        player.ShowHand(player)
        self.CheckIfBust(player)

    
    def Choice(self, player):
        choice = input("would you like to hit or stand? H/S ")
        if choice.upper() == "H":
            self.Hit(player)
        if choice.upper() == "S":
            print(f"you have decide to stand with a total of {player.GetHandScore}")

    def CheckIfBust(self, player):
        if player.IsBust == True:
            if isinstance(player, Human):
                print("\nyou've gone bust")
                self.Lose()
            if isinstance(player, Dealer):
                print("the dealer has gone bust")
                self.Win(Human)
            else:
                print("its a Draw")

    def Lose(self):
        print("The house has won")
        
    def Win(self, player):
        print("you've won this time")
        player.chips += 2 * self.playerBet
        self.playerBet = 0
        

    def Compare(self, player, dealer):
        if player.GetHandScore > dealer.GetHandScore:
            self.Win(player)
        if player.GetHandScore < dealer.GetHandScore:
            self.Lose()
        else:
            ("its a draw")
        
    def PlayAgain(self):
        Again = input("\ndo you want to play again? Y/N ")
        if Again.upper == "Y":
            return True
        if Again.upper == "N":
            return False
    
    def ResetPlayers(self):
        for player in self.players:
            player.reset()
        self.playerBet = 0
        
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
        return HandScore
    
    def ShowHand(self, player):
            for n, card in enumerate(self.Hand):
                print(self.Hand[n])
    
    @property
    def IsBust(self):
        if self.GetHandScore > 21:
            return True
    
    def reset(self):
        self.Hand = []

class Human(Player):
    def __init__(self, chips):
        super().__init__()
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
    
    def RevealHand(self):
        print("?")
        print(str(self.Hand[1]))

def main():
    game = Game()
    game.PlayGame()



main()