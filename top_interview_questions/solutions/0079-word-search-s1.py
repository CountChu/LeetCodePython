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

solution_json = {
    "date": "2023/11/30",
    "design": 0,
    "coding": 0,
    "runtime": "4945 ms",
    "fasterThan": "77%",
    "memory": "16.2 MB"
}

'''
        0 1 2 3 x

    0   A B C E
    1   S F C S
    2   A D E E
    y

    h = 3, w = 4
    word = 'ABCCED'

'''

def go(m, h, w, y, x, visited, word, i, ctx):
    if ctx['matched']:
        return

    if i == len(word):
        ctx['matched'] = True
        return

    if m[y][x] != word[i]:
        return

    visited.add((x, y))
    #print(x, y, m[y][x], len(visited), i)
    if i + 1 == len(word):
        ctx['matched'] = True
        return

    if x <= w - 2:                      # go right
        if (x+1, y) not in visited:
            go(m, h, w, y, x+1, visited, word, i+1, ctx)
    
    if y <= h - 2:                      # go down
        if (x, y+1) not in visited:      
            go(m, h, w, y+1, x, visited, word, i+1, ctx)

    if x >= 1:                          # go left
        if (x-1, y) not in visited:
            go(m, h, w, y, x-1, visited, word, i+1, ctx)        

    if y >= 1:                          # go up
        if (x, y-1) not in visited:     
            go(m, h, w, y-1, x, visited, word, i+1, ctx)       

    visited.remove((x, y))    

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def exist(self, board: List[List[str]], word: str) -> bool:

        m = board
        h = len(m)
        w = len(m[0])

        for y in range(h):
            for x in range(w):
                visited = set()
                i = 0
                ctx = {}
                ctx['matched'] = False
                go(m, h, w, y, x, visited, word, i, ctx)
                if ctx['matched']:
                    return True 

        return False





