#
# https://leetcode.com/problems/third-maximum-number/
#
# Given an integer array nums, return the third distinct maximum number in this array. 
# If the third maximum does not exist, return the maximum number.
#
# Example 1:
#       Input: nums = [3, 2, 1]
#       Output: 1
#
# Example 2: 
#       Input: nums = [1, 2]
#       Output: 2
# 
# Example 3: 
#       Input: nums = [2, 2, 3, 1]
#       Output: 1
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/2",
    "design": 0,
    "coding": 0,
    "runtime": "122 ms",
    "fasterThan": "16%",
    "memory": "14.8 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    """  
         v
        [2, 2, 3, 1]
        [2]
    
            v
        [2, 2, 3, 1]
        [2]

               v
        [2, 2, 3, 1]
        [2, 3]

                  v
        [2, 2, 3, 1]
        [1, 2, 3]
    """

    def thirdMax(self, nums: List[int]) -> int:
        max_ls = []
        for v in nums:
            #print(v, max_ls)
            if len(max_ls) <= 2:
                if v not in max_ls:
                    max_ls.append(v)
                    max_ls.sort()
            else:
                if v > max_ls[0]:
                    if v not in max_ls:
                        max_ls.pop(0)                
                        max_ls.append(v)
                        max_ls.sort()

        #br()
        if len(max_ls) == 3:
            return max_ls[0]
        else:
            return max_ls[-1]

