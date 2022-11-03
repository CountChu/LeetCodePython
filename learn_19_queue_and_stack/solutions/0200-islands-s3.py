#
# https://leetcode.com/problems/number-of-islands/
#
# Given an m x n 2D binary grid grid which represents a map of '1's (land) 
# and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all 
# surrounded by water.
#
# Example 1:
#       Input: grid = [
#                  ["1","1","1","1","0"],
#                  ["1","1","0","1","0"],
#                  ["1","1","0","0","0"],
#                  ["0","0","0","0","0"]
#              ]
#       Output: 1
#
# Example 2: 
#       Input: grid = [
#                  ["1","1","0","0","0"],
#                  ["1","1","0","0","0"],
#                  ["0","0","1","0","0"],
#                  ["0","0","0","1","1"]
#              ]
#       Output: 3 
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/13",
    "design": 0,
    "coding": 0,
    "runtime": "2189 ms",
    "fasterThan": "5%",
    "memory": "23.6 MB" 
}

'''
        0    1    2    3    4
    0 ["2", "2", "2", "2", "0"],
    1 ["2", "2", "0", "2", "0"],
    2 ["2", "2", "0", "0", "0"],
    3 ["0", "0", "0", "0", "0"],
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        assert m >= 1

        n = len(grid[0])
        assert n >= 1
        
        h = {}                           # h[(y, x)] = seen
        for y in range(m):
            for x in range(n):
                if grid[y][x] == '1':
                    h[(y, x)] = True

        out = 0
        while True:
            if h == {}:
                break

            p = list(h.keys())[0]
            go(p, m, n, h)
            out += 1

        return out

def go(p, m, n, h):
    queue = [p]
    del h[p]

    while True:
        if queue == []:
            break

        y, x = queue.pop(0)
        #print(y, x)

        p = move('left', y, x, m, n, h)
        if p != None:
            queue.append(p)
            del h[p]

        p = move('right', y, x, m, n, h)
        if p != None:
            queue.append(p)
            del h[p]

        p = move('up', y, x, m, n, h)
        if p != None:
            queue.append(p)
            del h[p]

        p = move('down', y, x, m, n, h)
        if p != None:
            queue.append(p)
            del h[p]

def move(dir, y, x, m, n, h):

    if dir == 'left':
        x -= 1
        if x == -1:
            return None

    elif dir == 'right':
        x += 1
        if x == n:
            return None 

    elif dir == 'up':
        y -= 1
        if y == -1:
            return None

    elif dir == 'down':
        y += 1
        if y == m:
            return None

    else:
        assert False, dir

    if (y, x) not in h:
        return None

    return (y, x)
