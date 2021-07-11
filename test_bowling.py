import unittest
from bowling import BowlingGame

class BowlingGameTest(unittest.TestCase):

    def test_should_return_0(self):

        result = BowlingGame().bowling_game(0)

        self.assertEqual(0,result)

