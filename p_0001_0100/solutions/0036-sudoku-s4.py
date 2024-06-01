solution_json = {
    "date": "2024/1/8",
    "design": 0,
    "coding": 9,
    "runtime": "99 ms",
    "fasterThan": "63%",
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

def check_row(m, y):
    set0 = set()
    for x in range(9):
        v = m[y][x]
        if v == '.':
            continue

        if v in set0:
            return False
        set0.add(v)
    return True

def check_col(m, x):
    set0 = set()
    for y in range(9):
        v = m[y][x]
        if v == '.':
            continue

        if v in set0:
            return False
        set0.add(v)
    return True

def check_cell(m, s_x, s_y):
    set0 = set()
    for x in range(3):
        for y in range(3):
            v = m[s_y+y][s_x+x]
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

        for y in range(9):
            if not check_row(m, y):
                return False

        for x in range(9):
            if not check_col(m, x):
                return False

        for y in range(0, 9, 3):
            for x in range(0, 9, 3):
                if not check_cell(m, x, y):
                    return False

        return True
