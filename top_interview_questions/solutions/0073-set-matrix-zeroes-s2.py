solution_json = {
    "date": "2023/12/16",
    "design": 0,
    "coding": 8,
    "runtime": "115 ms",
    "fasterThan": "68%",
    "memory": "17.26 MB"
}

#
# https://leetcode.com/problems/set-matrix-zeroes/
#
# Given an m x n integer matrix matrix, if an element is 0, set its entire 
# row and column to 0's.
#
# You must do it in place.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
         0 1 2 3 x

     0   0 1 2 0
     1   3 4 5 2
     2   1 3 1 5
     y
'''

def fill_row(m, w, y):
    for x in range(w):
        m[y][x] = 0

def fill_col(m, h, x):
    for y in range(h):
        m[y][x] = 0

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    """
    Do not return anything, modify matrix in-place instead.
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = matrix
        h = len(m)
        w = len(m[0])

        zero_ls = []
        for y in range(h):
            for x in range(w):
                if m[y][x] == 0:
                    zero_ls.append((x, y))

        rows = set()
        cols = set()
        for (x, y) in zero_ls:
            if y not in rows:
                fill_row(m, w, y)
                rows.add(y)

            if x not in cols:
                fill_col(m, h, x)
                cols.add(x)

        pass









