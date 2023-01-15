from unittest import TestCase,mock
from unittest.mock import patch
from Player import Player
from Deck_Of_Cards import Deck_Of_Cards
from Card_Game import Card_Game
from Card import Card


class TestCard_Game(TestCase):
    def setUp(self):
        self.game=Card_Game("tomer","tom",10,10)
        self.deck=Deck_Of_Cards()
        self.game2 = Card_Game("tomer", "tom")

    def test_init_valid_case_starting_game_each_player_has_10_cards(self):
        self.assertTrue(self.game)
        self.assertEqual("tomer",self.game.player1.name)
        self.assertEqual("tom",self.game.player2.name)
        self.assertEqual(10,self.game.player1.number_cards)
        self.assertEqual(10,self.game.player2.number_cards)
        self.assertEqual(32,len(self.game.deck_cards.cards))

    def test_init_valid_case_starting_game_each_player_has_26_cards(self):
        self.assertTrue(self.game2)
        self.assertEqual("tomer",self.game2.player1.name)
        self.assertEqual("tom",self.game2.player2.name)
        self.assertEqual(26,self.game2.player1.number_cards)
        self.assertEqual(26,self.game2.player2.number_cards)
        self.assertEqual(0,len(self.game2.deck_cards.cards))

    def test_init_valid_case_argument_num_cards_of_player_is_bigger_than_the_other_player(self):
        game=Card_Game("tomer","tom",26,10)
        self.assertTrue(game)
        self.assertEqual(game.player1.number_cards,game.player2.number_cards)
        self.assertNotEqual(10,game.player2.number_cards)
        self.assertEqual(26,game.player2.number_cards)

    def test_init_valid_case_argument_num_cards_under_10_or_over_26(self):
        game = Card_Game("tomer", "tom", 27, 9)
        self.assertTrue(game)
        self.assertEqual(26,game.player1.number_cards)
        self.assertEqual(26,game.player2.number_cards)
        game2 = Card_Game("tomer", "tom", 9,27)
        self.assertTrue(game)
        self.assertEqual(26, game2.player1.number_cards)
        self.assertEqual(26, game2.player2.number_cards)

    def test_init_invalid_case_argument_name_not_str(self):
        with self.assertRaises(TypeError):
         game=Card_Game(["tomer"],"tomer")
        with self.assertRaises(TypeError):
         game=Card_Game("tomer",["tomer"])

    def test_init_invalid_case_argument_num_cards_not_int(self):
        with self.assertRaises(TypeError):
         game=Card_Game("tomer","tomer",[26],26)
        with self.assertRaises(TypeError):
         game=Card_Game("tomer","tomer",10,"10")

    def test_new_game_calling_to_shuffle(self):
        with patch('Deck_Of_Cards.Deck_Of_Cards.cards_shuffle') as mock_shuffle:
            game=Card_Game("tomer","tom")
            mock_shuffle.assert_called_with()

    def test_new_game_calling_to_set_hand(self):
        with patch('Player.Player.set_hand') as mock_set_hand:
           game=Card_Game("tomer","tom")
           mock_set_hand.assert_called_with(game.deck_cards)

    def test_new_game_valid_case_deck_of_cards_is_full_and_each_player_not_has_cards(self):
        player1=Player("tomer",10)
        player2=Player("tom",10)
        self.assertEqual(len(self.deck.cards),52)
        self.assertEqual(len(player1.cards),0)
        self.assertEqual(len(player2.cards),0)
        game=Card_Game(player1.name,player2.name,player1.number_cards,player2.number_cards)
        self.assertTrue(game)
        self.assertEqual(len(game.deck_cards.cards),32)
        self.assertEqual(len(game.player1.cards),10)
        self.assertEqual(len(game.player2.cards),10)

    def test_new_game_invalid_case_player_has_already_cards(self):
        game=Card_Game("tomer","tom")
        self.assertEqual(len(game.player1.cards),26)
        self.assertFalse(game.new_game())

    def test_new_game_invalid_case_deck_of_cards_isnt_52_cards(self):
        game=Card_Game("tomer","tom")
        game.deck_cards.cards.append(Card(1,1))
        self.assertFalse(game.new_game())

    def test_get_winner_player_1_wins(self):
        game=Card_Game("tomer","dan",10,10)
        self.assertEqual(len(game.player1.cards),len(game.player2.cards))
        game.player1.cards.append(Card(1,1))
        self.assertEqual(11, len(game.player1.cards))
        self.assertEqual(game.get_winner(),f"The winner of the game is: {game.player1.name.title()}")

    def test_get_winner_player_2_wins(self):
        game=Card_Game("tomer","dan",10,10)
        self.assertEqual(len(game.player1.cards),len(game.player2.cards))
        game.player2.cards.append(Card(1,1))
        self.assertEqual(11,len(game.player2.cards))
        self.assertEqual(game.get_winner(),f"The winner of the game is: {game.player2.name.title()}")

    def test_get_winner_draw_between_the_2_players(self):
        game=Card_Game("tomer","tom",10,10)
        self.assertEqual(len(game.player1.cards), len(game.player2.cards))
        self.assertEqual(None,game.get_winner())
