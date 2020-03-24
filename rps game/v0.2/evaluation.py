# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 18:33:41 2020

@author: splin
"""

# this file contains a couple of fuctions that evaluate turns in the rps game

def evaluate(move, value, result):
    if result == 'draw':
        print(move + ' versus... ' + value)
        print('It is a tie')
        
    elif result == 'victory':
        print(move + ' versus... ' + value)
        print('You win!')
    
    elif result == 'defeat':
        print(move + ' versus... ' + value)
        print('You lose.')
        
def score(wins, losses, ties):
    print(str(wins) + " "+ "Wins", str(losses) +" "+ "Losses", str(ties) +" "+ "Ties",
      sep=', ')
    