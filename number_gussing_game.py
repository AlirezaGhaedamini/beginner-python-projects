import random

random_number = random.randint(1, 10)
guess = None
tries = 0

while guess != random_number:
    guess = int(input("Guess a number between 1 and 10: "))
    tries += 1
    if guess < random_number:
        print("Too low!")
    elif guess > random_number:
        print("Too high!")
    else:
        print(f"🎉 Correct! You guessed it in {tries} tries.")