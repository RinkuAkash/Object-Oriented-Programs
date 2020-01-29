'''
Created on 29/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Program DeckOfCards.java, to initialize deck of cards
 having suit ("Clubs", "Diamonds", "Hearts", "Spades") & Rank
  ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace").
   Shuffle the cards using Random method and then distribute 9 Cards to 4 Players and
    Print the Cards the received by the 4 Players using 2D Array…

'''

from DeckOfCards import *

if __name__=='__main__':

    cards=DeckOfCards()
    cards.Shuffle()
    print(np.array([
        cards.distribute(9),
        cards.distribute(9),
        cards.distribute(9),
        cards.distribute(9)
    ])
    )