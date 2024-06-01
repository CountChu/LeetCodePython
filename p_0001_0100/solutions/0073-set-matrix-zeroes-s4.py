solution_json = {
    "date": "2024/1/10",
    "design": 0,
    "coding": 8,
    "runtime": "108 ms",
    "fasterThan": "79%",
    "memory": "18.34 MB"
}

#
# https://leetcode.com/problems/set-matrix-zeroes/
#
# Medium.
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

def find_zeros(m, w, h):
    out = []
    for y in range(h):
        for x in range(w):
            if m[y][x] == 0:
                out.append((x, y))
    return out

def fill_col(m, h, x0):
    for y in range(h):
        m[y][x0] = 0

def fill_row(m, w, y0):
    for x in range(w):
        m[y0][x] = 0

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
        zero_ls = find_zeros(m, w, h)
        #lg(zero_ls)

        vis_x = set()
        vis_y = set()
        for (x, y) in zero_ls:
            if not x in vis_x:
                vis_x.add(x)
                fill_col(m, h, x)

            if not y in vis_y:
                vis_y.add(y)
                fill_row(m, w, y)








