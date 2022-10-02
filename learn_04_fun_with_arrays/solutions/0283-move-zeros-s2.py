#
# https://leetcode.com/problems/move-zeroes/
#
# Given an integer array nums, move all 0's to the end of it 
# while maintaining the relative order of the non-zero elements.
#
# Note that you must do this in-place without making a copy of the array.
#
# Example 1:
#       Input: nums = [0, 1, 0, 3, 12]
#       Output: [1, 3, 12, 0, 0]
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
    "runtime": "429 ms",
    "fasterThan": "27%",
    "memory": "15.7 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    """
         v
        [0, 1, 0, 3, 12]

            v
        [0, 1, 0, 3, 12]
        [1, 0, 0, 3, 12]

               v
        [1, 0, 0, 3, 12]

                  v
        [1, 0, 0, 3, 12]
        [1, 3, 0, 0, 12]

                     v
        [1, 3, 0, 0, 12]
        [1, 3, 12, 0, 0]
    """
    def moveZeroes(self, nums: List[int]) -> None:
        s = []
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                s.append(i)
            else:
                if len(s) >= 1:
                    zero_idx = s.pop(0)
                    nums[zero_idx], nums[i] = nums[i], nums[zero_idx]
                    s.append(i)







