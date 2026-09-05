# 🧮 Simple Python Calculator

A simple command-line calculator written in **Python** that performs basic arithmetic operations: addition, subtraction, multiplication, and division.

## 📌 Features

* Addition of two numbers
* Subtraction of two numbers
* Multiplication of two numbers
* Division of two numbers
* Handles division by zero
* Handles invalid number inputs
* Allows the user to quit the calculator using `q`
* Uses separate functions for each arithmetic operation

## 🛠️ Technologies Used

* **Python 3**
* Command Line / Terminal

## 📂 Project Structure

```text
calculator/
│
├── calculator.py
└── README.md
```

## ▶️ How to Run

### 1. Install Python

Make sure Python 3 is installed on your computer.

Check the Python version using:

```bash
python --version
```

### 2. Run the Program

Open the terminal in the project directory and execute:

```bash
python calculator.py
```

## 💻 How to Use

After running the program, you will see:

```text
Select Operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
```

Enter a choice from `1` to `4`.

Then enter the two numbers when prompted.

### Example

```text
Enter choice (1/2/3/4) or 'q' to quit: 1
Enter first number: 10
Enter second number: 5
Result: 10.0 + 5.0 = 15.0
```

### Division Example

```text
Enter choice (1/2/3/4) or 'q' to quit: 4
Enter first number: 10
Enter second number: 2
Result: 10.0 / 2.0 = 5.0
```

### Division by Zero

The program safely handles division by zero:

```text
Enter choice (1/2/3/4) or 'q' to quit: 4
Enter first number: 10
Enter second number: 0
Result: 10.0 / 0.0 = Error! Division by zero.
```

### Quit the Program

Enter `q` to exit:

```text
Enter choice (1/2/3/4) or 'q' to quit: q
Goodbye!
```

## 🔍 Functions Used

| Function         | Description                                       |
| ---------------- | ------------------------------------------------- |
| `add(x, y)`      | Adds two numbers                                  |
| `subtract(x, y)` | Subtracts the second number from the first        |
| `multiply(x, y)` | Multiplies two numbers                            |
| `divide(x, y)`   | Divides the first number by the second            |
| `calculator()`   | Controls the calculator menu and user interaction |

## ⚠️ Error Handling

The program handles two common errors:

1. **Invalid number input**
   If the user enters text instead of a number, the program displays:

   ```text
   Invalid input. Please enter numbers only.
   ```

2. **Division by zero**
   If the second number is `0` during division, the program displays:

   ```text
   Error! Division by zero.
   ```

## 🎯 Purpose

This project is designed to demonstrate basic Python programming concepts such as:

* Functions
* Conditional statements
* `while` loops
* User input
* Exception handling using `try-except`
* Arithmetic operators
* Formatted strings
* Function calling

## 🚀 Future Improvements

The calculator can be extended by adding:

* Modulus (`%`)
* Power (`**`)
* Square root
* Percentage calculation
* A graphical user interface (GUI)
* Calculation history
* More advanced mathematical operations

## 📄 License

This project is created for **educational and learning purposes**.
