#
# https://leetcode.com/problems/permutations/
#
# Given an array nums of distinct integers, return all the possible permutations. 
# You can return the answer in any order.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2023/11/26",
    "design": 0,
    "coding": 0,
    "runtime": "45 ms",
    "fasterThan": "56%",
    "memory": "16.52 MB" 
}


'''
     0  1  2
    [1, 2, 3]
        1 [2, 3]  perm(1, [2, 3])
        2 [1, 3]  perm(2, [1, 3])
        3 [1, 2]  perm(3, [1, 2])

     0  1
    [2, 3]
        1  [2]    perm(2, [3])  
        2  [3]    perm(3, [2])    
'''

def perm(v, ls, path, out):
    #print(v, ls, path)

    if len(ls) == 1:
        path = path + ls 
        #print('path = %s' % path)
        out.append(path)
        return

    for i in range(len(ls)):
        v1 = ls[i]
        ls1 = ls[0:i] + ls[i+1:]
        perm(v1, ls1, path + [v1], out)

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        out = []
        for i in range(len(nums)):
            v = nums[i]
            ls = nums[0:i] + nums[i+1:]
            perm(v, ls, [v], out)
        return out
