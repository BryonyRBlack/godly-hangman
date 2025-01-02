# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

#Add ons to be imported to ensure the program runs as intended
import random
import string
import os

#Word lists to import
from greek import greek_gods
from roman import roman_gods
from viking import viking_gods

#The Hangman image to be printed after each guess
from hangman import HANGMAN

#Function user will see on loading game
def start_page():
    print("Welcome to Godly Hangman\n")
    while True:
        name = input("Please enter your name: \n")
        if not name.isalpha():
            print("Please only enter letters")
        else:
            print(f"Welcome to Hangman {name}!\n")
            break
    global category
    category = choice()
    return category

#Function to give the user different game categories
def choice():
    print("Please pick a category using 1, 2 or 3\n")
    while True:
        try:
            user_choice = int(input("1. Greek Gods, 2. Roman Gods or 3. Viking Gods"))
        except ValueError:
            print("Please pick either 1, 2 or 3")
            continue
        if user_choice < 0 or user_choice > 3:
            print("Only 1, 2 or 3 are valid options")
            continue
        else:
            break
    if user_choice == 1:
        category = "Greek Gods"
        print("You have chosen Greek Gods!\n")
    elif user_choice == 2:
        category = "Roman Gods"
        print("You have chosen Roman Gods!\n")
    elif user_choice == 3:
        category == "Viking Gods"
        print("You have chosen Viking Gods!\n")
    else:
        print("Invalid choice, please try again")
    
    return category

#This function selects a random word from the list for the user to try and guess
def word_to_guess():
    if category == "Greek Gods":
        word = random.choice(greek_gods)
        return word.upper()
    elif category == "Roman Gods":
        word = random.choice(roman_gods)
        return word.upper()
    else:
        word = random.choice(viking_gods)
        return word.upper()

#This function is the basic hangman game
def hangman_game():
    #This takes the word from the word_to_guess function, and breaks it down in order for the user to guess
    clear()
    word = word_to_guess()
    letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    #This sets the lives at 7 from the start of the game for the game logic to work
    lives = 7

    #This reads the users input of a letter, and displays the current lives, guessed letters
    #and "-" for letters not yet guessed
    while len(letters) > 0 and lives > 0:
        print("You have", lives, "remaining. You have guessed:", "".join(used_letters))
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("".join(word_list))
        guessed_letter = input("Guess a letter: ").upper()
        
        #This displays if the user has guessed the correct letter
        if guessed_letter in alphabet - used_letters:
            clear()
            print(HANGMAN[lives])
            print(guessed_letter, "is in the word")
            used_letters.add(guessed_letter)
            
            if guessed_letter in letters:
                letters.remove(guessed_letter)
                print("")
            
            #This runs if the guessed letter is not in the word. It also removes a life
            else:
                clear()
                lives = lives - 1
                print(HANGMAN[lives])
                print(guessed_letter, "is not in this word")

        #This runs if the user has guessed a letter they have previously guessed    
        elif guessed_letter in used_letters:
            clear()
            print(HANGMAN[lives])
            print("You have already guessed this letter. Please try again")

        #This only runs if the user attempts to input something that is not a letter
        else:
            clear()
            print(HANGMAN[lives])
            print("Please only guess a letter")

        #This is the end of the game. If the user has no lives remaining it confirms the word
        #else it congratulates the user for guessing it correctly
        if lives == 0:
            print("You have died. The word was", word)
        else:
            print("Congratulations! You guessed the word was", word)
        
        play_again()

#This function allows the user to play again
def play_again():
    while True:
        try:
            print("Would you like to play again?\n")
            run_again = input("Yes or no?: ").lower()
            if run_again == "yes":
                run_game()
                break
            elif run_again == "no":
                print("Thank you for playing!")
                break
        except ValueError:
            print("Please enter yes or no")


#Code taken from https://www.geeksforgeeks.org/clear-screen-python/
#This keeps the console clear, as it removes previous inputs
def clear():
        # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

start_page()

def run_game():
    choice()
    word_to_guess()
    hangman_game()

#This runs the game
if __name__ == "main":
    hangman_game()