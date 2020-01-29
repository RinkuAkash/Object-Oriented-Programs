'''
Created on 28/01/2020
@author: B Akash
'''
'''
Problem statement:
Write a Program DeckOfCards.java, to initialize deck of cards having suit
 ("Clubs", "Diamonds", "Hearts", "Spades") & Rank
 ("2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace").
 Shuffle the cards using Random method and then distribute 9 Cards to 4 Players 
 and Print the Cards the received by the 4 Players using 2D Array…

 Extend the above program to create a Player Object having Deck of Cards, and having
  ability to Sort by Rank and maintain the cards in a Queue implemented using
   Linked List. Do not use any Collection Library. Further the Player are also arranged
    in Queue. Finally Print the Player and the Cards received by each Player.
'''

import numpy as np 
from queue import Queue

class DeckOfCards:
    def __init__(self):
        self.SUIT=np.array(['Clubs','Diamonds','Hearts','Spades']*13)
        self.RANK=np.array(['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']*4)
    
    def Shuffle(self):
        np.random.shuffle(self.SUIT)
        np.random.shuffle(self.RANK)
    
    def distribute(self,no_of_cards):
        queue = Queue()
        randomCards = zip(
            np.random.choice(self.SUIT,no_of_cards),
            np.random.choice(self.RANK,no_of_cards)
        )

        for suit, rank in randomCards:
            queue.addRear(suit, rank)
        
        return queue