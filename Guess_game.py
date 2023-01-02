import random

# define the game
class Game:
  def __init__(self):
    self.number = random.randint(1, 10)

  def start(self):
    print("I'm thinking of a number between 1 and 10. Can you guess what it is?")
    while True:
      guess = int(input("Enter your guess: "))
      if guess == self.number:
        print("You got it! Congratulations!")
        break
      elif guess < self.number:
        print("Your guess is too low. Try again.")
      else:
        print("Your guess is too high. Try again.")

# create a new game and start it
game = Game()
game.start()
