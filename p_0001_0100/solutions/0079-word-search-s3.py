solution_json = {
    "date": "2024/1/1",
    "design": 0,
    "coding": 0,
    "runtime": "8011 ms",
    "fasterThan": "11%",
    "memory": "17.28 MB"
}

#
# https://leetcode.com/problems/word-search/
#
# Given an m x n grid of characters board and a string word, return true 
#if word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. The same 
# letter cell may not be used more than once.
#
 
from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    Input: 
        board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 
        word = "ABCCED"
    Output: true

           0  1  2  3

        0  A  B  C  E
        1  S  F  C  S
        2  A  D  E  E
'''

def go(m, w, h, x, y, vis, word, i, ctx):
    if ctx['found']:
        return

    if i >= len(word):
        return

    v = m[y][x]

    #lg('idx = %d' % idx)
    if v != word[i]:
        return

    if i == len(word) - 1:
        ctx['found'] = True
        return

    vis.add((x, y))

    #lg('%s(%d, %d) %s' % ('    ' * i, x, y, v))
    #lg('%s%s %s' % (' ' * i, v, vis))

    d_ls = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for (dx, dy) in d_ls:
        x1 = x + dx
        y1 = y + dy
        if x1 in range(w) and y1 in range(h):
            if not (x1, y1) in vis:
                go(m, w, h, x1, y1, vis, word, i+1, ctx)

    vis.remove((x, y))

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = board
        h = len(m)
        w = len(m[0])
        ctx = {'found': False}
        for x in range(w):
            for y in range(h):
                vis = set()
                i = 0
                go(m, w, h, x, y, vis, word, i, ctx)
                if ctx['found']:
                    return True 

        return False







