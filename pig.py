"""
IS 211 Assignment 7 - The Game of Pig (OOP Implementation)
"""

import random

# Mandatory random seed for testability
random.seed(0)

class Die:
    """Represents a single 6-sided die."""
    def roll(self):
        return random.randint(1, 6)

class Player:
    """Represents a player in the game of Pig."""
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn_total = 0

    def add_to_turn_total(self, value):
        self.turn_total += value

    def reset_turn_total(self):
        self.turn_total = 0

    def bank_score(self):
        self.score += self.turn_total
        self.reset_turn_total()

class Game:
    """Manages the state and flow of the Pig game."""
    def __init__(self, player1_name="Player 1", player2_name="Player 2"):
        self.players = [Player(player1_name), Player(player2_name)]
        self.die = Die()
        self.current_player_idx = 0

    def play_turn(self):
        player = self.players[self.current_player_idx]
        player.reset_turn_total()
        print(f"\n--- {player.name}'s Turn ---")

        while True:
            # Prompt user for decision ('r' or 'h')
            decision = input(f"{player.name}, your total score is {player.score}. Turn total is {player.turn_total}. Roll (r) or Hold (h)? ").strip().lower()
            
            if decision == 'r':
                roll_val = self.die.roll()
                print(f"{player.name} rolled a {roll_val}.")
                
                if roll_val == 1:
                    print(f"Oops! Rolled a 1. {player.name} scores nothing this turn.")
                    player.reset_turn_total()
                    break
                else:
                    player.add_to_turn_total(roll_val)
                    print(f"Current turn total: {player.turn_total}")
            elif decision == 'h':
                player.bank_score()
                print(f"{player.name} holds. New total score: {player.score}")
                break
            else:
                print("Invalid input. Please enter 'r' to roll or 'h' to hold.")

    def check_winner(self):
        for player in self.players:
            if player.score >= 100:
                return player
        return None

    def start(self):
        print("=== Welcome to the Game of Pig! ===")
        while True:
            self.play_turn()
            
            winner = self.check_winner()
            if winner:
                print(f"\n*** {winner.name} wins with a score of {winner.score}! ***")
                break
                
            # Switch player turn
            self.current_player_idx = 1 - self.current_player_idx

if __name__ == "__main__":
    game = Game()
    game.start()
