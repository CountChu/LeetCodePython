solution_json = {
    "date": "2024/1/16",
    "design": 0,
    "coding": 7,
    "runtime": "106 ms",
    "fasterThan": "78%",
    "memory": "18.27 MB"
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

'''
    Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

            0  1  2  3

        0  [0, 1, 2, 0]
        1  [3, 4, 5, 2]
        2  [1, 3 ,1, 5]
'''

def collect(m, w, h):
    out = []
    for x in range(w):
        for y in range(h):
            if m[y][x] == 0:
                out.append((x, y))

    return out

def fill_col(m, h, x):
    for y in range(h):
        m[y][x] = 0

def fill_row(m, w, y):
    for x in range(w):
        m[y][x] = 0

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def setZeroes(self, matrix: List[List[int]]) -> None:
        m = matrix
        h = len(m)
        w = len(m[0])
        zero_ls = collect(m, w, h)
        #lg(zero_ls)

        vis_col = set()
        vis_row = set()
        for (x, y) in zero_ls:
            if x not in vis_col:
                fill_col(m, h, x)
                vis_col.add(x)

            if y not in vis_row:
                fill_row(m, w, y)
                vis_row.add(y)
