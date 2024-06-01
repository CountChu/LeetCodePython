solution_json = {
    "date": "2023/12/27",
    "design": 0,
    "coding": 13,
    "runtime": "92 ms",
    "fasterThan": "91%",
    "memory": "17.48 MB"
}

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
lg = print

def check_column(m, x):
    v_set = set()
    for y in range(9):
        v = m[y][x]
        if v == '.':
            continue

        if v in v_set:
            return False

        v_set.add(v)
    
    return True

def check_row(m, y):
    v_set = set()
    for x in range(9):
        v = m[y][x]
        if v == '.':
            continue

        if v in v_set:
            return False

        v_set.add(v)
    
    return True

def check_box(m, start_x, start_y):
    v_set = set()
    for x in range(start_x, start_x + 3):
        for y in range(start_y, start_y + 3):
            v = m[y][x]
            if v == '.':
                continue

            if v in v_set:
                return False 

            v_set.add(v)

    return True

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = board

        for x in range(9):
            if not check_column(m, x):
                return False

        for y in range(9):
            if not check_row(m, y):
                return False

        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                if not check_box(m, x, y):
                    return False

        return True
