solution_json = {
    "date": "2023/12/17",
    "design": 0,
    "coding": 21,
    "runtime": "7690 ms",
    "fasterThan": "13%",
    "memory": "16.31 MB"
}

#
# https://leetcode.com/problems/word-search/
#
# Given an m x n grid of characters board and a string word, return true 
# if word exists in the grid.
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
         0 1 2 3

     0   A B C E
     1   S F C S
     2   A D E E   

     ABCCED

'''
def go(m, w, h, x, y, i, ctx, vis):
    if ctx['matched']:
        return

    if i >= len(ctx['word']):
        return

    ctx['count'] += 1
    #if ctx['count'] == 10:
    #    br()

    v = m[y][x]
    #lg('%d (%d, %d) %s' % (i, x, y, v))

    if v != ctx['word'][i]:
        return

    if i == len(ctx['word']) - 1:
        ctx['matched'] = True
        return

    vis.add((x, y))

    d_ls = [(1, 0), (0, 1), (-1, 0), (0, -1)] # left, down, right, up
    for dx, dy in d_ls:
        x1 = x + dx
        if x1 == -1 or x1 == w:
            continue 

        y1 = y + dy
        if y1 == -1 or y1 == h:
            continue

        if (x1, y1) in vis:
            continue

        go(m, w, h, x1, y1, i+1, ctx, vis)

    vis.remove((x, y))

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = board
        h = len(m)
        w = len(m[0])
        ctx = {
            'count': 0,
            'word': word,
            'matched': False    
        }

        for y in range(h):
            for x in range(w):
                vis = set()
                i = 0
                go(m, w, h, x, y, i, ctx, vis)
                if ctx['matched']:
                    return True

        return False







