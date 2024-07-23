import random

class Hangman:
    def __init__(self,word_list, num_lives):
        self.word = word = random.choice(word_list)
        print(word)
        self.word_guessed = []
        self.num_letters = len(set(word))
        self.list_of_guesses = []
        word = word.lower() #ensures the string is all lower case
        self.empty_list = [] #Use to store each character of Fruits in a list
        for character in word:
            self.empty_list.append(character) #separates characters into elements in the list
            self.word_guessed.append("_") #assigns the number of spaces needed
        self.num_lives = num_lives

    def check_guess(self,guess):
        guess = guess.lower()
        if guess in self.word:
            print("")
            print(f"Well done, '{guess}', is in the word")
            print(f"Letters guessed already: {self.list_of_guesses}")
            print("")
            for index, character in enumerate(self.empty_list):
                if guess == character:
                    self.word_guessed[index] = guess
            self.num_letters = self.num_letters - 1
        else:
            print(f"Sorry, '{guess}', is not in the word")
            self.num_lives = self.num_lives - 1
            print("")

    def ask_for_input(self):
        while True:
            if self.num_lives == 0:
                print("Game Over! You Lost!")
                break
            if self.num_letters > 0:
                pass
            if self.num_lives != 0 and self.num_letters == 0:
                print("Congratulations! You won the game!")
                print(f"The Word Was: {self.word}")
                break

            print(f"Number of Unique Letters Remaining: {self.num_letters}")
            print(f"Number of Lives Remaining: {self.num_lives}")
            print("")
            print(self.word_guessed)
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

word_list = ["mango", "apple", "pear", "grape", "orange","banana"] #Input any word
num_lives = 5

#Test_word = Hangman(word_list,num_lives)
#Test_word.ask_for_input()

def play_game():
    num_lives = 5
    game = Hangman(word_list,num_lives)
    game.ask_for_input()


play_game()