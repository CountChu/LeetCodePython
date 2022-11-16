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
    "date": "2022/11/13",
    "design": 0,
    "coding": 0,
    "runtime": "8445 ms",
    "fasterThan": "18%",
    "memory": "14 MB" 
}
'''
        0 1 2 3
      0 A B C E
      1 S F C S
      2 A D E E 

        ABCCED
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def exist(self, board: List[List[str]], word: str) -> bool:
        h = len(board)
        w = len(board[0])

        if h == 1:
            row = board[0]
            board.append(['*'] * w)
            h = 2


        if w == 1:
            for y in range(h):
                board[y].append('*')
            w = 2

        for y in range(h):
            for x in range(w):
                path = set()            # Must use set instead of list otherwise Time Limit Exceed. 
                if search(board, h, w, y, x, word, path):
                    return True

        return False

def search(board, h, w, y, x, word, path):
    c = board[y][x]
    #print('y = %d, x = %d, c = %s, word = %s' % (y, x, c, word))

    if word == '':
        return True

    if len(word) == 1:
        if word == board[y][x]:
            return True

    #new_path = set()
    #new_path += path
    #new_path.append((y, x))
    new_path = path.union(set({(y, x)}))
    #dump(new_path, board)

    if word[0] != board[y][x]:
        return False

    next_ls = get_next(h, w, y, x, new_path)
    for y1, x1 in next_ls:
        if search(board, h, w, y1, x1, word[1:], new_path):
            return True

    return False

def get_next(h, w, y, x, path):
    out = []

    y1 = y - 1
    x1 = x
    if y1 >= 0:
        if (y1, x1) not in path:
            out.append((y1, x1))

    y1 = y + 1
    x1 = x
    if y1 <= h - 1:
        if (y1, x1) not in path:
            out.append((y1, x1))

    y1 = y 
    x1 = x - 1
    if x1 >= 0:
        if (y1, x1) not in path:
            out.append((y1, x1))

    y1 = y
    x1 = x + 1 
    if x1 <= w - 1:
        if (y1, x1) not in path:
            out.append((y1, x1))

    return out

def dump(path, board):
    s = ''
    for y, x in path:
        c = board[y][x]
        s += '%s -> ' % c
    print(s)