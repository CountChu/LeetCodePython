# 
# Given an array nums and a value val, remove all instances of that value in-place and return the new length.
# 
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
# 
# The order of elements can be changed. It doesn't matter what you leave beyond the new length.
# 

from typing import List
import pdb

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx = 0
        for i in range(len(nums)):
            line = ''
            line += 'nums[%d] = %d, ' % (i, nums[i])
            if nums[i] != val:
                nums[idx] = nums[i]
                line  += 'nums[%d] = %d, ' % (idx, nums[idx])
                idx += 1
            #print(line)
        return idx
