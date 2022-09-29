#
# https://leetcode.com/problems/squares-of-a-sorted-array/
#
# Given an integer array nums sorted in non-decreasing order, return an array 
# of the squares of each number sorted in non-decreasing order.
#
# Example 1:
#       Input: nums = [-4,-1,0,3,10]
#       Output: [0,1,9,16,100]
#
# Example 2:
#       Input: nums = [-7,-3,2,3,11]
#       Output: [4,9,9,49,121]
#


from typing import List
import pdb

solution_json = {
    "date": "2022/8/31",
    "design": 0,
    "coding": 0,
    "runtime": "255 ms",
    "fasterThan": "84%",
    "memory": "18.2 MB"       
}

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        out = []
        h = {}
        for n in nums:
            if n not in h:
                h[n] = n*n
            out.append(h[n])
        out.sort()
        return out      
