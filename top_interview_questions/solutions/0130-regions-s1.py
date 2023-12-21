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
    "date": "2023/12/5",
    "design": 0,
    "coding": 0,
    "runtime": "244 ms",
    "fasterThan": "5.73%",
    "memory": "111.5 MB" 
}

def go(m, h, w, q, visited, region, idx):
    if len(q) == 0:
        return

    (x, y) = q.pop()
    #print(x, y)
    visited.add((x, y))
    region[idx].append((x, y))

    # move right
    if x <= w - 2:
        x1 = x + 1
        if m[y][x1] == 'O' and (x1, y) not in visited:
            q.append((x1, y))

    # move left
    if x >= 1:
        x1 = x - 1
        if m[y][x1] == 'O' and (x1, y) not in visited:
            q.append((x1, y))

    # move down
    if y <= h - 2:
        y1 = y + 1
        if m[y1][x] == 'O' and (x, y1) not in visited:
            q.append((x, y1))

    # move up
    if y >= 1:
        y1 = y - 1
        if m[y1][x] == 'O' and (x, y1) not in visited:
            q.append((x, y1))

    go(m, h, w, q, visited, region, idx)


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
        region = {}
        idx = 0
        visited = set()
        for y in range(h):
            for x in range(w):
                if m[y][x] == 'O':
                    if not (x, y) in visited:
                        q = [(x, y)]
                        region[idx] = []
                        go(m, h, w, q, visited, region, idx)
                        idx += 1

        match = {}
        for idx, ls in region.items():
            match[idx] = True
            for (x, y) in ls:
                if x == 0 or x == w - 1:
                    match[idx] = False
                    break

                if y == 0 or y == h - 1:
                    match[idx] = False
                    break

        for idx, flag in match.items():
            if flag:
                ls = region[idx]
                for (x, y) in ls:
                    m[y][x] = 'X'
        
