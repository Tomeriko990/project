from Deck_Of_Cards import Deck_Of_Cards
from random import choice
from Card import Card

class Player:
    """Represent player in the game each player has a name
    and number of cards that has in his hand"""
    def __init__(self,name:str,num_cards:int=26):
        if type(name)!=str:
            raise TypeError("Argument name must be str")
        if name=="" or name==" ":
            raise ValueError("Argument name must contain at least 1 letter")
        if type(num_cards)!=int:
            raise TypeError("Argument num_cards must be int")
        if num_cards<10 or num_cards>26:
            num_cards=26
        self.name=name
        self.number_cards=num_cards
        self.cards=[]

    def set_hand(self,deck_cards:Deck_Of_Cards):
        """Function that setting a list of cards to the hand list of the player
         random card only from the Deck_Of_Cards"""
        if type(deck_cards)!=Deck_Of_Cards:
            raise TypeError("Argument deck_cards must be Deck_Of_Cards")
        for i in range(self.number_cards):
            self.cards.append(deck_cards.deal_one())

    def get_card(self):
        """Function that choose randomly card from the hand of the player
        and remove it from tha list of his cards"""
        if len(self.cards)>0:
         c=choice(self.cards)
         self.cards.remove(c)
         return c
        else:
            print(f"{self.name} dont have cards")
            return  False

    def add_card(self,card:Card):
        """Function that adding a Card to the hand of the player"""
        if type(card)!=Card:
            raise TypeError("Can add only cards")
        self.cards.append(card)

    def __repr__(self):
        return f"{self.name.title()} hand:{self.cards}"
