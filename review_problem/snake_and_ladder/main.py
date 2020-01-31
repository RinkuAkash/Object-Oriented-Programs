from snake_and_ladder import SnakeAndLadder

if __name__ == "__main__":
    print("The Snake And Ladder Game")

    # Taking players name as input
    player1_name = input('Enter player1 name : ')
    player2_name = input("Enter player2 name : ")
    player1 = SnakeAndLadder(player1_name)
    player2 = SnakeAndLadder(player2_name)

    # Repeating game till any player wins
    while True:
        if not player1.play_game:
            break
        if not player2.play_game:
            break
    print("Dice roll count : ", player1.roll_count)
