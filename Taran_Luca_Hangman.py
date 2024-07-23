import random

class Hangman:
    def __init__(self,word_list, num_lives):
        self.word = random.choice(word_list) #Code chooses a random word from the word_list
        self.word_guessed = [] #empty list used for the placeholders
        self.num_letters = len(set(self.word)) #determines the number of unique characters in the word
        self.list_of_guesses = [] #empty list used to store the previous characters selected by the player
        self.word = self.word.lower() #ensures the string is all lower case
        self.empty_list = [] #Use to store the separated character of word in a list
        for character in self.word:
            self.empty_list.append(character) #separates characters into elements in the list
            self.word_guessed.append("_") #assigns the number of spaces needed
        self.num_lives = num_lives

    def check_guess(self,guess):
        guess = guess.lower()                                       #ensures that the user's input it all lowercase
        if guess in self.word:                                      #if the inputted character matches a character in the selected word
            print(f"\nWell done, '{guess}', is in the word\n")      #prints well done and shows the letter that was correct
            print(f"Letters already used: {self.list_of_guesses}")  #shows the letters that have been inputted by the user
            for index, character in enumerate(self.empty_list):     #using enumerate to produce the index for all characters in the list
                if guess == character:                              #if the matching character(s) are selected
                    self.word_guessed[index] = guess                #puts the inputted character(s) into the correct place(s) into the word
            self.num_letters = self.num_letters - 1                 #lowers the number of unique characters left to find
        else:
            print(f"Sorry, '{guess}', is not in the word\n")        #prints sorry the letter inputted is not present in the word
            self.num_lives = self.num_lives - 1                     #removes one life from the total lives

    def ask_for_input(self):
        while True:                                                 #infinte loop
            if self.num_lives == 0:                                 #if lives have dropped to zero
                print("Game Over! You Lost!")                       #prints game over
                print(f"The Word Was: {self.word.capitalize()}")    #shows the answer (and capitalises the first character)
                break                                               #exits the program
            if self.num_letters > 0:                                #if there are still unique letters left to find
                pass                                                #carry on with the program
            if self.num_lives != 0 and self.num_letters == 0:       #if lives are not at zero and there are no more unique letters to find
                print("Congratulations! You won the game!")         #prints congratulations
                print(f"The Word Was: {self.word.capitalize()}")    #shows the answer (and capitalises the first character)
                break                                               #exits the program

            #print(f"Number of Unique Letters Remaining: {self.num_letters}")   code kept if you want to validate the number of unique letters left
            
            print(f"Number of Lives Remaining: {self.num_lives}")   #prints the number of lives remaining            
            print(f"Letters Guessed So Far: {self.word_guessed}")   #shows the letters (and in the correct place) that have been guessed correctly
            guess = input("Enter a Single Letter ")                 #input for the user to select a letter
            if guess.isalpha() == False or len(guess) > 1:          #validates that the input is both a single and an alphabetical character
                print("Invalid letter. Please enter a single alphabetical character.\n")    #prints error so that the user is aware their input has not be registered correctly
            elif guess in self.list_of_guesses:                     #if the inputted letter has already been used previously (correct or incorrect)
                print("You've already tried that letter\n")         #prints showing the user has used this character before
            else:                                                   #if the correct critera has been met the code continues
                self.list_of_guesses.append(guess)                  #this adds the valid input to the list of characters inputted and registered through the program
                self.check_guess(guess)                             #this calls the check_guess method to run

word_list = ["mango", "apple", "pear", "grape", "orange","banana"] #Input any word or assign any list of strings to this variable
num_lives = 5                                                      #Starting number of lives

def play_game():                                                   #Function that runs all of the code above
    game = Hangman(word_list,num_lives)                            #Collects variable game assigned to the class. Inputting the word_list and num_lives into it
    game.ask_for_input()                                           #Line that runs the class function


play_game()                                                        #Line that runs the game function thus running the class