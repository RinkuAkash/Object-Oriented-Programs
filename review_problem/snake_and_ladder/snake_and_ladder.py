import numpy as np


def roll_die():
    return np.random.randint(1,7)


class SnakeAndLadder:
    def __init__(self, user_name):
        self.user_name = user_name
        self.position = 0

    def play_game(self):
        steps = roll_die()
        option = int(input())
        if option == 2:
            self.position -= steps
            if self.position < 0:
                self.position = 0
        elif option == 3:
            self.position += steps
