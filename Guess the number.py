import random

Num_to_guess = random.randint(1,10)

attempts = 0

print("Welcome to the Guessing Game")
print("I'm thinking of a number between 1 and 10")

while True:
    user_guess = input("Guess a number: ")

    if user_guess.lower() == "quit":
        print("Okay, the number was {}".format(Num_to_guess))
        break
    try:
      user_guess = int(user_guess)
    except ValueError:
      print("That's not valid number!")
      continue

    attempts += 1
   
    if user_guess == Num_to_guess:
      print("Congratulations!! you found the right number.")
      print("You took {} attempts".format(attempts))

    elif user_guess < Num_to_guess:
     print("too low!")

    else:
        print ("too high!")
