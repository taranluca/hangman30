import random

word_list = ["Mango", "Apple", "Pear", "Grape", "Orange"]

word = random.choice(word_list)

#print(word)


def input_guess():
    guess = input("Enter a Single Letter ")
    if len(guess) == 1:
        return "Good Guess"
    else:
        print("Oops! That is not a valid input")
        return input_guess()
input_guess()