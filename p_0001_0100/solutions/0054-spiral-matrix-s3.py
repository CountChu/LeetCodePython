solution_json = {
    "date": "2023/12/29",
    "design": 0,
    "coding": 0,
    "runtime": "68 ms",
    "fasterThan": "5%",
    "memory": "17.31 MB"
}

#
# https://leetcode.com/problems/spiral-matrix/
#
# Given an m x n matrix, return all elements of the matrix in spiral order.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
#lg = print

'''
         0   1   2   3  

     0   1   2   3   4
     1   5   6   7   8
     2   9  10  11  12  


     . . . . .
     . . . . .
     . . . . .
     . . . . .

     . . .
     . . .
     . . .
     . . .

'''

def go(m, w, h, start_x, start_y, out, vis):
    width = w - start_x - start_x
    height = h - start_y - start_y
    #lg('width = %d, height = %d' % (width, height))
    if width == 1 and height == 1:
        if (start_x, start_y) in vis:
            return        

        out.append(m[start_x][start_y])
        vis.add((start_x, start_y))

    # go right
    #lg('right: ', end='')
    y = start_y
    #lg('y = %d: ' % y, end='')
    for x in range(start_x, start_x+width-1):
        if (x, y) in vis:
            return

        #lg('%d, ' % m[y][x], end='')
        out.append(m[y][x])
        vis.add((x, y))
    #lg('')

    # go down
    #lg('down:  ', end='')
    x = w - 1 - start_x
    #lg('x = %d: ' % x, end='')    
    for y in range(start_y, start_y+height-1):
        if (x, y) in vis:
            return

        #lg('%d, ' % m[y][x], end='')
        out.append(m[y][x])
        vis.add((x, y))
    #lg('')

    # go left
    #lg('left:  ', end='')
    y = h - 1 - start_y
    #lg('y = %d: ' % y, end='')
    for x in reversed(range(start_x+1, w - start_x)):
        if (x, y) in vis:
            return

        #lg('%d, ' % m[y][x], end='')
        out.append(m[y][x])
        vis.add((x, y))
    #lg('')    

    # go up
    x = start_x
    #lg('up:    ', end='')
    #lg('x = %d: ' % x, end='')    
    for y in reversed(range(start_y+1, h - start_y)):
        if (x, y) in vis:
            return

        #lg('%d, ' % m[y][x], end='')
        out.append(m[y][x])
        vis.add((x, y))
    #lg('')

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = matrix
        h = len(m)
        w = len(m[0])

        start_x = 0
        start_y = 0

        out = []
        vis = set()
        while True:
            #lg('(%d, %d)' % (start_x, start_y))
            go(m, w, h, start_x, start_y, out, vis)
            if len(vis) == w * h:
                break

            start_x += 1
            start_y += 1
        
        return out
