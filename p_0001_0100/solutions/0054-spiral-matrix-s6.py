solution_json = {
    "date": "2024/1/15",
    "design": 0,
    "coding": 15,
    "runtime": "38 ms",
    "fasterThan": "59%",
    "memory": "17.36 MB"
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

        0  [ 1,  2,  3,  4]
        1  [ 5,  6,  7,  8]
        2  [ 9, 10, 11, 12]

    

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = matrix
        h = len(m)
        w = len(m[0])
        x0 = 0
        y0 = 0
        vis = set()
        d_ls = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        idx = 0
        out = []
        while True:
            #lg(m[y0][x0], vis)

            if not (x0, y0) in vis:
                out.append(m[y0][x0])
                vis.add((x0, y0))

            if len(vis) == h * w:
                break            

            (dx, dy) = d_ls[idx]
            x1 = x0 + dx
            y1 = y0 + dy

            if not x1 in range(w):
                idx = (idx + 1) % 4
                continue

            if not y1 in range(h):
                idx = (idx + 1) % 4
                continue

            if (x1, y1) in vis:
                idx = (idx + 1) % 4
                continue

            x0 = x1
            y0 = y1

        return out
