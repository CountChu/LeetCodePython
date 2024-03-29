#
# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
#
# Given an array nums of integers, return how many of them contain an even number 
# of digits.
#
# Example 1:
#       Input: nums = [12,345,2,6,7896]
#       Output: 2
#
# Example 2: 
#       Input: nums = [555,901,482,1771]
#       Output: 1 
# 

from typing import List
import pdb

solution_json = {
    "date": "2022/8/31",
    "again": ["2022/10/1"],
    "design": 0,
    "coding": 0,
    "runtime": "66 ms",
    "fasterThan": "81%",
    "memory": "14.1 MB" 
}

def digits(num):
    if num == 0:
        return 1

    out = 0
    while True:
        if num == 0:
            break 
        num = num // 10
        out += 1
    
    return out

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        out = 0

        for n in nums:
            if digits(n) % 2 == 0:
                out += 1
        
        return out