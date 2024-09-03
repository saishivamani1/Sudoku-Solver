import tkinter as tk
from tkinter import messagebox

# Function to check if placing num in grid[row][col] is valid
def is_valid(grid, row, col, num):
    for i in range(9):
        if grid[row][i] == num or grid[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True

# Function to check if the entire grid is valid
def is_grid_valid(grid):
    for row in range(9):
        for col in range(9):
            num = grid[row][col]
            if num != 0:
                grid[row][col] = 0
                if not is_valid(grid, row, col, num):
                    grid[row][col] = num
                    return False
                grid[row][col] = num
    return True

# Backtracking solver function
def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        if solve_sudoku(grid):
                            return True
                        grid[row][col] = 0
                return False
    return True

# Function to fetch and solve the Sudoku puzzle from the GUI
def solve():
    grid = []
    initial_grid = []
    for i in range(9):
        row = []
        initial_row = []
        for j in range(9):
            value = entries[i][j].get()
            if value == '':
                row.append(0)
                initial_row.append(0)
            else:
                row.append(int(value))
                initial_row.append(int(value))
        grid.append(row)
        initial_grid.append(initial_row)
    
    if not is_grid_valid(grid):
        messagebox.showinfo("Sudoku Solver", "The Sudoku puzzle is not valid.")
        return
    
    if solve_sudoku(grid):
        for i in range(9):
            for j in range(9):
                entries[i][j].delete(0, tk.END)
                entries[i][j].insert(0, str(grid[i][j]))
                if initial_grid[i][j] == 0:
                    entries[i][j].config(fg='green')
                else:
                    entries[i][j].config(fg='red')
    else:
        messagebox.showinfo("Sudoku Solver", "No solution exists.")

# Function to clear the Sudoku board
def clear():
    for i in range(9):
        for j in range(9):
            entries[i][j].delete(0, tk.END)
            entries[i][j].config(fg='black')

# Setting up the main window
root = tk.Tk()
root.title("Sudoku Solver")

# Adding the heading "Sudoku Solver" above the grid
heading = tk.Label(root, text="Sudoku Solver", font=('Arial', 24, 'bold'), fg='black')
heading.grid(row=0, column=0, columnspan=9, pady=10)

# Create a 9x9 grid of entries
entries = [[tk.Entry(root, width=5, font=('Arial', 18), justify='center') for j in range(9)] for i in range(9)]
for i in range(9):
    for j in range(9):
        entries[i][j].grid(row=i+1, column=j, padx=5, pady=5)

# Buttons to solve and clear the Sudoku
button_frame = tk.Frame(root)
button_frame.grid(row=10, column=0, columnspan=9, pady=20)

solve_button = tk.Button(button_frame, text="Solve", command=solve, font=('Arial', 18), padx=20, pady=10)
solve_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear", command=clear, font=('Arial', 18), padx=20, pady=10)
clear_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
