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

def compress_path(nums, x):
    print('x = %d' % x)

    px = nums[x]
    if px == x:
        #print(x, px)
        return px

    r = compress_path(nums, px)
    #print(x, r)
    nums[x] = r
    return r

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def compress_path(self, nums, x):
        compress_path(nums, x)
