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
    "design": 0,
    "coding": 0,
    "runtime": "419 ms",
    "fasterThan": "9%",
    "memory": "20.1 MB" 
}

'''
        [[1, 3], [2, 6], [8, 10], [15, 18]]

        1 2 3 6 8 10 15 18
        [   ]
          [   ]
                [  ]
                     [   ]

        [[2, 3], [5, 5], [2, 2], [3, 4], [3, 4]]

        2  3  4  5
        [  ]
        [] [  ]  []
           [  ]

        1  2  0  0
        [  -  ]  []

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #intervals = sorted(intervals, key = lambda x: x[0])
        
        h = {}          # h[x] = {'[': 1, ']': 2}
        for i, [x0, x1] in enumerate(intervals):
            
            if x0 not in h:
                h[x0] = {'[': 0, ']': 0}
            
            if x1 not in h:
                h[x1] = {'[': 0, ']': 0}

            h[x0]['['] += 1
            h[x1][']'] += 1

        #dump(h)

        out = []
        acc = 0
        state = 'init'
        for x in sorted(h.keys()):
            if x0 == None:
                x0 = x
            
            count = h[x]
            acc += count['['] - count[']']

            if state == 'init':
                if acc == 0:
                    state = '[]'
                elif acc > 0:
                    state = '['
                else:
                    assert False

            elif state == '[]':
                if acc == 0:
                    state = '[]'
                elif acc > 0:
                    state = '['
                else:
                    assert False

            elif state == '[':
                if acc == 0:
                    state = ']'
                elif acc > 0:
                    state = '-'
                else:
                    assert False 

            elif state == '-':
                if acc == 0:
                    state = ']'
                elif acc > 0:
                    state = '-'
                else:
                    assert False    

            elif state == ']':
                if acc == 0:
                    state = '[]'
                elif acc > 0:
                    state = '['
                else:
                    assert False

            #print(x, acc, state)

            if state == '[':
                x0 = x 
            elif state == ']':
                x1 = x 
                out.append([x0, x1])
            elif state == '[]':
                x0 = x1 = x
                out.append([x0, x1])

        return out

def dump(h):
    for x in sorted(h.keys()):
        count = h[x]
        print('%d: %s' % (x, count))

