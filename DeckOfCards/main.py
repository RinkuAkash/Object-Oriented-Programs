from DeckOfCards import DeckOfCards

"""
Created on 29/01/2020
@author: B Akash
"""
"""
Problem statement:
Write a Program DeckOfCards.java, to initialize deck of cards
 having suit ("Clubs", "Diamonds", "Hearts", "Spades") & Rank
  ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King",
   "Ace"). Shuffle the cards using Random method and then distribute
   9 Cards to 4 Players and Print the Cards the received by the
   4 Players using 2D Array…
"""


if __name__ == "__main__":

    cards = DeckOfCards()
    cards.Shuffle()

    player1 = cards.distribute(9)
    player2 = cards.distribute(9)
    player3 = cards.distribute(9)
    player4 = cards.distribute(9)

    player1.sort()
    player2.sort()
    player3.sort()
    player4.sort()

    print("player1 cards")
    player1.show()
    print("\nplayer2 cards")
    player2.show()
    print("\nplayer3 cards")
    player3.show()
    print("\nplayer4 cards")
    player4.show()
