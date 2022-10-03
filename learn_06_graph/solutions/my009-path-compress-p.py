#
# https://leetcode.com/explore/learn/card/graph/618/disjoint-set/3880/
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/3",
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
                        v
         0  1  2  3  4  5
        [0, 0, 1, 2, 3, 4]
    """
    def compress_path(self, nums, x):
        root = find_root(nums, x)

def find_root(nums, i):
    p_i = i 
    r_i = None 
    s = []
    while True:
        if nums[p_i] == p_i:
            r_i = p_i
            break
        s.append(p_i)
        p_i = nums[p_i]

    for i in s:
        nums[i] = r_i





