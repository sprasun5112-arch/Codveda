# 🎯 Number Guessing Game

A simple Python-based **Number Guessing Game** where the computer randomly selects a number between **1 and 100**, and the user tries to guess it. The program provides feedback after each guess, indicating whether the guess is too high or too low.

## 📌 Features

* Generates a random number between 1 and 100.
* Allows the user to enter guesses repeatedly.
* Gives feedback:

  * **Too high** if the guess is greater than the target number.
  * **Too low** if the guess is smaller than the target number.
  * **Correct** when the user guesses the number.
* Handles invalid input.
* Ends the game when the correct number is guessed.

## 🛠️ Technologies Used

* **Python 3**
* `random` module

## 📂 Project Structure

```text
number-guessing-game/
│
├── guessing_game.py
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the installed version:

```bash
python --version
```

### 2. Run the Program

Open a terminal in the project folder and run:

```bash
python guessing_game.py
```

## 🎮 How to Play

1. The computer randomly generates a number between **1 and 100**.
2. Enter your guess when prompted.
3. The program will tell you:

   * `Too low! Try again.` if your guess is too small.
   * `Too high! Try again.` if your guess is too large.
4. Continue guessing until you find the correct number.
5. The program displays a congratulatory message when you win.

## 💻 Example Output

```text
🎯 Number Guessing Game
I have chosen a number between 1 and 100.
Try to guess it!

Enter your guess: 50
Too high! Try again.

Enter your guess: 25
Too low! Try again.

Enter your guess: 38
Too low! Try again.

Enter your guess: 44
🎉 Congratulations! You guessed the correct number!
```

## 🔍 Code Explanation

### Random Number Generation

```python
number = random.randint(1, 100)
```

This generates a random integer between **1 and 100**.

### Getting User Input

```python
guess = int(input("Enter your guess: "))
```

This asks the user to enter a number and converts the input into an integer.

### Comparing the Guess

```python
if guess < number:
    print("Too low! Try again.")
elif guess > number:
    print("Too high! Try again.")
else:
    print("Congratulations! You guessed the correct number!")
```

The program compares the user's guess with the randomly generated number and provides appropriate feedback.

## ⚠️ Error Handling

The program uses `try-except` to handle invalid input.

For example:

```text
Enter your guess: hello
Invalid input. Please enter a number.
```

This prevents the program from crashing when the user enters something other than a number.

## 🎯 Learning Objectives

This project demonstrates basic Python concepts including:

* Importing modules
* Random number generation
* Variables
* User input
* `if`, `elif`, and `else`
* `while` loops
* `try-except` exception handling
* Comparison operators
* Basic game logic

## 🚀 Future Improvements

The game can be improved by adding:

* A limit on the number of attempts.
* A score system.
* Difficulty levels such as Easy, Medium, and Hard.
* Hints for the user.
* Option to play again.
* Tracking the best score.
* A graphical user interface (GUI).

## 📄 License

This project is created for **educational and learning purposes**.