solution_json = {
    "date": "2023/12/18",
    "design": 0,
    "coding": 8,
    "runtime": "35 ms",
    "fasterThan": "87%",
    "memory": "16.37 MB"
}

#
# https://leetcode.com/problems/pascals-triangle/
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''

       0 1 2 3 4

    0: 1
    1: 1 1
    2: 1 2 1
    3: 1 3 3 1
    4: 1 4 6 4 1

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def generate(self, numRows: int) -> List[List[int]]:
        out = []
        for i in range(numRows):
            if i == 0:
                ls1 = [1]
            elif i == 1:
                ls1 = [1, 1]
            else:
                ls1 = [1]
                for j in range(i - 1):
                   v = ls0[j] + ls0[j+1]
                   ls1.append(v)
                ls1.append(1) 

            out.append(ls1)
            #lg(ls1)
            ls0 = ls1

        return out


