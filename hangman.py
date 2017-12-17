#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 21:37:43 2017

@author: tsengler
"""
import os
import random

# =============================================================================
 
def hangman(word):
    wrong = 0
    stages = ["",
              "__________          ",
              "|                   ",
              "|         |         ",
              "|         O         ",
              "|        /|\        ",
              "|        / \        ",
              "|                   ",
              ]
    rletters = list(word)
    board = ["__"] * len(word)
    #lettersGuessed = []
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        while len(char) != 1:
            print("Please enter only one letter. No more no less.")
            char = input(msg)
        if char in rletters:
            while char in rletters:
                cind = rletters.index(char)
                board[cind] = char
                rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        #lettersGuessed.append(char)
        #print(sorted(lettersGuessed))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
       
    if not win:
        print("\n".join(stages[0:wrong]))
        print("You lose dummy! It was {}. So easy!".format(word))
         
 
# =============================================================================

words = []
file1 = os.path.join("/", "Users", "tsengler", "Desktop", "test_files", \
                     "largedict")

with open(file1, 'r') as f:
    for line in f:
        words.append(line.strip())


#hangman("mississippi")
hangman(random.choice(words))