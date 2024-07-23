import random

class Hangman:
    def __init__(self,word,word_guessed,num_letters,list_of_guesses):
        self.word = word #Currently being called through usign the Fruit Variable
        self.num_letters = num_letters
        self.list_of_guesses = list_of_guesses
        self.word_guessed = word_guessed
        self.word_list = ["mango", "apple", "pear", "grape", "orange"]
        self.num_lives = 5

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print("")
            print(f"Well done, '{guess}', is in the word")
            print(self.list_of_guesses)
            print("")
            for index, character in enumerate(empty_list):
                if guess == character:
                    word_list[index] = guess
            self.num_letters = self.num_letters - 1
        else:
            print(f"Sorry, '{guess}', is not in the word")
            self.num_lives = self.num_lives - 1
            print("")

    def ask_for_input(self):
        while True:
            print(f"Number of Unique Letters Remaining {self.num_letters}")
            print(f"Number of Lives Remaining {self.num_lives}")
            print("")
            print(word_list)
            guess = input("Enter a Single Letter ")
            #print(guess)
            if guess.isalpha() == False or len(guess) > 1:
                print("Invalid letter. Please enter a single alphabetical character.")
                print("")
            elif guess in self.list_of_guesses:
                print("You've already tried that letter")
                print("")
            else:
                self.list_of_guesses.append(guess)
                self.check_guess(guess)

Fruit = "Banana" #Input any friut
num_letters = len(set(Fruit))
Fruit = Fruit.lower() #ensures the string is all lower case
empty_list = [] #Use to store each character of Fruits in a list
word_list = [] #Used to show correct letters ["_","_",etc.]
for character in Fruit:
  empty_list.append(character) #separates characters into elements in the list
  word_list.append("_") #assigns the number of spaces needed

Test_word = Hangman(Fruit,word_list,num_letters,[])
Test_word.ask_for_input()