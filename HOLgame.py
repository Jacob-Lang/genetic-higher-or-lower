# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from random import randint

# gets input (guess between upper and lower bounnd) from human or computer via a range of methods. 
def inputAll(method, lower_bound, upper_bound, nguesses):
    if method == "human":
        message = "Pick a number between " + str(lower_bound) + " and " + str(upper_bound) + ": \n"
        while True:
            try:
                userInput = int(input(message))       
            except ValueError:
                print("Please input a whole number. Try again: \n")
                continue
            else:
                return userInput 
            break
    elif method == "computer_random":
        return randint(lower_bound, upper_bound)
    elif method == "computer_bifurcate":
        return int(round((upper_bound + lower_bound)/2))
    elif method == "computer_bad":
        return lower_bound
    elif type(method) != str:
        ri = method[nguesses]
        return int(round(lower_bound + ri*(upper_bound - lower_bound)))  

# checks if target is higher or lower than guess and returns new bounds
# returns run = "False" if guess is correct
def checkNumber(Ngoal, Nchoice, lower_bound, upper_bound):
    if Nchoice == Ngoal:
#        print("YES! CONGRATULATIONS! THE NUMBER WAS ", Ngoal,)
        new_upper_bound = Ngoal
        new_lower_bound = Ngoal
        return [new_lower_bound, new_upper_bound, "False"] # "False" tells game to not run again
    elif Nchoice < Ngoal:
#        print("Nope. You need to go higher.")
        new_lower_bound = max(Nchoice + 1, lower_bound)
        new_upper_bound = upper_bound
        return [new_lower_bound, new_upper_bound, "True"]
    elif Nchoice > Ngoal:
#        print("Nope. You need to go lower.")
        new_lower_bound = lower_bound
        new_upper_bound = min(Nchoice - 1, upper_bound)
        return [new_lower_bound, new_upper_bound, "True"]
    
    
# game engine
def playGame(method, lower_bound, upper_bound):        
#    print("\n")
#    print("Let's play higher or lower.")
    
    Ngoal = randint(lower_bound, upper_bound)
    
    nguesses = 0
    
    run = "True"
    while run == "True":
    
        # advance game
        string = "Pick a number between " + str(lower_bound) + " and " + str(upper_bound)
#        print(string)
        
        # get input
        try:
            Nchoice = inputAll(method, lower_bound, upper_bound, nguesses)
        except IndexError:
#            print("Out of guesses")
            break
#        print(Nchoice)
    
        # increase guess count
        nguesses = nguesses + 1
        
        #check input
        [lower_bound, upper_bound, run] = checkNumber(Ngoal, Nchoice, lower_bound, upper_bound)  
            
    distance = abs(Ngoal - Nchoice)
#    print("The target was " + str(Ngoal))
#    print("You were " + str(distance) + " away after " + str(nguesses) + " guesses.")
    return[distance, nguesses]
    

