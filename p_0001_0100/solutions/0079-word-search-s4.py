solution_json = {
    "date": "2024/1/11",
    "design": 0,
    "coding": 12,
    "runtime": "6869 ms",
    "fasterThan": "24%",
    "memory": "17.38 MB"
}

#
# https://leetcode.com/problems/word-search/
#
# Medium.
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
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true

              0    1    2    3

        0   ["A", "B", "C", "E"],
        1   ["S", "F", "C", "S"],
        2   ["A", "D", "E", "E"]
'''

def go(m, w, h, x, y, level, path, idx, word, ctx):
    #lg('%s%s' % (' '*level, m[y][x]))

    if ctx['out']:
        return

    if m[y][x] != word[idx]:
        #lg('%sSkip it.' % (' '*level))
        return

    else:
        if idx == len(word) - 1:
            #lg('%sFinished it.' % (' '*level))
            ctx['out'] = True
            return

    path.add((x, y))

    d_ls = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for (dx, dy) in d_ls:
        x1 = x + dx
        y1 = y + dy
        if (x1, y1) in path:
            continue

        if not x1 in range(w):
            continue

        if not y1 in range(h):
            continue

        go(m, w, h, x1, y1, level+1, path, idx+1, word, ctx)

    path.remove((x, y))


class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = board
        h = len(m)
        w = len(m[0])
        ctx = {'out': False}    

        for y in range(h):
            for x in range(w):
                level = 0
                path = set()
                idx = 0
                go(m, w, h, x, y, level, path, idx, word, ctx)
                if ctx['out']:
                    return True

        return False







