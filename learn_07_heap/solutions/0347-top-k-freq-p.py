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
    "date": "2022/10/4",
    "design": 0,
    "coding": 0,
    "runtime": "265 ms",
    "fasterThan": "14",
    "memory": "18.9 MB" 
}

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}
        for v in nums:
            if v not in h:
                h[v] = 0
            h[v] += 1

        v_c_ls = []
        for v, c in h.items():
            v_c_ls.append((v, c))

        v_c_ls.sort(key = lambda x : x[1], reverse=True)
        
        out = []
        for i in range(k):
            out.append(v_c_ls[i][0])

        return out


