solution_json = {
    "date": "2024/1/15",
    "design": 0,
    "coding": 20,
    "runtime": "132 ms",
    "fasterThan": "63%",
    "memory": "22.16 MB"
}

#
# https://leetcode.com/problems/merge-intervals/
#
# Medium.
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
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]

         0  1  2  3  4   5   6   7
        [1, 2, 3, 6, 8, 10, 15, 18]
         +     -
            +     -
                     +   -   +   -
         1  2  1  0  1   0   1   0

    Case 2:

        [1, 2, 3, 6, 8, 10, 15, 18]
         +  -  +- +  +   -   -   +-
         1  0  0  1  2   1   0   0
'''

def build_h(h):
    ls = sorted(h.keys())
    c = 0
    count = 0       
    out = {}
    for v in ls:
        flag_ls = h[v]

        for f in flag_ls:
            if f == '+':
                count += 1
            elif f == '-':
                count -= 1
            else:
                assert False
        out[v] = count

    return ls, out

'''
    [0] [1]  1  b
    [1] [2]  2
    [2] [3]  1
    [3] [6]  0  e
    [4] [8]  1  b
    [5] [10] 0  e
    [6] [15] 1  b
    [7] [18] 0  e
'''    


class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        h = {}
        for b, e in intervals:
            if not b in h:
                h[b] = []
            h[b].append('+')

            if not e in h:
                h[e] = []
            h[e].append('-')
        #lg(h)

        ls, h1 = build_h(h)
        #for v in ls:
            #lg('[%d] %d' % (v, h1[v]))

        out = []
        b = None
        for i in range(len(ls)):
            v = ls[i]
            c = h1[v]
            #lg('[%d] [%d] %d' % (i, v, c))

            if b == None:
                if c != 0:
                    b = v
                    #lg('b = %d' % b)
                else:
                    b = v
                    e = v
                    #lg('b = %d' % b)
                    #lg('e = %d' % e)
                    out.append([b, e])
                    b = None
            else:
                if c == 0:
                    e = v
                    #lg('e = %d' % e)
                    out.append([b, e])
                    b = None

        return out


    
