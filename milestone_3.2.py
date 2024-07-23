
the_word = "apple"
list_of_guesses = ["p","e","l"]
def check_guess(guess):
  guess = guess.lower()
  if guess in the_word:
      print(f"Well done, '{guess}', is in the word")
  else:
      print(f"Sorry, '{guess}', is not in the word")

def ask_for_input():
    while True:
        guess = input("Enter a Single Letter ")
        if guess.isalpha() == False or len(guess) > 1:
            print(len(guess))
            print("Invalid letter. Please, enter a single alphabetical character.")
        elif guess in list_of_guesses:
            print("You've already tried that")
        else: break
            
    check_guess(guess)
ask_for_input()