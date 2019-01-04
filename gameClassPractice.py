# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 14:37:09 2018

@author: Jacob
"""

from random import randint

class Player():
    """This is a class that represents a player in the game"""
    def __init__(self):
        self.method= "human"     # automatically set to human player. see guess() for options
        self.guesses = []        # record guesses made here
        self.quit = "False"      # can quit if out of guesses
        
    def guess(self, lower_bound, upper_bound):
        if self.method == "human":
            while True:
                try:
                    guess = int(input())       # takes human guess
                except ValueError:
                    print("Please input a whole number. Try again: \n")   # error handling
                    continue
                else:
                    self.guesses.append(guess)
                    return guess 
                break
        elif self.method == "computer_random":   # randomly guesses within bounds
            guess = randint(lower_bound, upper_bound)
            self.guesses.append(guess)
            return guess
        elif self.method == "computer_bifurcate":  # picks a number halfway between bounds
            guess = int(round((upper_bound + lower_bound)/2))
            self.guesses.append(guess)
            return guess
        elif self.method == "computer_bad":  #just picks the lower bound. 
            guess = int(lower_bound)
            self.guesses.append(guess)
            return guess
        elif type(self.method) != str:    
            # e.g. [0.25, 0.5] guesses 1/4 between first set of bounds then 1/2.
            # then quits
            nguesses = len(self.guesses)  # number of guesses made so far
            if nguesses < len(self.method): # does method have any guesses left?
                ri = self.method[nguesses]  # current split ratio
                guess = int(round(lower_bound + ri*(upper_bound - lower_bound)))
                self.guesses.append(guess)  
                return guess
            elif nguesses == len(self.method): # if not ...
                self.quit = "True"
                return "QUIT"   # forces game to quit
                
class Game():
    """This is a class that represents the game"""
    def __init__(self):
        self.lower_bound = 1
        self.upper_bound = 100
        self.goal = randint(self.lower_bound, self.upper_bound)   # randomly choose number
        self.quit = "False"        # can switch to true to force quit
        self.method = "human"
        self.guesses = []
        self.narrate = "True"
        
    def requestGuess(self):  # prints text requesting number. can be neglected when running the game many time
        print("Pick a number between " + str(self.lower_bound) + " and " + str(self.upper_bound) + ":")
        
    def checkGuess(self, guess):   # checks guess and updates bounds. checks for guess = "QUIT"  command.
        if type(guess) == str:
            self.quit = "True"
        elif guess == self.goal:
            self.lower_bound = self.goal
            self.upper_bound = self.goal
            self.quit = "True"
        elif guess < self.goal:
            self.lower_bound = max(guess + 1, self.lower_bound)  # update lower bound
        elif guess > self.goal:
            self.upper_bound = min(guess - 1, self.upper_bound)  # update upper bound   
            
                
    def guess(self, lower_bound, upper_bound):
        if self.method == "human":
            while True:
                try:
                    guess = int(input())       # takes human guess
                except ValueError:
                    print("Please input a whole number. Try again: \n")   # error handling
                    continue
                else:
                    self.guesses.append(guess)
                    return guess 
                break
        elif self.method == "computer_random":   # randomly guesses within bounds
            guess = randint(lower_bound, upper_bound)
            self.guesses.append(guess)
            return guess
        elif self.method == "computer_bifurcate":  # picks a number halfway between bounds
            guess = int(round((upper_bound + lower_bound)/2))
            self.guesses.append(guess)
            return guess
        elif self.method == "computer_bad":  #just picks the lower bound. 
            guess = int(lower_bound)
            self.guesses.append(guess)
            return guess
        elif type(self.method) != str:    
            # e.g. [0.25, 0.5] guesses 1/4 between first set of bounds then 1/2.
            # then quits
            nguesses = len(self.guesses)  # number of guesses made so far
            if nguesses < len(self.method): # does method have any guesses left?
                ri = self.method[nguesses]  # current split ratio
                guess = int(round(lower_bound + ri*(upper_bound - lower_bound)))
                self.guesses.append(guess)  
                return guess
            elif nguesses == len(self.method): # if not ...
                self.quit = "True"
                return "QUIT"   # forces game to quit
            
    def narrateProgress(self, guess): # prints the result of the guess. can also be neglected. 
        if type(guess) == str:
            0
        elif guess == self.goal:
           print("YES! CONGRATULATIONS! THE NUMBER WAS ", self.goal,)
           print("You got the answer correct after " + str(len(self.guesses)) + " guesses.")
        elif guess < self.goal:
            print("Nope. You need to go higher.")
        elif guess > self.goal:
           print("Nope. You need to go lower.")
        elif type(guess) == str:
           print("You are out of guesses")
       
    def playGame(self):
        while self.quit == "False":
            if self.narrate == "True":
                self.requestGuess()
            guess = self.guess(self.lower_bound, self.upper_bound)
            if self.narrate == "True" and self.method != "human":
                print(guess)
            self.checkGuess(guess)
            if self.narrate == "True":
                self.narrateProgress(guess)
                
    def reset(self):
        self.lower_bound = 1
        self.upper_bound = 100 
        self.goal = randint(self.lower_bound, self.upper_bound)   # randomly choose number
        self.quit = "False"        # can switch to true to force quit
        self.guesses = []


def main():
    game = Game()
    game.playGame()
      
if __name__== "__main__":
    main()
