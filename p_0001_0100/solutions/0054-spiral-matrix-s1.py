#
# https://leetcode.com/problems/spiral-matrix/
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2023/11/27",
    "design": 0,
    "coding": 0,
    "runtime": "27 ms",
    "fasterThan": "97%",
    "memory": "16.6 MB" 
}

def move_right(m, p, w, h, out):
    x0, y0 = p

    x = x0
    for x in range(x0+1, x0 + w):
        if m[y0][x] == None:
            return (x-1, y0) 

        out.append(m[y0][x])
        m[y0][x] = None 
        if len(out) == w * h:
            return None        

    return (x, y0)

def move_down(m, p, w, h, out):
    x0, y0 = p

    y = y0
    for y in range(y0+1, y0 + h):
        if m[y][x0] == None:
            return (x0, y-1) 

        out.append(m[y][x0])
        m[y][x0] = None 
        if len(out) == w * h:
            return None

    return (x0, y)

def move_left(m, p, w, h, out):
    x0, y0 = p

    x = x0
    for x in range(x0-1, -1, -1):
        if m[y0][x] == None:
            return (x+1, y0) 

        out.append(m[y0][x])
        m[y0][x] = None 
        if len(out) == w * h:
            return None

    return (x, y0)

def move_top(m, p, w, h, out):
    x0, y0 = p

    y = y0
    for y in range(y0-1, -1, -1):
        if m[y][x0] == None:
            return (x0, y+1) 

        out.append(m[y][x0])
        m[y][x0] = None 
        if len(out) == w * h:
            return None        

    return (x0, y)

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        out = []
        m = matrix
        h = len(m)
        w = len(m[0])

        if h == 1 and w == 1:
            return [m[0][0]]

        p = (0, 0)
        out.append(m[0][0])
        m[0][0] = None
        while True:
            p = move_right(m, p, w, h, out)
            if p == None:
                break

            p = move_down(m, p, w, h, out)
            if p == None:
                break

            p = move_left(m, p, w, h, out)
            if p == None:
                break

            p = move_top(m, p, w, h, out)
            if p == None:
                break
        
        return out
