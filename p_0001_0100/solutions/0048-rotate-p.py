#
# https://leetcode.com/problems/rotate-image/
#
# You are given an n x n 2D matrix representing an image, rotate the image 
# by 90 degrees (clockwise).
# 
# You have to rotate the image in-place, which means you have to modify 
# the input 2D matrix directly. DO NOT allocate another 2D matrix 
# and do the rotation.
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/9",
    "design": 0,
    "coding": 20,
    "runtime": "57 ms",
    "fasterThan": "72%",
    "memory": "14 MB" 
}

''' 
         0  1  2
      0  1  2  3
      1  4  5  6
      2  7  8  9

          0   1   2   3
      0   5   1   9  11 
      1   2   4   8  10
      2  13   3   6   7
      3  15  14  12  16
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        h = {}                          # h[(y, x)] = v
        for y0 in range(n):
            for x0 in range(n):
                v0 = matrix[y0][x0]
                y1 = x0
                x1 = n - y0 - 1
                #print('(%d, %d) -> (%d, %d)' % (y0, x0, y1, x1))
                h[(y1, x1)] = v0
        
        for (y, x), v in h.items():
            #print(y, x, v) 
            matrix[y][x] = v
        
        return matrix



