import numpy as np


def roll_die():
    return np.random.randint(1, 7)


class SnakeAndLadder:
    def __init__(self, user_name):
        self.user_name = user_name
        self.position = 0
        self.roll_count = 0

    def play_game(self):
        steps = roll_die()
        self.roll_count += 1
        option = np.random.randint(0, 3)
        if option == 0:
            self.position -= steps
            if self.position < 0:
                self.position = 0
            print("You got snake")
        elif option == 1:
            if self.position + steps > 100:
                print("No moment")
            elif self.position + steps == 100:
                print("Congratulations, you won")
            else:
                self.position += steps
                print("You got ladder")
        else:
            if self.position + steps > 100:
                print("No moment")
            else:
                self.position += steps
                if self.position == 100:
                    print("Congratulations, you won")
                    return False

        return True
