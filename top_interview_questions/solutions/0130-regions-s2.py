solution_json = {
    "date": "2023/12/20",
    "design": 0,
    "coding": 21,
    "runtime": "182 ms",
    "fasterThan": "16.19%",
    "memory": "41.16 MB"
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

def go(m, w, h, x, y, vis, ctx, pt_ls):
    v = m[y][x]
    vis.add((x, y))
    pt_ls.append((x, y))
    if x == 0:
        ctx['touched'] = True
    if x == w - 1:
        ctx['touched'] = True
    if y == 0:
        ctx['touched'] = True
    if y == h - 1:
        ctx['touched'] = True

    #lg('(%d, %d): %s' % (x, y, v))
    d_ls = [(1, 0), (0, 1), (-1, 0), (0, -1)]     # right, down, left, top
    for (dx, dy) in d_ls:
        x1 = x + dx
        if x1 == -1:
            continue
        if x1 == w:
            continue

        y1 = y + dy
        if y1 == -1:
            continue 
        if y1 == h:
            continue 

        if m[y1][x1] != 'O':
            continue 

        if (x1, y1) in vis:
            continue 

        go(m, w, h, x1, y1, vis, ctx, pt_ls)

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
        vis = set()
        ctx = {'touched': False}
        for y in range(h):
            for x in range(w):
                if not (x, y) in vis:
                    if m[y][x] == 'O':
                        #lg('----')
                        pt_ls = []
                        go(m, w, h, x, y, vis, ctx, pt_ls) 
                        #lg(ctx)
                        if ctx['touched'] == False:
                            for (x1, y1) in pt_ls:
                                m[y1][x1] = 'X'
                        ctx['touched'] = False
        pass
