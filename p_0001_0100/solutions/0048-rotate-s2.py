solution_json = {
    "date": "2023/12/14",
    "design": 0,
    "coding": 0,
    "runtime": "47 ms",
    "fasterThan": "22%",
    "memory": "16.48 MB"
}

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
lg = print

'''
          0  1  2   3

     0    5  1  9  11
     1    2  4  8  10
     2   13  3  6   7
     3   15 14 12  16


     x  y      x  y 
    (0, 0) -> (3, 0)  (n - 1 - y, x)
    (1, 0) -> (3, 1)  (n - 1 - y, x)
    (2, 0) -> (3, 2)  (n - 1 - y, x)
    (3, 0) -> (3, 3)  (n - 1 - y, x)
    (3, 1) -> (2, 3)  (n - 1 - y, x) 
    (3, 2) -> (1, 3)  (n - 1 - y, x) 
    (3, 3) -> (0, 3)  (n - 1 - y, x)
    (2, 3) -> (0, 2)  (n - 1 - y, x)
    (1, 3) -> (0, 1)  (n - 1 - y, x)
    (0, 3) -> (0, 0)  (n - 1 - y, x)
    (0, 2) -> (1, 0)  (n - 1 - y, x)
    (0, 1) -> (2, 0)  (n - 1 - y, x)

    (1, 1) -> (2, 1)  (n - 1 - y, x)
    (2, 1) -> (2, 2)  (n - 1 - y, x)
    (2, 2) -> (1, 2)  (n - 1 - y, x)
    (1, 2) -> (1, 1)  (n - 1 - y, x)

'''

def build(m, x, y):
    v = m[y][x]
    return [(x, y), v]

def go(m, n, i):
    
    ls = []

    ls.append(build(m, 0+i, 0+i))

    for x in range(1+i, n-1-i):
        ls.append(build(m, x, 0+i))

    ls.append(build(m, n-1-i, 0+i))

    for y in range(1+i, n-1-i):
        ls.append(build(m, n-1-i, y))


    ls.append(build(m, n-1-i, n-1-i))

    for x in reversed(range(1+i, n-1-i)):
        ls.append(build(m, x, n-1-i))

    ls.append(build(m, 0+i, n-1-i))

    for y in reversed(range(1+i, n-1-i)):
        ls.append(build(m, 0+i, y))

    for (x, y), v in ls:
        x1 = n - 1 - y
        y1 = x
        #lg('(%d, %d): %2d -> (%d, %d)' % (x, y, v, x1, y1))
        m[y1][x1] = v
    

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def rotate(self, matrix: List[List[int]]) -> None:
        m = matrix
        n = len(m)

        #go(m, n, 1)
        #br()

        for i in range(n // 2):
            go(m, n, i)
