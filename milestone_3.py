
the_word = "apple"

def check_guess(guess):
  guess = guess.lower()
  if guess in the_word:
      print(f"Well done, '{guess}', is in the word")
  else:
      print(f"Sorry, '{guess}', is not in the word")

def ask_for_input():
    while True:
        guess = input("Enter a Single Letter ")
        if guess.isalpha() == True:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    check_guess(guess)
ask_for_input()