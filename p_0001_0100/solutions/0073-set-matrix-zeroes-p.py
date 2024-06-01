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
    "date": "2022/11/12",
    "design": 0,
    "coding": 7,
    "runtime": "288 ms",
    "fasterThan": "53%",
    "memory": "14.7 MB" 
}

'''
            [[0, 1, 2, 0],
             [3, 4, 5, 2],
             [1, 3, 1, 5]]
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    """
    Do not return anything, modify matrix in-place instead.
    """
    def setZeroes(self, matrix: List[List[int]]) -> None:
        h = len(matrix)
        w = len(matrix[0])
        #print(h, w)
        
        zero_ls = []
        for y in range(h):
            for x in range(w):
                if matrix[y][x] == 0:
                    zero_ls.append((y, x))

        for y, x in zero_ls:
            fill_zero(matrix, h, w, y, x)

        pass

def fill_zero(matrix, h, w, cy, cx):
    for x in range(w):
        matrix[cy][x] = 0 

    for y in range(h):
        matrix[y][cx] = 0












