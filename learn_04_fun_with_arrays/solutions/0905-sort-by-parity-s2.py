#
# https://leetcode.com/problems/sort-array-by-parity/
#
# Given an integer array nums, move all the even integers at the beginning 
# of the array followed by all the odd integers.
#
# Return any array that satisfies this condition.
#
# Example 1:
#       Input: nums = [3, 1, 2, 4]
#       Output: [2, 4, 3, 1]
#
# Example 2: 
#       Input: nums = [0]
#       Output: [0]
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/2",
    "design": 0,
    "coding": 0,
    "runtime": "197 ms",
    "fasterThan": "11%",
    "memory": "14.6 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    """
         v
        [3, 1, 2, 4]
        [3]
    
            v
        [3, 1, 2, 4]
        [3, 1]

               v
        [3, 1, 2, 4]
        [2, 3, 1]
        
                  v
        [2, 3, 1, 4]
        [2, 4, 3, 1]

    """
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        j = 0
        n = len(nums)
        out = []
        for i in range(n):
            if nums[i] % 2 == 0:
                out.insert(j, nums[i])
                j += 1
            else:
                out.append(nums[i])

        return out










