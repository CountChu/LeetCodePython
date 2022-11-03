#
# https://leetcode.com/problems/max-consecutive-ones/
#
# Given a binary array nums, return the maximum number of consecutive 1's 
# in the array.
#
# Example 1:
#       Input: nums = [1,1,0,1,1,1]
#       Output: 3
#
# Example 2:
#       Input: nums = [1,0,1,1,0,1]
#       Output: 2
#

from typing import List
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/30",
    "design": 0,
    "coding": 0,
    "runtime": "394 ms",
    "fasterThan": "83%",    
    "memory": "14.2 MB"       
}

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        out = 0

        for v in nums:
            if v == 0:
                count = 0
            else:
                count += 1 
            #print(v, count)
            
            out = max(out, count)

        return out


