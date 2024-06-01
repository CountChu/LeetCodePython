solution_json = {
    "date": "2024/1/3",
    "design": 0,
    "coding": 0,
    "runtime": "1481 ms",
    "fasterThan": "5%",
    "memory": "38.19 MB"
}

#
# https://leetcode.com/problems/surrounded-regions/
#
# Given an m x n matrix board containing 'X' and 'O', capture all regions 
# that are 4-directionally surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region. 
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
        0 1 2 3

    0   X X X X
    1   X O O X
    2   X X O X
    3   X O X X
'''

def go(m, w, h, x, y, vis, ctx):
    if x == 0 or x == w - 1:
        ctx['touched'] = True

    if y == 0 or y == h - 1:
        ctx['touched'] = True

    vis.add((x, y))
    #lg('(%d, %d) %s' % (x, y, vis))

    d_ls = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for (dx, dy) in d_ls:
        x1 = x + dx
        y1 = y + dy
        if x1 in range(0, w) and y1 in range(0, h):
            if m[y1][x1] == 'X':
                continue

            if (x1, y1) in vis:
                continue
                
            go(m, w, h, x1, y1, vis, ctx)

def fill(m, vis):
    for (x, y) in vis:
        m[y][x] = 'X'

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    """
    Do not return anything, modify board in-place instead.
    """
    def solve(self, board: List[List[str]]) -> None:
        m = board
        h = len(m)
        w = len(m[0])

        for x in range(w):
            for y in range(h):
                if m[y][x] == 'X':
                    continue

                vis = set()
                ctx = {'touched': False}
                go(m, w, h, x, y, vis, ctx)
                if not ctx['touched']:
                    fill(m, vis)

