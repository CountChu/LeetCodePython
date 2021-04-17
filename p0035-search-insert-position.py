# 
# Given a sorted array of distinct integers and a target value, 
# return the index if the target is found. 
# If not, return the index where it would be 
# if it were inserted in order.
# 

from typing import List
import pdb

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        idx = -1
        #print('target = %d' % target)
        for i in range(len(nums)):
            line = ''
            line  += ('nums[%d] = %d, ' % (i, nums[i]))
            
            if nums[i] >= target:
                idx = i
                line += 'idx = %d, ' % idx
                print(line)
                return idx
            
            #print(line)
        
        return i+1
        #pdb.set_trace()
        

