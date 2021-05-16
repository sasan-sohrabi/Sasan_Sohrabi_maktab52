# Exercise 7

# Sudoku project: generate sudoku 9 * 9 table that solvable and in three level contain easy, normal and hard.
# Note: In this project, the backtracking algorithm is used for generating and solve sudoku puzzle.

# Steps to generating a sudoku puzzle is:
# 1- At first start with an empty table.
# 2- By using backtracking, generate a complete solution and fills up the table.
# 3- Remove some numbers depend on difficulty of sudoku puzzle that user chose.

# Import related libraries that we need for this project.
from random import randint


class Sudoku:
    board = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    def __init__(self, level: str):
        self.level = level

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        if value.lower() in ['easy', 'normal', 'hard']:
            self.__level = value
        else:
            raise ValueError('Input variable must be easy or normal or hard!!!')

    def solve(self, bo):
        find = self.find_empty(bo)
        if not find:
            return True
        else:
            row, col = find

        for i in range(1, 10):
            r = randint(1, 9)
            if self.valid(bo, r, (row, col)):
                bo[row][col] = r

                if self.solve(bo):
                    return True

                bo[row][col] = 0

        return False

    def valid(self, bo, num, pos):
        # Check row
        for i in range(len(bo[0])):
            if bo[pos[0]][i] == num and pos[1] != i:
                return False

        # Check column
        for i in range(len(bo)):
            if bo[i][pos[1]] == num and pos[0] != i:
                return False

        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3

        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if bo[i][j] == num and (i, j) != pos:
                    return False

        return True

    def print_board(self, bo):
        for i in range(len(bo)):
            if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")

            for j in range(len(bo[0])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                if j == 8:
                    print(bo[i][j])
                else:
                    print(str(bo[i][j]) + " ", end="")

    def find_empty(self, bo):
        for i in range(len(bo)):
            for j in range(len(bo[0])):
                if bo[i][j] == 0:
                    return (i, j)  # row, col
        return None

    def empty(self, bo):
        if self.level == "easy":
            cond_num = randint(29, 34)
        elif self.level == "normal":
            cond_num = randint(35, 47)
        else:
            cond_num = randint(47, 53)
        count_t = 0
        while True:
            if count_t == cond_num:
                break
            row = randint(0, 8)
            col = randint(0, 8)
            if bo[row][col] == 0:
                continue
            bo[row][col] = 0
            count_t += 1
        print(count_t)
        return bo

    def valid_table(self, bo):
        for i in range(len(bo)):
            for j in range(len(bo)):
                if bo[i][j] != 0 and not self.valid(bo, bo[i][j], (i, j)):
                    return False
        return True


s = Sudoku('HARD')
s.print_board(s.board)
s.solve(s.board)
print("___________________")
s.print_board(s.board)
print(s.board)
s.print_board(s.empty(s.board))
print(s.valid_table([[3, 7, 9, 2, 8, 4, 4, 1, 5], [1, 8, 2, 5, 9, 6, 4, 3, 7], [5, 4, 6, 3, 1, 7, 8, 2, 9], [8, 6, 5, 9, 4, 1, 2, 7, 3], [4, 9, 7, 8, 3, 2, 1, 5, 6], [2, 3, 1, 6, 7, 5, 9, 4, 8], [9, 1, 4, 7, 6, 3, 5, 8, 2], [7, 5, 8, 1, 2, 9, 3, 6, 4], [6, 2, 3, 4, 5, 8, 7, 9, 1]]))
# print(randint(1, 9))
