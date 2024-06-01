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
    "date": "2022/11/10",
    "design": 0,
    "coding": 0,
    "runtime": "64 ms",
    "fasterThan": "23%",
    "memory": "14 MB" 
}

'''   
          0   1   2   3
     0   [1,  2,  3,  4]
     1   [5,  6,  7,  8]
     2   [9, 10, 11, 12]

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        h = len(matrix)
        w = len(matrix[0])
        print(h, w)

        if h == 1 and w == 1:
            v = matrix[0][0]
            return [v]

        if h == 1:
            return matrix[0]

        if w == 1:
            out = []
            for y in range(h):
                v = matrix[y][0]
                out.append(v)
            return out

        l = 0
        r = w - 1
        t = 0
        b = h - 1
        #print(l, r, t, b)

        y = 0
        x = 0
        s = 'init'
        count = 0
        out = []
        while True:


            if s == 'init':
                if x == l:
                    s = 'left-top'
                else:
                    assert False

            elif s in ['left-top', 'move-right']:
                if x == r:
                    s = 'right-top'
                else:
                    s = 'move-right'

            elif s in ['right-top', 'move-bottom']:
                if y == b:
                    s = 'right-bottom'
                else:
                    s = 'move-bottom'

            elif s in ['right-bottom', 'move-left']:
                if x == l:
                    s = 'left-bottom'
                else:
                    s = 'move-left'

            elif s in ['left-bottom', 'move-top']:
                if y == t:
                    s = 'left-top'
                else:
                    s = 'move-top'

            #print('%10s: (%d, %d)' % (s, y, x))

            if s == 'left-top':
                t += 1
                v = matrix[y][x]
                x += 1

            elif s == 'move-right':
                v = matrix[y][x]
                x += 1

            elif s == 'right-top':
                r -= 1
                v = matrix[y][x]
                y += 1

            elif s == 'move-bottom':
                v = matrix[y][x]
                y += 1
            
            elif s == 'right-bottom':
                b -= 1
                v = matrix[y][x]
                x -= 1

            elif s == 'move-left':
                v = matrix[y][x]
                x -= 1
            
            elif s == 'left-bottom':
                l += 1
                v = matrix[y][x]
                y -= 1

            elif s == 'move-top':
                v = matrix[y][x]
                y -= 1

            else:
                assert False, s

            out.append(v)
            #print('v = %d' % v)

            count += 1

            if count >= w * h:
                break

        return out
