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
'''

import numpy as np 


class DeckOfCards:
    def __init__(self):
        self.SUIT=np.array(['Clubs','Diamonds','Hearts','Spades']*13)
        self.RANK=np.array(['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']*4)
        self.count=0
    
    def Shuffle(self):
        np.random.shuffle(self.SUIT)
        np.random.shuffle(self.RANK)
    
    def distribute(self,no_of_cards):
        return [
            np.random.choice(self.SUIT,no_of_cards),
            np.random.choice(self.RANK,no_of_cards)
        ]