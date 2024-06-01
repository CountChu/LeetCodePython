solution_json = {
    "date": "2024/1/10",
    "design": 0,
    "coding": 25,
    "runtime": "124 ms",
    "fasterThan": "88%",
    "memory": "21.89 MB"
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

        [1, 2, 3, 6, 8, 10, 15, 18]
         +     -
            +     -  +   -   +   -
         1  2  1  0  1   0   1   0

    [[2, 3], [4, 6], [5, 7], [3, 4]],
    [[2, 7]])

        [2, 3, 4, 5, 6, 7]
         +  -
            +  -
               +     -
                  +     -

         1  1  1  2  1  0

    [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]],
    [[2, 4], [5, 5]]

        [2,  3,  4,  5]
         +   -      +-
         +-  +   -
             +   -
         1   2   0   0

    [[0, 2], [2, 3], [4, 4], [0, 1], [5, 7], [4, 5], [0, 0]],
    [[0, 3], [4, 7]]

        [0, 1, 2, 3, 4, 5, 7]
         +     -
               +  -
                    +-
         +  -           +  -           
                     +  -
         +-            
'''

def build_h(intervals):
    h = {}
    for b, e in intervals:
        if b not in h:
            h[b] = []
        h[b].append('+')

        if e not in h:
            h[e] = []
        h[e].append('-')

    return h

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        h = build_h(intervals)
        count = 0
        out = []
        b = None
        for idx in sorted(h.keys()):
            flags = h[idx]
            for flag in flags:
                if flag == '+':
                    count += 1

                elif flag == '-':
                    count -= 1

                else:
                    assert False

            #lg(idx, flags, count)


            if b == None:
                b = idx
                #lg('b = %d' % b)

            if count == 0:
                e = idx
                #lg('e = %d' % e)  
                out.append([b, e])
                b = None

        return out
    
