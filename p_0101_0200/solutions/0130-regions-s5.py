solution_json = {
    "date": "2024/1/22",
    "design": 0,
    "coding": 12,
    "runtime": "117 ms",
    "fasterThan": "89%",
    "memory": "17.94 MB"
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

            0   1   2   3
 
        0 ["X","X","X","X"]
        1 ["X","O","O","X"]
        2 ["X","X","O","X"]
        3 ["X","O","X","X"]

'''

def go(m, w, h, x, y, level, vis):
    v = m[y][x]
    #lg('%s(%d, %d) %s' % (' '*level, x, y, v))
    vis.add((x, y))

    d_ls = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for (dx, dy) in d_ls:
        x1 = x + dx
        y1 = y + dy

        if not x1 in range(w):
            continue 

        if not y1 in range(h):
            continue

        if (x1, y1) in vis:
            continue 

        if m[y1][x1] == 'X':
            continue 

        go(m, w, h, x1, y1, level+1, vis)


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

        keep = set()
        for y in range(h):
            for x in range(w):
                if (x, y) in keep:
                    continue

                if m[y][x] == 'X':
                    continue

                is_edge = False
                
                if x == 0 or x == w - 1:
                    is_edge = True 

                if y == 0 or y == h - 1:
                    is_edge = True

                if not is_edge:
                    continue

                level = 0
                vis = set()
                go(m, w, h, x, y, level, vis)

                keep = keep.union(vis)

        for y in range(h):
            for x in range(w):
                if (x, y) in keep:
                    m[y][x] = 'O'
                else:
                    m[y][x] = 'X'




