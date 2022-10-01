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

solution_json = {
    "date": "2022/8/31",
    "again": ["2022/10/1"],
    "design": 0,
    "coding": 0,
    "runtime": "352 ms",
    "fasterThan": "96%",
    "memory": "14.3 MB"       
}

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        s = 'init'
        out = 0 
        acc = 0
        for i in range(len(nums)):
            n = nums[i]
            if s in ['init', '1', '0']:
                if n == 1:
                    s = '1'
                elif n == 0:
                    s = '0'
                else:
                    assert False 
            else:
                assert False 

            if s == '1':
                acc += 1
            elif s == '0':
                out = max(acc, out)
                acc = 0
            else:
                assert False

            #print(s, n)

        out = max(acc, out)
        return out


