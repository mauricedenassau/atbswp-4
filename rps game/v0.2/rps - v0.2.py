# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:07:31 2020

@author: splin
"""
import random, sys
from evaluation import score, evaluate
# rock paper scissors game
print('ROCK, PAPER, SCISSORS')
wins = 0
losses = 0
ties = 0
moves = {'r': 'ROCK', 'p': 'PAPER', 's': 'SCISSORS'}

# random.choices generates a list with a single value from default, i proceed
# to unlist that new generated value
while True: 
    score(wins, losses, ties)
    while True:

# this seems confusing, but i did this so there was no need to create a list
# with each one of the moves
        value = random.choices([v for v in moves.values()]).pop()
        print("Enter your move: (r)ock, (p)aper, (s)cissors or (q)uit")
        move = input()
        
        if move == 'q':
            sys.exit()
        
        elif move in ['p', 'r', 's', 'q']:
            break
        print('Type one of r, p, s, or q.')
        
    if moves[move] == value:
        evaluate(moves[move], value, 'draw')
        ties = ties + 1
    
    elif moves[move] == 'ROCK' and value == 'SCISSORS':
        evaluate(moves[move], value, 'victory')
        victorys = wins + 1

    elif moves[move] == 'ROCK' and value == 'PAPER':
        evaluate(moves[move], value, 'defeat')
        losses = losses + 1
            
    elif moves[move] == 'PAPER' and value == 'ROCK':
        evaluate(moves[move], value, 'victory')
        wins = wins + 1
    
    elif moves[move] == 'PAPER' and value == 'SCISSORS':
        evaluate(moves[move], value, 'lose')
        losses = losses + 1
    
    elif moves[move] == 'SCISSORS' and value == 'ROCK':
        evaluate(moves[move], value, 'lose')
        losses = losses + 1
        
    elif moves[move] == 'SCISSORS' and value == 'PAPER':
        evaluate(moves[move], value, 'victory')
        wins = wins + 1
