#
# https://leetcode.com/problems/remove-element/
#
# Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
# The relative order of the elements may be changed.
#
# Since it is impossible to change the length of the array in some languages, 
# you must instead have the result be placed in the first part of the array nums. 
# More formally, if there are k elements after removing the duplicates, 
# then the first k elements of nums should hold the final result. 
# It does not matter what you leave beyond the first k elements.
#
# Return k after placing the final result in the first k slots of nums.
#
# Do not allocate extra space for another array. You must do this 
# by modifying the input array in-place with O(1) extra memory.
#
# Example 1:
#       Input: nums = [3, 2, 2, 3], val = 3
#       Output: 2, nums = [2, 2, _, _]
#
# Example 2: 
#       nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
#       5, nums = [0, 1, 4, 0, 3, _ ,_ ,_]
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
    def __init__(self):
        self.module = sys.modules[__name__]

    def removeElement(self, nums: List[int], val: int) -> int:
        return 0