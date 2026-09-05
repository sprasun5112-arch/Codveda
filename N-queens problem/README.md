# N-Queens Problem Solver

A Python program that solves the classic **N-Queens Problem** using a backtracking algorithm.

This project was completed as part of my **Codveda Technologies Python Development Internship – Level 3 (Advanced), Task 3**.

## 📌 Task Description

The N-Queens problem is a classic algorithmic problem where the goal is to place `N` queens on an `N × N` chessboard such that no two queens can attack each other.

The queens must not share the same:

- Row
- Column
- Diagonal

## 🎯 Objectives

- Represent the chessboard as a 2D array.
- Use backtracking to place queens safely.
- Ensure that no two queens occupy the same row, column, or diagonal.
- Display a valid solution on the console.

## 🛠️ Technologies Used

- **Python 3**
- Backtracking Algorithm
- 2D Lists / Arrays

## ⚙️ How It Works

1. The user enters the value of `N`.
2. The program creates an `N × N` chessboard.
3. It attempts to place one queen in each row.
4. Before placing a queen, the program checks whether the position is safe.
5. If a position is unsafe, the program tries another position.
6. If no valid position is available, the algorithm backtracks to the previous row.
7. Once all queens are placed successfully, the solution is displayed.

## ▶️ How to Run

Open the project folder in a terminal and run:

```bash
python n_queens.py


Example:
==========================================
        N-QUEENS PROBLEM SOLVER
==========================================

Enter the value of N: 4

Solution for 4-Queens:

. Q . .
. . . Q
Q . . .
. . Q .


🧠 Algorithm
The program uses backtracking.
For every row, the algorithm tries each column and checks whether placing a queen there is safe.
If a valid position is found, the queen is placed and the algorithm moves to the next row.
If the algorithm reaches a situation where no safe position exists, it removes the previously placed queen and tries another position.
📸 Output
The program successfully generated a solution for N = 4.
The output represents the chessboard using:
- Q → Queen
- . → Empty position


📂 Project Structure:
N-Queens/
│
├── n_queens.py
├── README.md
└── screenshots/
    └── n_queens_output.png

✅ Result
The N-Queens Solver successfully finds a valid arrangement of queens using the backtracking technique.
For N = 4, the program successfully produced a valid solution where no two queens attack each other.

👨‍💻 Internship
Organization: Codveda Technologies
Role: Python Development Intern
Level: Level 3 – Advanced
Task: Task 3 – N-Queens Problem