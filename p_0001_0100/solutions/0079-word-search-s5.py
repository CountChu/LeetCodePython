solution_json = {
    "date": "2024/1/17",
    "design": 0,
    "coding": 16,
    "runtime": "8014 ms",
    "fasterThan": "10%",
    "memory": "17.32 MB"
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
#lg = print

'''
    Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
    Output: true

             0    1    2    3

        0  ["A", "B", "C", "E"]    ABCCED
        1  ["S", "F", "C", "S"] 
        2  ["A", "D", "E", "E"]    
'''

def go(m, w, h, x, y, path, level, word, ctx):
    if ctx['found']:
        return

    if level == len(word):
        ctx['found'] = True
        return

    v = m[y][x]
    #lg('%s%s, %d' % (' '*level, v, level))

    if v != word[level]:
        return
    else:
        if level == len(word) - 1:
            ctx['found'] = True
            return

    path.add((x, y))

    d_ls = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for (dx, dy) in d_ls:
        x1 = x + dx
        y1 = y + dy

        if not x1 in range(w):
            continue

        if not y1 in range(h):
            continue

        if (x1, y1) in path:
            continue 

        go(m, w, h, x1, y1, path, level+1, word, ctx)

    path.remove((x, y))


class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = board
        h = len(m)
        w = len(m[0])
        for y in range(h):
            for x in range(w):
                path = set()
                level = 0
                ctx = {'found': False}
                go(m, w, h, x, y, path, level, word, ctx)
                if ctx['found']:
                    return True

        return False







