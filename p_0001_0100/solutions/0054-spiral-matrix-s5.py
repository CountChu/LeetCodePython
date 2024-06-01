solution_json = {
    "date": "2024/1/9",
    "design": 0,
    "coding": 13,
    "runtime": "34 ms",
    "fasterThan": "83%",
    "memory": "17.25 MB"
}

#
# https://leetcode.com/problems/spiral-matrix/
#
# Medium.
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    Output: [1,2,3,4,8,12,11,10,9,5,6,7]

             0   1   2   3

        0   [1,  2,  3,  4]
        1   [5,  6,  7,  8]
        2   [9, 10, 11, 12]

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = matrix
        h = len(m)
        w = len(m[0])

        idx = 0
        d_ls = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        vis = set()
        x0 = 0
        y0 = 0
        out = []
        while True: 
            if len(vis) == h * w:
                break

            vis.add((x0, y0))
            #lg('(%d, %d): %d, %d' % (x0, y0, m[y0][x0], len(vis)))     
            out.append(m[y0][x0])           

            (dx, dy) = d_ls[idx]
            x1 = x0 + dx
            y1 = y0 + dy

            if x1 not in range(w) or y1 not in range(h) or (x1, y1) in vis:
                idx = (idx + 1) % 4
                (dx, dy) = d_ls[idx]
                x0 = x0 + dx
                y0 = y0 + dy
            else:
                x0 = x1
                y0 = y1

            #br()

        return out
