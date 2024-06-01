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

solution_json = {
    "date": "2023/11/29",
    "design": 0,
    "coding": 0,
    "runtime": "121 ms",
    "fasterThan": "33%",
    "memory": "17.26 MB" 
}

def fill_y(m, h, w, y):
    for x in range(w):
        m[y][x] = 0

def fill_x(m, h, w, x):
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

        set_y = set()
        set_x = set()
        for (x, y) in zero_ls:
            if m[y][x] == 0:
                if y not in set_y:
                    fill_y(m, h, w, y)
                    set_y.add(y)
                if x not in set_x:
                    set_x.add(x)
                    fill_x(m, h, w, x)










