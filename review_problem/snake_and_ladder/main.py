from snake_and_ladder import SnakeAndLadder

if __name__ == '__main__':
    print("The Snake And Ladder Game")
    user_name = input("Enter your name to start : ")
    player1 = SnakeAndLadder(user_name)
    print(player1.user_name, 'at', player1.position, 'position')