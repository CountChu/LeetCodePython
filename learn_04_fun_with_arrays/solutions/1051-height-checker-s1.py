from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2021/4/29",
    "again": ["2022/10/2"],
    "design": 0,
    "coding": 2,
    "runtime": "35 ms",
    "fasterThan": "96%",
    "memory": "14 MB"      
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
