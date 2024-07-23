import random

class Hangman:
    def __init__(self,word,word_guessed,num_letters,list_of_guesses):
        self.word = word #Currently being called through usign the Fruit Variable
        self.word_guessed = word_guessed
        self.num_letters = num_letters
        self.list_of_guesses = list_of_guesses
        self.word_list = ["mango", "apple", "pear", "grape", "orange","banana"]
        self.num_lives = 5

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print("")
            print(f"Well done, '{guess}', is in the word")
            print(f"Letters guessed already: {self.list_of_guesses}")
            print("")
            for index, character in enumerate(empty_list):
                if guess == character:
                    word_guessed[index] = guess
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
            print(word_guessed)
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

word_list = ["mango", "apple", "pear", "grape", "orange","banana"] #Input any friut
word = random.choice(word_list)
print(word)
num_letters = len(set(word))
word = word.lower() #ensures the string is all lower case
empty_list = [] #Use to store each character of Fruits in a list
word_guessed = [] #Used to show correct letters ["_","_",etc.]
for character in word:
  empty_list.append(character) #separates characters into elements in the list
  word_guessed.append("_") #assigns the number of spaces needed

Test_word = Hangman(word,word_guessed,num_letters,[])
Test_word.ask_for_input()