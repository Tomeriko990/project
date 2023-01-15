from unittest import TestCase
from Card import Card


class TestCard(TestCase):
    def setUp(self):
        self.card=Card(1,1)
        self.card2=Card(13,4)

    def test_init_valid_case(self):
        self.assertTrue(Card(1,1))
        self.assertTrue(Card(13,4))

    def test_init_invalid_case_value_not_int(self):
        with self.assertRaises(TypeError):
           Card("14",1)
        with self.assertRaises(TypeError):
           Card([14],1)

    def test_init_invalid_case_suit_not_int(self):
        with self.assertRaises(TypeError):
            Card(13, "1")
        with self.assertRaises(TypeError):
            Card(13, [1])

    def test_init_invalid_case_value_under1_or_over13(self):
        with self.assertRaises(ValueError):
            Card(0,4)
        with self.assertRaises(ValueError):
            Card(14,1)

    def test_init_invalid_case_suit_under1_or_over4(self):
        with self.assertRaises(ValueError):
            Card(1,0)
        with self.assertRaises(ValueError):
            Card(13,5)

    def test_gt_valid_case_true(self):
        card1=Card(1,4)
        card2=Card(13,4)
        self.assertTrue(card1>card2)
        card3 = Card(13, 3)
        card4 = Card(13, 2)
        self.assertTrue(card3>card4)
        card5=Card(5,1)
        card6=Card(4,1)
        self.assertTrue(card5>card6)

    def test_gt_valid_case_false(self):
        card1 = Card(13, 4)
        card2 = Card(1, 4)
        self.assertFalse(card1>card2)
        card3 = Card(13, 3)
        card4 = Card(13, 4)
        self.assertFalse(card3 > card4)
        card5 = Card(5, 1)
        card6 = Card(6, 1)
        self.assertFalse(card5 > card6)

    def test_gt_invalid_case_not_comparing_to_card(self):
       with self.assertRaises(TypeError):
           self.card>[1,2,3]
       with self.assertRaises(TypeError):
           self.card>100

    def test_eq_valid_case_true(self):
        card1=Card(5,4)
        card2=Card(5,4)
        self.assertTrue(card1==card2)

    def test_eq_valid_case_false(self):
        card1 = Card(2, 4)
        card2 = Card(5, 4)
        self.assertFalse(card1 == card2)

    def test_eq_invalid_case_not_comparing_to_card(self):
        with self.assertRaises(TypeError):
            self.card == [1, 2, 3]
        with self.assertRaises(TypeError):
            self.card == 100
