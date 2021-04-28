#
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# 
# Given a sorted array nums, remove the duplicates in-place such 
# that each element appears only once and returns the new length.
# 
# Do not allocate extra space for another array, you must do this 
# by modifying the input array in-place with O(1) extra memory.
#

from typing import List
import pdb

#
# 2021/3/24: 108 ms, 16 MB
#

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        idx2 = 1
        for i in range(len(nums)):
            num = nums[i]
            num2 = nums[idx]
            if num2 != num:
                idx = i
                num3 = nums[idx]
                nums[idx2] = num3
                idx2 += 1
        return idx2
        


