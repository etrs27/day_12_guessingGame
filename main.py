from art import logo
import random

print(logo)
EASY_MODE = 10
HARD_MODE = 5

# Determine difficulty
def mode():
  type = input("Please choose a mode.\nType 'e' for Easy or 'h' for Hard. ").lower()
  if type == 'e':
    return EASY_MODE
  elif type == 'h':
    return HARD_MODE
# Guess!
def guess(attempts, chosenNumber):
  while attempts != 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    checker = check_guess(guess, chosenNumber)
    if checker:
      print(f"You guessed correctly. The answer is {chosenNumber}")
      break
    else:
      attempts -= 1
    if attempts == 0:
      print("You have run out of guesses. End of game.")
# Check answer against guess
def check_guess(guess, chosenNumber):
  if guess == chosenNumber:
    return True
  elif guess > chosenNumber:
    print("Too high.")
  else:
    print("Too low.")
# Game
def game():
  print("I'm thinking of a number between 1 and 100.")
  chosenNumber = random.randrange(1, 101)
  attempts = mode()
  guess(attempts, chosenNumber)
  restart = input("Play again? Yes or No? \n").lower()
  if restart == "yes":
    game()
  else:
    None
game()
