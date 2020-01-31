class SnakeAndLadder:
    def __init__(self, user_name):
        self.user_name = user_name
        self.position = 0
        self.SNAKES = {
            32: 10,
            36: 6,
            48: 26,
            62: 18,
            88: 24,
            95: 56,
            97: 78
        }
        self.LADDERS = {
            1: 38,
            4: 14,
            8: 30,
            21: 42,
            28: 76,
            50: 67,
            71: 92,
            80: 99
        }