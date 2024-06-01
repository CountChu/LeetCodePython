solution_json = {
    "date": "2023/12/15",
    "design": 0,
    "coding": 0,
    "runtime": "130 ms",
    "fasterThan": "87%",
    "memory": "21.37 MB"
}

#
# https://leetcode.com/problems/merge-intervals/
#
# Given an array of intervals where intervals[i] = [starti, endi], 
# merge all overlapping intervals, and return an array of the non-overlapping 
# intervals that cover all the intervals in the input. 
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
          0       1        2         3
    [[1, 3], [2, 6], [8, 10], [15, 18]]

            1 2 3 6 8 10 15 18
    i = 0:  b - e
    i = 1:  b - - e
    i = 2:  b - - e b  e
    i = 3:  b - - e b  b  b  e

          0       1       2       3
    [[2, 3], [4, 6], [5, 7], [3, 4]]

            2 3 4 5 6 7
    i = 0:  b e
    i = 1:  b e b - e
    i = 2:  b e b - - e
    i = 3:  b - - - - e

         0       1       2       3      4
    [2, 3], [5, 5], [2, 2], [3, 4], [3, 4]

            2  3  4  5
    i = 0:  b  e
    i = 1:  b  e    be      
    i = 2:  b  e    be
    i = 3:  b  -  e be
    i = 4:  b  -  e be

          0       1       2       3       4       5       6
    [[0, 2], [2, 3], [4, 4], [0, 1], [5, 7], [4, 5], [0, 0]]

            0  1  2  3  4  5  7
    i = 0:  b  -  e
    i = 1:  b  -  -  e
    i = 2:  b  -  -  e be
    i = 3:  b  -  -  e be 
    i = 4:  b  -  -  e be  b  e
    i = 5:  b  -  -  e  b  -  e

'''

def dump(h):
    for x, s in h.items():
        lg('%s ' % s, end='')
    lg('')

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pts = set()
        for [x0, x1] in intervals:
            pts.add(x0)
            pts.add(x1)

        ls = list(pts)
        ls.sort()
        #lg(ls)

        h = {}
        for x in ls:
            h[x] = ''

        for [x0, x1] in intervals:
            #lg('(%d, %d)' % (x0, x1))
            if x0 == x1:
                if h[x0] == '':
                    h[x0] = 'be'
                #dump(h)
                continue

            if h[x0] == '':
                h[x0] = 'b'
            elif h[x0] == 'e':
                h[x0] = '-'
            elif h[x0] == 'be':
                h[x0] = 'b'

            if h[x1] == '':
                h[x1] = 'e'
            elif h[x1] == 'b':
                h[x1] = '-'
            elif h[x1] == 'be':
                h[x1] = 'e'

            for i in range(x0+1, x1):
                if i not in pts:
                    continue
                h[i] = '-'
            
            #dump(h)

        out = []
        x0 = None
        for x in sorted(h.keys()):
            s = h[x]
            if s == 'b':
                x0 = x
            elif s == 'e':
                x1 = x
                #lg(x0, x1)
                out.append([x0, x1])
            elif s == 'be':
                #lg(x, x)
                out.append([x, x])

        return out
    
