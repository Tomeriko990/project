from Card_Game import Card_Game
from Player import Player
from Card import Card
player1=input("enter name: ")
player2=input("enter name: ")
game=Card_Game(player1,player2)
print(game.player1)
print(game.player2)
for i in range(1,11):
    if len(game.player1.cards)<1 or len(game.player2.cards)<1:
        break
    c=game.player1.get_card()
    c2=game.player2.get_card()
    print(f"========Round{i}==========")
    print(f"{game.player1.name.title()} Card is: {c}\n{game.player2.name.title()} Card is: {c2}")
    if c>c2:
        game.player1.add_card(c)
        game.player1.add_card(c2)
        print(game.player1.name.title(),f"win round {i} and taking the cards")
    else:
        game.player2.add_card(c)
        game.player2.add_card(c2)
        print(game.player2.name.title(),f"win round {i} and taking the cards")

print("==========End game==============")
if game.get_winner()== None:
    print(f"Draw between {game.player1.name} and {game.player2.name}")
else:
    print(game.get_winner())




