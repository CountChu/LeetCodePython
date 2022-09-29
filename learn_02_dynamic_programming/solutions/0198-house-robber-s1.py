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
    "again": ["2022/9/29"],
    "design": 0,
    "coding": 0,
    "runtime": "44 ms",
    "fasterThan": "66%",
    "memory": "13.9 MB" 
}

'''
Example 1:
    1, 2, 3, 1
    V     V     4 
    V        V  2 
       V     V  3

Example 2:
    0  1  2  3  4
    2, 7, 9, 3, 1
    V     V     V    12 
    V        V        6
    V           V     3 
       V     V       10 
       V        V     8
          V     V    10  

dp[4] = nums[4] + dp[2] = 1 + dp[2] 
dp[2] = nums[2] + dp[0] = 9 + dp[0]
dp[0] = nums[0] = 2

dp[4] = max(nums[4] + dp[2], dp[3])

dp[i] = max(nums[i] + dp[i-2], dp[i-1])
dp[0] = nums[0] 
dp[1] = nums[1]
dp[2] = max(nums[2] + dp[0], dp[1]) = max(11, 7) = 11
'''

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

        return dp[-1]




