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

solution_json = {
    "date": "2023/11/28",
    "design": 0,
    "coding": 0,
    "runtime": "134 ms",
    "fasterThan": "72%",
    "memory": "21.11 MB" 
}

'''
    [1, 3], [2, 6], [8, 10], [15, 18]
    --->
    [1, 6], [8, 10], [15, 18]


    1  2  3  6  8  10  15  18
    -------
       -------
                -----
                       ------
'''

def my_sort(intervals):
    out = sorted(intervals, key=lambda x: x[0])
    return out

def overlap(e0, e1):
    a, b = e0
    c, d = e1
    if b >= c:
        return [a, max(b, d)]
    else:
        return None

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ls = my_sort(intervals)

        n = len(ls)
        e = ls[0]
        out = []
        for i in range(1, n):
            e1 = overlap(e, ls[i])
            if e1 != None:
                e = e1
            else:
                out.append(e)
                e = ls[i]

        out.append(e)
        
        return out    
