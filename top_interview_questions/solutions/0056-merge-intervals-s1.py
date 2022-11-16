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
    "date": "2022/11/12",
    "again": ["2022/11/11"],
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB",
    "bug": "Time Limit Exceeded"

}


'''
    1 2 3 6  8  10  15  18
    [   ]    [   ]  [    ]
      [   ] 


    0 1 2 3 4 5
      [     ]
    [   ]
          [   ]


    2, 3, 4, 5, 6, 7
    [  ]  [     ]
             [     ]
       [  ]       

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n == 1:
            return intervals

        q0 = []
        pool = []

        while True:
            if intervals == []:
                break

            int1 = intervals.pop(0)
            #print('int1 = %s' % int1)
            q0.append(int1)
            #print('q0 = %s' % q0)


            for i, int0 in enumerate(q0):
                if is_overlapping(int1, int0):
                    int2 = merge(int1, int0)
                    if int1 in pool:
                        idx = pool.index(int1)
                        pool[idx] = int2

                    if int2 not in pool:
                        pool.append(int2)

                    int1 = int2

                else:
                    pool.append(int0)
                    if i == n - 1:
                        pool.append(int1)
                #print('    pool = %s' % pool)

            q0 = pool

            pool = []

        return q0

def is_overlapping(int1, int0):
    x1, x2 = int1
    x3, x4 = int0

    if x1 <= x2 < x3 <= x4:
        return False

    if x3 <= x4 < x1 <= x2:
        return False

    return True

def merge(int1, int0):
    x1, x2 = int1
    x3, x4 = int0

    return [min(x1, x3), max(x2, x4)]






