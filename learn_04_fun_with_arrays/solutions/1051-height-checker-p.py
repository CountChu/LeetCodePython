#
# https://leetcode.com/problems/height-checker/
#
# A school is trying to take an annual photo of all the students. 
# The students are asked to stand in a single file line in non-decreasing 
# order by height. Let this ordering be represented by the integer array expected 
# where expected[i] is the expected height of the ith student in line.
#
# Example 1:
#       Input: heights = [1, 1, 4, 2, 1, 3]
#       Output: 3
#
# Example 2: 
#       Input: heights = [5, 1, 2, 3, 4]
#       Output: 5
#
# Example 3: 
#       Input: heights = [1, 2, 3, 4, 5]
#       Output: 0
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/2",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    """
        [1, 1, 4, 2, 1, 3]
        [1, 1, 1, 2, 3, 4]

        [5, 1, 2, 3, 4]
        [1, 2, 3, 4, 5]
    """
    def heightChecker(self, heights: List[int]) -> int:
        order = heights.copy()
        order.sort()

        out = 0
        for i in range(len(order)):
            if order[i] != heights[i]:
                out += 1

        return out
