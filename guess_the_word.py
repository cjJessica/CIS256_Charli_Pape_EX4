#Charli Pape
#CIS256 2025
#EX 4

#Import random library
import random

#VARIABLES
# --Creation of lists
word_list = ["Potato", "Antarctica", "Treaty", "Penguins", "Isolation"]
guess_list = []

guess = ""

# --Chosing a word to guess from list randomly and making sure its all lowercase
word = (random.choice(word_list)).lower()
print(word)

# --Variables for word length, # of guesses, and what is displayed to user
length = len(word)
num_of_guesses = 5
display_word = ["_"] * length

# --This variable will control when the while loop ends
completed = False


#Functions
def user_guess(user_word_display, user_input, lives):

    if user_input in word:
        for pos in range(length):
            if word[pos] == user_input:
                user_word_display[pos] = word[pos]
                print(user_word_display)
    else:
        lives -= 1
        print(f"You now have {lives} guesses left.")
    

def was_not_guessed(user_input):
    if user_input not in guess_list:
        guess_list.append(user_input)
        return True
    else:
        print(f"Sorry, {user_input} was already guessed.")
        return False


user_guess(display_word, "a", num_of_guesses)

#while loop
while completed == False:
    if num_of_guesses > 0:

