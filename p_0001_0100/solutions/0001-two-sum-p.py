#
# https://leetcode.com/problems/two-sum/
#
# Given an array of integers nums and an integer target, return indices 
# of the two numbers such that they add up to target.  
#

from typing import List
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2023/11/22",
    "design": 0,
    "coding": 0,
    "runtime": "57 ms",
    "fasterThan": "92.%",    
    "memory": "17.69 MB"
}

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  
        d = {}
        for i in range(len(nums)):
            v = nums[i]
            if v in d:
                if v + v == target:
                    return [d[v], i]
            d[v] = i
        
        for v, idx in d.items():
            v2 = target - v 
            if v2 in d:
                if idx != d[v2]:
                    return [idx, d[v2]]

        return []

