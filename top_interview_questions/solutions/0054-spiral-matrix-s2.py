solution_json = {
    "date": "2023/12/15",
    "design": 0,
    "coding": 9,
    "runtime": "46 ms",
    "fasterThan": "9%",
    "memory": "16.44 MB"
}

#
# https://leetcode.com/problems/spiral-matrix/
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
       0  1  2  3

    0  1  2  3  4
    1  5  6  7  8
    2  9 10 11 12
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = matrix
        h = len(m)
        w = len(m[0])

        count = 0
        x = 0
        y = 0
        s = 'r'                         # r, d, l, t
        vis = set()
        out = []
        while True:
            if count == h * w:
                break

            v = m[y][x]
            #lg('(%d, %d), %d' % (x, y, v))
            out.append(v)
            vis.add((x, y))
            count += 1

            if s == 'r':
                if x == w - 1 or (x + 1, y) in vis:
                    s = 'd'
            elif s == 'd':
                if y == h - 1 or (x, y + 1) in vis:
                    s = 'l'
            elif s == 'l':
                if x == 0 or (x - 1, y) in vis:
                    s = 't'
            elif s == 't':
                if y == 0 or (x, y - 1) in vis:
                    s ='r'
            else:
                assert False

            if s == 'r':
                x += 1
            elif s == 'd':
                y += 1
            elif s == 'l':
                x -= 1
            elif s == 't':
                y -= 1
            else:
                assert False

        return out


