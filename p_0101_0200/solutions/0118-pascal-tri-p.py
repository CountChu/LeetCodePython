#
# https://leetcode.com/problems/pascals-triangle/
#
# Given an integer numRows, return the first numRows of Pascal's triangle.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/31",
    "design": 0,
    "coding": 0,
    "runtime": "45 ms",
    "fasterThan": "75%",
    "memory": "13.9 MB" 
}

'''
     1       n = 1
    1 1      n = 2
   1 2 1     n = 3 
  1 3 3 1    n = 4

   0 1      
  [1 1]      n = 2

   0 1 2
  [1 2 1]    n = 3

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]] 
        if numRows == 2:
            return [[1], [1, 1]]

        out_ls = [[1], [1, 1]]
        out = [0] * numRows
        out[0] = 1
        out[1] = 1
        for n in range(3, numRows + 1):
            out = gen_next(out, n)
            out_ls.append(out)

        return out_ls

def gen_next(nums, n):
    out = [0] * n
    idx = 0
    for i in range(n-1):
        #print('i = %d' % i)

        if i == 0:
            v = nums[i]
            out[idx] = v
            idx += 1

            v = nums[i] + nums[i+1]
            out[idx] = v
            idx += 1

        elif i == n-2:
            v = nums[i]
            out[idx] = v
            idx += 1

        else:
            v = nums[i] + nums[i+1]
            out[idx] = v
            idx += 1
    
    return out
