from unittest import TestCase,mock
from Player import Player
from unittest.mock import patch
from Card import Card
from Deck_Of_Cards import Deck_Of_Cards

class TestPlayer(TestCase):
    def setUp(self):
        self.deck=Deck_Of_Cards()
        self.player=Player("tomer")
        self.player2=Player("tomer",10)

    def test_init_valid_case_and_argument_number_cards_not_filled(self):
        self.assertTrue(self.player)
        self.assertEqual("tomer",self.player.name)
        self.assertEqual(26,self.player.number_cards)
        self.assertEqual([],self.player.cards)

    def test_init_valid_case_and_argument_number_cards_filled(self):
        self.assertTrue(self.player2)
        self.assertEqual("tomer", self.player2.name)
        self.assertEqual(10, self.player2.number_cards)
        self.assertEqual([], self.player2.cards)

    def test_init_valid_case_and_argument_num_cards_under10_or_over_26(self):
        player=Player("tomer", 9)
        player2=Player("tom", 27)
        self.assertTrue(player)
        self.assertEqual(26,player.number_cards)
        self.assertTrue(player2)
        self.assertEqual(26, player2.number_cards)

    def test_init_invalid_case_and_argument_name_not_str(self):
        with self.assertRaises(TypeError):
            player=Player(["tomer"],24)
        with self.assertRaises(TypeError):
            player=Player(123,24)

    def test_init_invalid_case_and_argument_name_not_filled_with_1_letter(self):
        with self.assertRaises(ValueError):
            player=Player("",10)
        with self.assertRaises(ValueError):
            player = Player(" ", 10)

    def test_init_invalid_case_and_argument_num_cards_not_int(self):
        with self.assertRaises(TypeError):
            player=Player("tomer",[24])
        with self.assertRaises(TypeError):
            player=Player("tomer","24")

    @patch('Deck_Of_Cards.Deck_Of_Cards.deal_one',return_value=Card(1,4))
    def test_set_hand_valid_case_10_cards(self,mock_deal_one):
        deck=Deck_Of_Cards()
        self.player2.set_hand(deck)
        self.assertEqual(len(self.player2.cards),10)
        self.assertIn(Card(1,4),self.player2.cards)
        print(self.player2.cards)

    @patch('Deck_Of_Cards.Deck_Of_Cards.deal_one', return_value=Card(1, 4))
    def test_set_hand_valid_case_26_cards(self,mock_deal_one):
        deck = Deck_Of_Cards()
        self.player.set_hand(deck)
        self.assertEqual(len(self.player.cards),26)
        self.assertIn(Card(1, 4), self.player.cards)
        print(self.player.cards)

    def test_set_hand_valid_case_different_cards(self):
        deck = Deck_Of_Cards()
        self.player.set_hand(deck)
        self.assertNotEqual(self.player.cards[0:14],self.player.cards[14::])
        print(self.player.cards)

    def test_set_hand_invalid_case_deck_cards_not_type_Deck_Of_Cards(self):
        with self.assertRaises(TypeError):
            self.player.set_hand([1,2,3,4,5,6])

    def test_get_card_valid_case_has_cards(self):
        self.player2.set_hand(self.deck)
        self.assertEqual(len(self.player2.cards), 10)
        print(self.player2.cards)
        c=self.player2.get_card()
        self.assertEqual(len(self.player2.cards), 9)
        print(self.player2.cards)
        self.assertNotIn(c,self.player2.cards)
        print(c)

    def test_get_card_invalid_case_not_has_cards_in_player_hand(self):
        self.assertEqual(len(self.player2.cards),0)
        self.assertFalse(self.player2.get_card())

    def test_add_card_valid_case(self):
        card=Card(4,2)
        self.assertEqual(len(self.player2.cards),0)
        self.assertNotIn(card,self.player2.cards)
        self.player2.add_card(card)
        self.assertEqual(len(self.player2.cards), 1)
        self.assertIn(card, self.player2.cards)
        print(self.player2.cards)

    def test_add_card_invalid_case_try_add_different_type_then_Card(self):
        with self.assertRaises(TypeError):
            self.player2.add_card(1,1)
        with self.assertRaises(TypeError):
            self.player2.add_card("Ace","Spade")
