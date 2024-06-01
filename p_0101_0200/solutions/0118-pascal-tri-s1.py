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

solution_json = {
    "date": "2023/12/2",
    "design": 0,
    "coding": 0,
    "runtime": "43 ms",
    "fasterThan": "38%",
    "memory": "16.23 MB" 
}

'''
             1      0
           1   1    1  ls
          1  2  1   2  ls1
         1 3  3  1  3

    ls1[0] = ls[0] 
    ls1[1] = ls[0] + ls[1]
    ls1[2] = ls[1]   
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]

        ls = []
        out = []
        for i in range(numRows):
            if i == 0:
                ls = [1]
            else:
                n = len(ls)
                for j in range(n):
                    if j == 0:
                        ls1 = [ls[j]]
                    else:
                        ls1.append(ls[j-1] + ls[j])
                ls1.append(ls[-1])
                ls = ls1
            #print(ls)
            out.append(ls)

        return out
