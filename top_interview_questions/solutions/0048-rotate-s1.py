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
    "date": "2023/11/26",
    "design": 0,
    "coding": 0,
    "runtime": "42 ms",
    "fasterThan": "55%",
    "memory": "16.34 MB" 
}

'''

       0 1 2        0 1 2 

    0  1 2 3     0  7 4 1
    1  4 5 6     1  8 5 2
    2  7 8 9     2  9 6 3

      y  x       y  x
    m[0][0] -> m[0][2]
    m[0][1] -> m[1][2]
    m[0][2] -> m[2][2]
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def rotate(self, matrix: List[List[int]]) -> None:
        m = matrix
        n = len(m)
        h = {}
        for y in range(n):
            for x in range(n):
                y1 = x 
                x1 = n - y - 1
                #print(y1, x1)
                h[(y1, x1)] = m[y][x]
        
        for y in range(n):
            for x in range(n):
                m[y][x] = h[(y, x)]
