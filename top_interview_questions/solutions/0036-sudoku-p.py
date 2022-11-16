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
    "date": "2022/11/7",
    "design": 0,
    "coding": 14,
    "runtime": "242 ms",
    "fasterThan": "30%",
    "memory": "13.9 MB" 
}

'''
    0 1 2 3 4 5 6 7 8 
    1
    2 . . _ _ _ . . .
    3
    4
    5 . . _ _ _ . . .
    6
    7
    8 . . _ _ _ . . .
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        h = 9
        w = 9

        for y in range(h):
            if not check_row(board, w, y):
                return False

        for x in range(w):
            if not check_col(board, h, x):
                return False

        for y in range(0, h, 3):
            for x in range(0, w, 3):
                #print(y, x, '------')
                if not check_box(board, y, x):
                    return False

        #br()
        return True

def check_row(board, w, y):
    num_set = set()
    for x in range(w):
        v = board[y][x]
        if v == '.':
            continue 

        if v in num_set:
            return False 

        num_set.add(v)

    return True

def check_col(board, h, x):
    num_set = set()
    for y in range(h):
        v = board[y][x]
        if v == '.':
            continue 

        if v in num_set:
            return False 

        num_set.add(v)

    return True

def check_box(board, start_y, start_x):
    num_set = set()
    for y in range(start_y, start_y+3):
        for x in range(start_x, start_x+3):
            #print(y, x)
            v = board[y][x]
            if v == '.':
                continue 

            if v in num_set:
                return False

            num_set.add(v)

    return True





