#
# https://leetcode.com/problems/valid-sudoku/
#
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be 
# validated according to the following rules:
#
# Each row must contain the digits 1-9 without repetition.
#
# Each column must contain the digits 1-9 without repetition.
#
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 
# without repetition.
#
# Note:
#       - A Sudoku board (partially filled) could be valid but is not 
#       necessarily solvable.
#       
#       - Only the filled cells need to be validated according to the mentioned 
#       rules.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2023/11/25",
    "design": 0,
    "coding": 0,
    "runtime": "100 ms",
    "fasterThan": "67%",
    "memory": "16.39 MB" 
}

'''
     0 1 2 3 4 5 6 7 8

  0  5 3 . . 7 . . . . 
  1  6 . . 1 9 5 . . .
  2  . 9 8 . . . . 6 .


    board[y][x]

'''

def check_x_y(board, start_x, start_y):
    h = {}
    for y in range(start_y, start_y+3):
        for x in range(start_x, start_x+3):
            v = board[y][x]
            if v == '.':
                continue

            if v in h:
                return False
            else:
                h[v] = True 
    return True

def check_y(board, y):
    h = {}
    for x in range(9):
        v = board[y][x]
        if v == '.':
            continue 

        if v in h:
            return False
        else:
            h[v] = True 
    return True

def check_x(board, x):
    h = {}
    for y in range(9):
        v = board[y][x]
        if v == '.':
            continue 

        if v in h:
            return False
        else:
            h[v] = True 
    return True    

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                if not check_x_y(board, x, y):
                    return False


        for y in range(9):
            if not check_y(board, y):
                return False 

        for x in range(9):
            if not check_x(board, x):
                return False 

        return True






