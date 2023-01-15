class Card:
    """Card value is from 1-13 1=Ace,11=Jack,12=Queen,13=King
       Card suit is from 1-4 1=Diamond,2=Spade,3=Heart,4=Club
            Ace is the greatest Value"""
    def __init__(self,value:int,suit:int):
        if type(value)!=int:
            raise TypeError("Argument value must be int")
        if type(suit)!=int:
            raise TypeError("Argument suit must be int")
        if value<1 or value>13:
            raise ValueError("Argument value must be value from 1-13")
        if suit<1 or suit>4:
            raise ValueError("Argument suit must be value from 1-4")
        self.value=value
        self.suit=suit

    def __gt__(self, other):
        """Function that compare greatness between card value and suit to other card"""
        if type(other)!=Card:
            raise TypeError("Can compare only between Cards")
        if self.value==1 and other.value!=1:
            return True
        elif self.value!=1 and other.value==1:
            return False
        if self.value==other.value and self.suit>other.suit:
            return True
        if self.value>other.value:
            return True
        else:
            return False

    def __eq__(self, other):
        """Function that compare equality between card value and suit to other card"""
        if type(other)!=Card:
            raise TypeError("Can compare only between Cards")
        if self.value==other.value and self.suit==other.suit:
            return True
        else:
            return False

    def __repr__(self):
        dic={1:"Ace",11:"Jack",12:"Queen",13:"King"}
        dic2={1:"Diamond",2:"Spade",3:"Heart",4:"Club"}
        for i in dic:
            if i==self.value:
                v=dic[i]
                break
        else:
            v=self.value
        s=dic2[self.suit]
        return f"{v}:{s}"



