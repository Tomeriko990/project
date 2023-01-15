import random
from Card import Card
from random import choice

class Deck_Of_Cards:
 """Deck_Of_Cards is a list of 52 cards from 1-13 different 4 suits """
 def __init__(self):
     self.cards = []
    #deck of cards not allowed duplicate cards
     for i in range(1,5):
         for j in range(1,14):
             if Card(j,i) not in self.cards:
              self.cards.append((Card(j,i)))

 def cards_shuffle(self):
     """Shuffle the deck of cards"""
     random.shuffle(self.cards)

 def deal_one(self):
    """Choose one random card from the deck of cards and delete it from it
    if there is cards in the deck"""
    if len(self.cards)>0:
       c=choice(self.cards)
       self.cards.remove(c)
       return c
    else:
        print("out of cards")
        return False

 def __repr__(self):
     return f"{self.cards}"
