#
# https://leetcode.com/problems/maximum-subarray/
#
# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.
#

from typing import List
import pdb

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def get_sum(nums, start, end):
            sum = 0
            for i in range(start, end+1):
                sum += nums[i]
            return sum      
        table = []
        max_sum = None
        max_row = None
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                #print(i, j)
                sum = get_sum(nums, i, j)
                row = (i, j, sum)
                table.append(row)
                if max_sum == None:
                    max_sum = sum
                    max_row = row
                elif max_sum < sum:
                    max_sum = sum
                    max_row = row    
        for row in table:
            print(row)      
        return max_sum