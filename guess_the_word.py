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

# --Variables for word length and # of guesses
length = len(word)
num_of_guesses = 5

# --This variable will control when the while loop ends
completed = False


#Function
def user_guess(user_word_display, user_input, lives):

    if user_input in word:
        for pos in range(length):
            if word[pos] == user_input:
                user_word_display[pos] = word[pos]
                print(user_word_display)
    else:
        lives -= 1
        print(f"You now have {lives} guesses left.")
    


display_word = ["_"] * length
user_guess(display_word, "a", num_of_guesses)

#while loop
#while completed == False:
    #user input
