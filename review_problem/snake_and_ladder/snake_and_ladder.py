import numpy as np


def roll_die():
    return np.random.randint(1, 7)


class SnakeAndLadder:
    def __init__(self, user_name):
        self.user_name = user_name
        self.position = 0

    def play_game(self):
        steps = roll_die()
        option = np.random.randint(0, 3)
        if option == 0:
            self.position -= steps
            if self.position < 0:
                self.position = 0
            print("You got snake")
        elif option == 1:
            self.position += steps
            print("You got ladder")
        else:
            if self.position + steps > 100:
                print("No moment")
            else:
                self.position += steps
