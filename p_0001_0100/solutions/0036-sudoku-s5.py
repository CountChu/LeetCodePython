solution_json = {
    "date": "2024/1/14",
    "design": 0,
    "coding": 8,
    "runtime": "91 ms",
    "fasterThan": "85%",
    "memory": "17.3 MB"
}

#
# https://leetcode.com/problems/valid-sudoku/
#
# Medium.
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
lg = print

def check_cell(m, x0, y0):
    set0 = set()

    for x in range(x0, x0 + 3):
        for y in range(y0, y0 + 3):
            v = m[y][x]
            if v == '.':
                continue 
            
            if v in set0:
                return False

            set0.add(v) 

    return True

def check_col(m, h, x0):
    set0 = set()

    for y in range(9):
        v = m[y][x0]
        if v == '.':
            continue 
        
        if v in set0:
            return False

        set0.add(v) 

    return True

def check_row(m, w, y0):
    set0 = set()

    for x in range(9):
        v = m[y0][x]
        if v == '.':
            continue 
        
        if v in set0:
            return False

        set0.add(v) 

    return True    

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = board
        h = len(m)
        w = len(m[0])

        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                if not check_cell(m, x, y):
                    return False

        for x in range(w):
            if not check_col(m, h, x):
                return False

        for y in range(h):
            if not check_row(m, w, y):
                return False

        return True

