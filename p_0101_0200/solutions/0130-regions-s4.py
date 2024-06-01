solution_json = {
    "date": "2024/1/12",
    "design": 0,
    "coding": 19,
    "runtime": "1416 ms",
    "fasterThan": "5%",
    "memory": "40.1 MB"
}

#
# https://leetcode.com/problems/surrounded-regions/
#
# Medium.
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
#lg = print

'''
    Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

            0 1 2 3

        0   X X X X
        1   X O O X
        2   X X O X
        3   X O X X

'''

def go(m, w, h, x0, y0, vis, ctx, level):
    #lg('%s(%d, %d)' % ('    '*level, x0, y0))

    if x0 == 0 or x0 == w - 1:
        ctx['touched'] = True

    if y0 == 0 or y0 == h - 1:
        ctx['touched'] = True

    vis.add((x0, y0))

    d_ls = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    
    for (dx, dy) in d_ls:
        x1 = x0 + dx
        y1 = y0 + dy

        if not x1 in range(w):
            continue 

        if not y1 in range(h):
            continue 

        if m[y1][x1] == 'X':
            continue

        if (x1, y1) in vis:
            continue

        go(m, w, h, x1, y1, vis, ctx, level+1)


def fill(m, vis):
    for x, y in vis:
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
        for y in range(h):
            for x in range(w):
                if m[y][x] == 'O':
                    ctx = {'touched': False}
                    level = 0
                    vis = set()
                    go(m, w, h, x, y, vis, ctx, level)
                    if not ctx['touched']:
                        fill(m, vis)

        pass


