from unittest import TestCase,mock
from Deck_Of_Cards import Deck_Of_Cards
from Card import Card
from unittest.mock import patch



class TestDeck_Of_Cards(TestCase):
    def setUp(self):
        self.deck=Deck_Of_Cards()

    def test_init_valid_case(self):
        self.assertTrue(self.deck.cards)
        self.assertEqual(len(self.deck.cards),52)
        print(self.deck.cards)

    def test_cards_shuffle(self):
      self.assertEqual(self.deck.cards,self.deck.cards[0::])
      self.deck.cards_shuffle()
      self.assertNotEqual(self.deck.cards_shuffle(),self.deck.cards[0::])

    def test_deal_one_valid_case_choose_random_card_and_delete_it_from_the_list(self):
        self.assertEqual(len(self.deck.cards), 52)
        c=self.deck.deal_one()
        self.assertEqual(len(self.deck.cards),51)
        self.assertNotIn(c,self.deck.cards)

    def test_deal_one_invalid_case_no_cards_in_the_list(self):
        self.deck.cards=[]
        self.assertFalse(self.deck.deal_one())
    @patch('Deck_Of_Cards.Deck_Of_Cards.deal_one',return_value=Card(2,3))
    def test_deal_one(self,mock):
        self.deck.deal_one()
        self.deck.cards.remove(self.deck.deal_one())
        print(len(self.deck.cards))
        self.assertNotIn(Card(2,3),self.deck.cards)
        print(len(self.deck.cards))




