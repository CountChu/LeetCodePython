#
# https://leetcode.com/problems/two-sum/
#
# Given an array of integers nums and an integer target, return indices 
# of the two numbers such that they add up to target.  
#

from typing import List
import pdb

solution_json = {
    "date": "2021/4/10",
    "coding": 7,
    "runtime": "48 ms",
    "memory": "14.5 MB"
}

#
# 2021/4/10: 7 mins
#

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = len(nums)
        for i in range(m - 1):
            for j in range(1, m):
                if i != j:
                    if nums[i] + nums[j] == target:
                        return [i, j]
                #print(i, j)
        
        return None        
        #pdb.set_trace()        
