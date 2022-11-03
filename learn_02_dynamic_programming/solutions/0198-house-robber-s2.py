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

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/30",
    "design": 0,
    "coding": 0,
    "runtime": "65 ms",
    "fasterThan": "27%",
    "memory": "13.8 MB" 
}


'''
     0  1  2  3
    [2, 1, 1, 2]
     v     v
     v        v
        v     v
    
    dp[0] = 2
    dp[1] = 1
    dp[2] = 1 + dp[0] = 3
    dp[3] = 2 + dp[1] = 3
    dp[3] = 2 + dp[0] = 2 + 2 = 4

     0  1  2  3  4
    [2, 7, 9, 3, 1]
     v     v     v 
        v     v
          
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        for i, v in enumerate(nums):
            dp[i] = v 
            
            if i >= 2:
                dp[i] += max(dp[:i-1])

        return max(dp)
