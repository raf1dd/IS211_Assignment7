"""
IS 211 Assignment 7 - Unit Tests for the Game of Pig
"""

import unittest
import pig

class PigTestCases(unittest.TestCase):

    def test_die_roll(self):
        d = pig.Die()
        for _ in range(100):
            val = d.roll()
            self.assertTrue(1 <= val <= 6)

    def test_player_initialization(self):
        p = pig.Player("TestPlayer")
        self.assertEqual(p.name, "TestPlayer")
        self.assertEqual(p.score, 0)
        self.assertEqual(p.turn_total, 0)

    def test_player_scoring(self):
        p = pig.Player("TestPlayer")
        p.add_to_turn_total(10)
        self.assertEqual(p.turn_total, 10)
        p.bank_score()
        self.assertEqual(p.score, 10)
        self.assertEqual(p.turn_total, 0)

    def test_game_initialization(self):
        g = pig.Game("Alice", "Bob")
        self.assertEqual(len(g.players), 2)
        self.assertEqual(g.players[0].name, "Alice")
        self.assertEqual(g.players[1].name, "Bob")

if __name__ == "__main__":
    unittest.main(verbosity=2)
