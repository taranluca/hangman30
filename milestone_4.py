import random

class Hangman:
    def __init__(self,word,word_guessed,num_letters,list_of_guesses):
        self.word = word
        self.num_letters = num_letters
        self.list_of_guesses = list_of_guesses
        self.word_guessed = word_guessed
        self.word_list = ["mango", "apple", "pear", "grape", "orange"]
        self.num_lives = 5

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print(f"Well done, '{guess}', is in the word")
            print(self.list_of_guesses)
            print("")
        else:
            print(f"Sorry, '{guess}', is not in the word")

    def ask_for_input(self):
        while True:
            print(word_list)
            guess = input("Enter a Single Letter ")
            print(guess)
            if guess.isalpha() == False or len(guess) > 1:
                print("Invalid letter. Please enter a single alphabetical character.")
            elif guess in self.list_of_guesses:
                print("You've already tried that letter")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)

Fruit = "Banana" #Input any friut
Fruit = Fruit.lower() #ensures the string is all lower case
empty_list = [] #Use to store each character of Fruits in a list
word_list = [] #Used to show correct letters ["_","_",etc.]
for character in Fruit:
  empty_list.append(character) #separates characters into elements in the list
  word_list.append("_") #assigns the number of spaces needed

Test_word = Hangman(Fruit,word_list,5,[])
Test_word.ask_for_input()