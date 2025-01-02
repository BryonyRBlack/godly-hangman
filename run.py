# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high



#Word lists to import
from greek import greek_gods
from roman import roman_gods
from viking import viking_gods

#The Hangman image to be printed after each guess
from hangman import HANGMAN

#This function selects a random word from the list for the user to try and guess
def word_to_guess():
    word = random.choice(greek_gods)
    return word.upper