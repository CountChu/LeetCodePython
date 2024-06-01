#
# https://leetcode.com/problems/two-sum/
#
# Given an array of integers nums and an integer target, return indices 
# of the two numbers such that they add up to target.  
#

from typing import List
import pdb

solution_json = {
    "date": "2021/4/17",
    "coding": 7,
    "runtime": "48 ms",
    "memory": "14.4 MB"
}

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        hash = {}
        for i in range(n):
            v = nums[i]
            v2 = target - v
            if v2 in hash:
                return [i, hash[v2]]
            else:
                hash[v] = i

        return []