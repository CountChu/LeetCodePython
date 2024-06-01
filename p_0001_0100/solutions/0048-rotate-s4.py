solution_json = {
    "date": "2024/1/9",
    "design": 0,
    "coding": 18,
    "runtime": "44 ms",
    "fasterThan": "45%",
    "memory": "17.23 MB"
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
#lg = print

'''
    Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

             0   1   2   3

        0  [ 5,  1,  9, 11]
        1  [ 2,  4,  8, 10]
        2  [13,  3,  6,  7]
        3  [15, 14, 12, 16]

        n = 4
        (0, 0), (1, 1)

        (0, 0): 3, n - 1
        (1, 1): 1, n - 3

             x  y
            (1, 0) (x0, y0)
        ->  (3, 1) (x1, y1)  y1 = x0, x1 = n - 1 - y0 
        ->  (2, 3)
        ->  (0, 2)

             x  y
            (1, 1)
        ->  (2, 1) 
        ->  (2, 2)
        ->  (1, 2)

'''

def rotate(n, x0, y0):
    y1 = x0
    x1 = n - 1 - y0
    return (x1, y1)


def go(m, n, x, y):
    x0 = x
    y0 = y
    #lg('(%d, %d) -> ' % (x0, y0), end='')

    (x1, y1) = rotate(n, x0, y0)
    #lg('(%d, %d) -> ' % (x1, y1), end='')    
    
    (x2, y2) = rotate(n, x1, y1)
    #lg('(%d, %d) -> ' % (x2, y2), end='')    
    
    (x3, y3) = rotate(n, x2, y2)
    #lg('(%d, %d)' % (x3, y3))

    m[y0][x0], m[y1][x1], m[y2][x2], m[y3][x3] = m[y3][x3], m[y0][x0], m[y1][x1], m[y2][x2]

def move(m, n, start, size):
    x0 = start
    y0 = start
    #lg(x0, y0)
    for x in range(start, start + size):
        #lg('x = %d' % x)
        go(m, n, x, y0)

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def rotate(self, matrix: List[List[int]]) -> None:
        m = matrix
        n = len(m)
        size = n - 1
        for i in range(n // 2):
            move(m, n, i, size)
            size -= 2
        