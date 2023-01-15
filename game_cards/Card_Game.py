from Deck_Of_Cards import Deck_Of_Cards
from Player import Player
class Card_Game:
    """Represent a card game between two Players
    each player has list of random cards
    the one who has more cards in his hand his the winner of th game"""
    def __init__(self,name_p1,name_p2,num_p1=26,num_p2=26):
        if type(name_p1)!=str:
            raise TypeError("Argument name_p1 must be str")
        if type(name_p2)!=str:
            raise TypeError("Argument name_p2 must be str")
        if type(num_p1)!=int:
            raise TypeError("Argument num_p1 must be int")
        if num_p1<10 or num_p1>26:
            num_p1=26
        if type(num_p2)!=int:
            raise TypeError("Argument num_p2 must be int")
        if num_p2<10 or num_p2>26:
            num_p2=26
        if num_p1>num_p2 or num_p2>num_p1:
            num_p2=num_p1
        self.player1=Player(name_p1,num_p1)
        self.player2=Player(name_p2,num_p2)
        self.deck_cards=Deck_Of_Cards()
        self.game=self.new_game()

    def new_game(self):
        """Start a new game between 2 players only when the deck_cards is full- 52 cards
        and each player has 0 cards in his hand"""
        if len(self.deck_cards.cards) == 52 and len(self.player1.cards)==0 and len(self.player2.cards)==0:
             self.deck_cards.cards_shuffle()
             self.player1.set_hand(self.deck_cards)
             self.player2.set_hand(self.deck_cards)
        else:
            print("Error cant start new game")

    def get_winner(self):
        """Checks which player has more cards in his deck
        the player that has more cards his the winner of the game"""
        if len(self.player1.cards)>len(self.player2.cards):
         return f"The winner of the game is: {self.player1.name.title()}"
        if len(self.player2.cards)>len(self.player1.cards):
         return f"The winner of the game is: {self.player2.name.title()}"
        else:
            return None




