solution_json = {
    "date": "2023/12/14",
    "design": 0,
    "coding": 12,
    "runtime": "108 ms",
    "fasterThan": "24%",
    "memory": "16.26 MB"
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

def check_rows(m):
    for y in range(9):
        u = set()
        for x in range(9):
            v = m[y][x]
            if v == '.':
                continue

            #lg(v)
            if v in u:
                return False 

            u.add(v)

    return True

def check_columns(m):
    for x in range(9):
        u = set()
        for y in range(9):
            v = m[y][x]
            if v == '.':
                continue

            #lg(v)
            if v in u:
                return False 

            u.add(v)

    return True    

def check_grid(m, x0, y0):
    u = set()
    for y in range(y0, y0 + 3):
        for x in range(x0, x0 + 3):
            v = m[y][x]
            if v == '.':
                continue 

            if v in u:
                return False 

            u.add(v)
            #lg(x, y)
    
    return True

'''
    0 1 2 3 4 5
   0
   1
   2 
'''
def check_grids(m):
    for y in range(0, 9, 3):
        for x in range(0, 9, 3):
            res = check_grid(m, x, y)
            if not res:
                return False

    return True

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = board

        res = check_rows(m)
        if not res:
            return False 

        res = check_columns(m)
        if not res:
            return False 

        res = check_grids(m)
        if not res:
            return False
        
        return True
