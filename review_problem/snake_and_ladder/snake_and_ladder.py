import numpy as np


def roll_die():
    return np.random.randint(1,7)


class SnakeAndLadder:
    def __init__(self, user_name):
        self.user_name = user_name
        self.position = 0

    def play_game(self):
        steps = roll_die()
        self.position += steps
