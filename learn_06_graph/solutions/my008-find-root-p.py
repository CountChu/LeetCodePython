#
# https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3880/
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/9/12",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

"""
    [0, 0, 1, 2, 3, 4]
     0  1  2  3  4  5

    r = find_root(nums, 2)
        nums[2] = 1
        r = find_root(nums, 1)
            nums[1] = 0
            r = find_root(nums, 0)
                nums[0] = 0
                return 0
"""

def find_root(nums, x):
    px = nums[x]
    if px == x:
        return px 
    return find_root(nums, px)

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def find_root(self, nums, x):
        r = find_root(nums, x)
        return r
     
