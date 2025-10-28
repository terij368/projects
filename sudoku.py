import time
import sys

def appearing(row, col, number):
    # Check if the number is appearing in the given row?
    for i in range(9):
        if board[row][i] == number:
            return False

    # Check if the number is appearing in the given column?
    for i in range(9):
        if board[i][col] == number:
            return False

    # Check if the number is appearing in the given square?
    x = (col // 3) * 3
    y = (row // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[y+i][x+j] == number:
                return False

    return True

def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for number in range(1, 10):
                    if appearing(row, col, number):
                        board[row][col] = number
                        if solve(board): 
                            return True
                        board[row][col] = 0

                return False
    return True


def read_sudoku_from_file(path):
    with open(path) as sudoku_file:
        file = sudoku_file.readlines()
        sudoku = []
        for line in file:
            sudoku_line = []
            for j in line:
                if j == "_":
                    sudoku_line.append(0)
                elif j == " " or j == "\n" :
                    pass
                else:
                    sudoku_line.append(int(j))
            sudoku.append(sudoku_line)
    return sudoku

def write_output(solution):
    for i in solution:
        for j in i:
            print(j, end = " ")
        print()

start_time = time.time()
board = read_sudoku_from_file(sys.argv[1])
if solve(board):
    elapsed_time =  (time.time() - start_time) * 1000
    print(f"Solution found in {elapsed_time:.3f}ms")
    write_output(board)

else:
    print("No solution exists")
