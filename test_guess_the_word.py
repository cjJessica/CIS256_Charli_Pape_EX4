#Charli Pape
#CIS256 2025
#EX 4 - test_guess_the_word.py

#Import the random_word and user_guess from check_guess
from guess_the_word import check_guess, random_word


def test_random_word():
    test_list = ["Test", "Capital", "Notes"]
    test_word = random_word(test_list)
    assert test_word in [item.lower() for item in test_list]

def test_check_guess():
    word = "test"
    user_display = ["_"] * len(word)
    

    assert check_guess(user_display, "t", word) == True
    assert check_guess(user_display, "w", word) == False