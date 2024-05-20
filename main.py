import random

gameActive = True
chosenNumber = random.randrange(1, 100)
print("I'm thinking of a number between 1 and 100.")
modeType = str(input("Please choose a mode. 'e' for Easy or 'h' for Hard. ")).lower()
if modeType == 'e':
  attempts = 10
elif modeType == 'h':
  attempts = 5
else:
  print("I could not understand your selection. Try again.")
  gameActive = False

while gameActive:
  print(f"You have {attempts} attempts remaining to guess the number.")
  guess = int(input("Make a guess: "))
  if guess == chosenNumber:
    print(f"You guessed correctly. The answer is {chosenNumber}")
    gameActive = False
    break
  elif guess > chosenNumber:
      print("Too high.")
  else:
      print("Too low.")
  attempts -= 1
  if attempts == 0 and guess != chosenNumber:
    print("You have run out of guesses. Play again.")
    gameActive = False
  else:
    print("Guess again.")