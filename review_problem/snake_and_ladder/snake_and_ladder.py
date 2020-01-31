import numpy as np


# Static method to roll dice using random function1
def roll_die():
    return np.random.randint(1, 7)


class SnakeAndLadder:
    def __init__(self, user_name):
        self.user_name = user_name
        self.position = 0
        self.roll_count = 0

    # Method to check position of player with conditions
    def check_position_count(self, steps):
        if self.position + steps > 100:
            print("No moment")
            return True
        elif self.position + steps == 100:
            print("Congratulations,", self.user_name, "won")
            return False
        else:
            self.position += steps
            return True

    # Method to play game, returns True if game continues
    def play_game(self):
        steps = roll_die()
        self.roll_count += 1

        # option is used to get snake, ladder or no play
        option = np.random.randint(0, 3)
        if option == 0:
            self.position -= steps
            if self.position < 0:
                self.position = 0
            print("You got snake")
        elif option == 1:
            if self.check_position_count(steps):
                print("you got ladder")
            else:
                return False
        else:
            if self.check_position_count(steps) is False:
                return False
        print("After rolling a die,", self.user_name,
              "at", self.position, "position")

        return True
