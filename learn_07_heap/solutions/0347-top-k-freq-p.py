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
    "date": "2022/9/5",
    "design": 0,
    "coding": 0,
    "runtime": "232 ms",
    "fasterThan": "11%",
    "memory": "18.9 MB" 
}

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for num in nums:
            if num not in h:
                h[num] = 0 
            h[num] += 1

        r_h = {}                        # r_h[count] = [num]
        for num, count in h.items():
            if count not in r_h:
                r_h[count] = []
            r_h[count].append(num)

        count_ls = list(r_h.keys())
        count_ls.sort(reverse=True)
        num_ls = []
        for count in count_ls:
            num_ls += r_h[count]
        
        out = num_ls[:k]

        return out