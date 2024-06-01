solution_json = {
    "date": "2023/12/29",
    "design": 0,
    "coding": 26,
    "runtime": "75 ms",
    "fasterThan": "5%",
    "memory": "17.44 MB"
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
#lg = print

'''
    r -> d -> l -> u
    (1, 0) -> (0, 1) -> (-1. 0) -> (0, -1)

        -1  0   1   2   3   4
    -1      x
    0       1   2   3   4   x
    1       5   6   7   8   
    2    x  9  10  11  12   
    3                   x   

    bounds = (0, -1), (4, 0), (3, 3), (-1, 2)
'''

def move(p, d):
    return (p[0]+d[0], p[1]+d[1])

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = matrix
        h = len(m)
        w = len(m[0])
        d_ls = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        bounds = [(0, -1), (w, 0), (w-1, h), (-1, h-1)]
        #lg(bounds)
        vis = set(bounds)
        x = 0
        y = 0
        d_idx = 0
        count = 0
        out = []
        while True:
            if count == w * h:
                break

            vis.add((x, y))
            v = m[y][x]
            out.append(v)
            #lg(v)
            count += 1

            d = d_ls[d_idx]
            (x1, y1) = move((x, y), d)
            if (x1, y1) in vis:
                d_idx += 1
                d_idx %= 4
                d = d_ls[d_idx]
                (x1, y1) = move((x, y), d)

            (x, y) = (x1, y1)

        return out


