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
    "design": 0,
    "coding": 0,
    "runtime": "71 ms",
    "fasterThan": "73%",
    "memory": "15.4 MB" 
}

class Solution:
    
    def get_digits(self, num):
        out = 0
        while True:
            out += 1
            num = num // 10
            if num == 0:
                break
        return out

    def findNumbers(self, nums: List[int]) -> int:

        out = 0
        for n in nums:
            d = self.get_digits(n)
            #print(n, d)
            if d % 2 == 0:
                out += 1

        return out