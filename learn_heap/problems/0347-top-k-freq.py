#
# https://leetcode.com/problems/top-k-frequent-elements/
#
# Given an integer array nums and an integer k, return the k most frequent elements. 
# You may return the answer in any order.
#
# Example 1:
#       Input: nums = [1,1,1,2,2,3], k = 2
#       Output: [1,2]
#
# Example 2: 
#       Input: nums = [1], k = 1
#       Output: [1]
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/?/??",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for num in nums:
            if num not in h:
                h[num] = 0 
            h[num] += 1
        br()