solution_json = {
    "date": "2023/12/30",
    "design": 0,
    "coding": 10,
    "runtime": "130 ms",
    "fasterThan": "80%",
    "memory": "22.02 MB"
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
#lg = print

'''
    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]

        1  2  3  6  8  10  15  18
        b     e
           b     e
                    b   e   
                            b   e
        b  b  e  e  b   e   b   e
        1  2  1  0  1   0   1   0

    Input: intervals = [[1,4],[4,5]]
    Output: [[1,5]]

        1  4  5
        b  e
           b  e
        b  eb e   
        1  1  0 

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        h = {}
        for b, e in intervals:
            if b not in h:
                h[b] = []
            h[b].append('b')

            if e not in h:
                h[e] = []
            h[e].append('e')

        count = 0
        b = None
        out = []
        for i in sorted(h.keys()):
            if b == None:
                b = i

            s_ls = h[i]
            for s in s_ls:
                if s =='b':
                    count += 1
                elif s == 'e':
                    count -= 1
                else:
                    assert False, s_ls
            #lg('[%d] %s, %d' % (i, s_ls, count))
            if count == 0:
                e = i 
                #lg('    [%d, %d]' % (b, e))
                out.append([b, e])
                b = None

        return out
    
