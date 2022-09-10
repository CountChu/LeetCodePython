#
# https://leetcode.com/problems/house-robber/
#
# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint 
# stopping you from robbing each of them is that adjacent houses 
# have security systems connected and it will automatically contact the police 
# if two adjacent houses were broken into on the same night.
# 
# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without 
# alerting the police.
#
# Example 1:
#       Input: nums = [1,2,3,1]
#       Output: 4
#
# Example 2: 
#       Input: nums = [2,7,9,3,1]
#       Output: 12
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/9/8",
    "design": 0,
    "coding": 0,
    "runtime": "44 ms",
    "fasterThan": "66%",
    "memory": "13.9 MB" 
}

"""
    dp[i]:
        case1: nums[i] + dp[i-2]
        case2: dp[i-1]
    dp[i] = max(case1, case2)

    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
 
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0 

        dp = [0] * n

        if n >= 1:
            dp[0] = nums[0] 

        if n >= 2:
            dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])

        return dp[n-1]




