solution_json = {
    "date": "2023/12/28",
    "design": 0,
    "coding": 18,
    "runtime": "77 ms",
    "fasterThan": "6%",
    "memory": "17.46 MB"
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
      0   1   2   3

      5   1   9  11   0
      2   4   8  10   1  
     13   3   6   7   2
     15  14  12  16   3

            start = 0 -> range(0, 3) = range(start, n - 1 - start)
            start = 1 -> range(1, 2) 

            (x, y)
               (1, 1)
            -> (2, 1)
            -> (2, 2)
            -> (1, 2)

               (1, 0)  (x0, y0)
            -> (3, 1)  (x1, y1)   y1 = x0, x1 = n - 1 - y0 
            -> (2, 3)
            -> (0, 2)


    [[ 1,  2,  3,  4,  5],
     [ 6,  7,  8,  9, 10],
     [11, 12, 13, 14, 15],
     [16, 17, 18, 19, 20],
     [21, 22, 23, 24, 25]],

            start = 0 -> range(0, 4) = range(start, n - 1 - start)
            start = 1 -> range(1, 3)


'''

def rotate(x0, y0, n):
    x1 = n - 1 - y0
    y1 = x0
    return (x1, y1)

def go(m, n, start):
    #lg(start)
    for x in range(start, n - 1 - start):
        x0 = x
        y0 = start
        #lg('   (%d, %d): %d' % (x0, y0, m[y0][x0]))

        (x1, y1) = rotate(x0, y0, n)
        #lg('-> (%d, %d): %d' % (x1, y1, m[y1][x1]))

        (x2, y2) = rotate(x1, y1, n)
        #lg('-> (%d, %d): %d' % (x2, y2, m[y2][x2]))

        (x3, y3) = rotate(x2, y2, n)
        #lg('-> (%d, %d): %d' % (x3, y3, m[y3][x3]))

        m[y0][x0], m[y1][x1], m[y2][x2], m[y3][x3] = m[y3][x3], m[y0][x0], m[y1][x1], m[y2][x2]

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def rotate(self, matrix: List[List[int]]) -> None:
        m = matrix
        n = len(m)
        for i in range(n // 2):
            go(m, n, i)




