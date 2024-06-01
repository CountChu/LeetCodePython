solution_json = {
    "date": "2023/12/31",
    "design": 0,
    "coding": 13,
    "runtime": "104 ms",
    "fasterThan": "87%",
    "memory": "18.41 MB"
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

       0 1 2 3 

    0  0 1 2 0
    1  3 4 5 2
    2  1 3 1 5

'''

def fill_zero(m, w, h, s_x, s_y, vis_rows, vis_cols):
    if not s_x in vis_cols:
        for y in range(h):
            m[y][s_x] = 0
        vis_cols.add(s_x)

    if not s_y in vis_rows:
        for x in range(w):
            m[s_y][x] = 0
        vis_rows.add(s_y)

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

        vis_rows = set()
        vis_cols = set()
        for (x, y) in zero_ls:
            fill_zero(m, w, h, x, y, vis_rows, vis_cols)










