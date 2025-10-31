#Charli Pape
#CIS256 2025
#EX 4

#Import random library
import random

#VARIABLES
# --Creation of lists
word_list = ["Potato", "Antarctica", "Treaty", "Penguins", "Isolation"]
guess_list = []


# --Chosing a word to guess from list randomly and making sure its all lowercase
word = (random.choice(word_list)).lower()

# --Variables for word length, # of guesses, and what is displayed to user
length = len(word)
num_of_guesses = 5
display_word = ["_"] * length

# --This variable will control when the while loop ends
completed = False


#Functions
def user_guess(user_word_display, user_input):
    """Checks to see if the user's input is in the word, if so it changes the displayed word's underscore to the actual letter via for in range. But if the input is not in the word, one life is lost"""
    
    #Made num_of_guesses public so that function does not raise error
    global num_of_guesses
    
    if user_input in word:
        for pos in range(length):
            if word[pos] == user_input:
                user_word_display[pos] = word[pos]
        print("Correct!")
        print(user_word_display)
    else:
        num_of_guesses -= 1
        print(f"Incorrect. You now have {num_of_guesses} guesses left.\n")
        print(user_word_display)
    

def was_not_guessed(user_input):
    """Checks to see if the user has already guessed the letter, if so function will return False. But if it's a new guess, the user's input will be added to the guess list and the function will return True"""
    
    if user_input not in guess_list:
        guess_list.append(user_input)
        return True
    else:
        print(f"Sorry, the letter '{user_input}' was already guessed.\n")
        return False



print(display_word)


#while loop
while completed == False:
    
    #Runs only if user has guesses left
    if num_of_guesses > 0:

        #input
        user_input = input("\nPlease guess one letter: ")

        #Runs was_not_guessed function and if true, user_guess function is ran. So if the user enters a new guess, the user_guess function will check if it is correct
        if was_not_guessed(user_input):
            user_guess(display_word, user_input)

        #Checks if the display word list (when a string) is equal to 
        if "".join(display_word) == word:
            print("\n Congrats! You guessed the word!!!!")
            completed = True
            break

    #Once user runs out of lives
    else:
        #Program will end and output the word
        completed = True
        print(f"You failed, the word was {word}")
        break

