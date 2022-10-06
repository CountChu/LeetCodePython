#
# https://leetcode.com/problems/pascals-triangle-ii/
#
# Given an integer rowIndex, return the rowIndexth (0-indexed) row 
# of the Pascal's triangle.
#
# In Pascal's triangle, each number is the sum of the two numbers directly 
# above it as shown:
#
# Example 1:
#       Input: rowIndex = 3
#       Output: [1,3,3,1]
#
# Example 2: 
#       Input: rowIndex = 0
#       Output: [1]
#
# Example 3:
#       Input: rowIndex = 1
#       Output: [1,1]
#
# Constraints:
#       0 <= rowIndex <= 33
#       

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/6",
    "design": 0,
    "coding": 0,
    "runtime": "63 ms",
    "fasterThan": "22%",
    "memory": "13.9 MB" 
}

'''
    0:      1        1 
    1:     1 1       2 
    2:    1 2 1      3
    3:   1 3 3 1     4
    4:  1 4 6 4 1    5
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1] 

        if rowIndex == 1:
            return [1, 1]

        ctx = {
            'out': None 
        }
        func(2, [1, 2, 1], rowIndex, ctx)
        
        return ctx['out']

'''
     0  1  2
    [1, 2, 1]
'''
def func(idx, ls, target, ctx):
    #print(ls)
    if idx == target:
        ctx['out'] = ls
        return

    new_ls = [1]
    for i in range(1, len(ls)):
        new_ls.append(ls[i-1] + ls[i])
    new_ls.append(1)

    func(idx + 1, new_ls, target, ctx)













