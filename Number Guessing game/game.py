import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

print("🎯 Number Guessing Game")
print("I have chosen a number between 1 and 100.")
print("Try to guess it!")

while True:
    try:
        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Too low! Try again.")
        elif guess > number:
            print("Too high! Try again.")
        else:
            print("🎉 Congratulations! You guessed the correct number!")
            break

    except ValueError:
        print("Invalid input. Please enter a number.")