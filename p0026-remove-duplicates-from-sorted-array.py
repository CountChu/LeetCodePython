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

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        idx2 = 1
        for i in range(len(nums)):
            line = ''
            line += 'i = %d, ' % i
            num = nums[i]
            line += 'num = %d, ' % num
            line += 'idx = %d, ' % idx
            num2 = nums[idx]
            line += 'num2 = %d, ' % num2
            if num2 != num:
                idx = i
                line += 'idx = %d, ' % idx
                num3 = nums[idx]
                line += 'num3 = %d, ' % num3
                nums[idx2] = num3
                idx2 += 1
            #print(line)
        return idx2
        


