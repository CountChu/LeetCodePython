#
# https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3880/
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
         0  1  2  3  4  5
        [0, 0, 1, 2, 3, 4]
    """
    def find_root(self, nums, x):
        p_i = x
        while True:
            if nums[p_i] == p_i:
                return p_i 
            p_i = nums[p_i]
     
