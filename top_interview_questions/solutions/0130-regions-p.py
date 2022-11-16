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

solution_json = {
    "date": "2022/11/15",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

'''
         0 1 2 3
      
      0  X X X X
      1  X O O X
      2  X X O X
      3  X O X X
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    """
    Do not return anything, modify board in-place instead.
    """
    def solve(self, board: List[List[str]]) -> None:
        h = len(board)
        w = len(board[0])        
        r_ls = find_regions(board, h, w)
        fill_regions(board, h, w, r_ls)

def find_regions(board, h, w):
    seen = set()

    out = []
    for y in range(h):
        for x in range(w):
            if board[y][x] == 'O':
                if (y, x) not in seen:
                    r = get_region(board, h, w, y, x, seen)
                    out.append(r)
                    #print(r)
    
    return out

def get_region(board, h, w, y, x, seen):
    q = [(y, x)]
    out = []
    while True:
        if q == []:
            break

        y, x = q.pop(0)
        seen.add((y, x))        
        
        out.append((y, x))
        next_ls = get_next_ls(board, h, w, y, x, seen)
        #print(next_ls)
        for nx in next_ls:
            q += next_ls
        #print(seen)
        #print(out)

    return out

def get_next_ls(board, h, w, y, x, seen):
    y0 = y - 1
    y2 = y + 1
    x0 = x - 1
    x2 = x + 1

    out = []

    if y0 >= 0:                         # top
        if board[y0][x] == 'O':
            if (y0, x) not in seen:
                out.append((y0, x))

    if y2 <= h - 1:                     # down
        if board[y2][x] == 'O':
            if (y2, x) not in seen:
                out.append((y2, x))

    if x0 >= 0:                         # left
        if board[y][x0] == 'O':
            if (y, x0) not in seen:
                out.append((y, x0))

    if x2 <= w - 1:                     # right
        if board[y][x2] == 'O':
            if (y, x2) not in seen:
                out.append((y, x2))

    return out

def fill_regions(board, h, w, r_ls):
    for r in r_ls:
        if is_surrounded(board, h, w, r):
            fill_region(board, r)

def is_surrounded(board, h, w, r):
    out = True
    for y, x in r:
        
        if y == 0:
            out = False
        elif y == h - 1:
            out = False

        if x == 0:
            out = False
        elif x == w - 1:
            out = False

    #br()        
    return out

def fill_region(board, r):
    for y, x in r:
        board[y][x] = 'X'









