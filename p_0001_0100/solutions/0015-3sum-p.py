#
# https://leetcode.com/problems/3sum/
#
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/6",
    "design": 0,
    "coding": 0,
    "runtime": "1380 ms",
    "fasterThan": "76%",
    "memory": "18 MB"
}

'''
        [-1, 0, 1, 2, -1, -4]

        [-4, -1, -1, 0, 1, 2]
    i=0   .  twoSum(4)  
    i=1       .
    i=2           .  
    i=3              .

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        #print(nums)

        out = []
        pre_v = None
        for i in range(0, len(nums) - 2):
            v0 = nums[i]
            if pre_v != None and pre_v == v0:
                continue 

            pre_v = v0
            #print(i, v0)

            pair_ls = twoSum(nums[i+1:], -v0)
            for v1, v2 in pair_ls: 
                #print(v0, v1, v2)
                triple = [v0, v1, v2]
                out.append(triple)

        return out

def twoSum(nums, target):
    #print(nums, target)
    h = {}
    for i, v in enumerate(nums):
        if v not in h:
            h[v] = i

    out = []
    for i, v0 in enumerate(nums):
        v1 = target - v0

        if v1 in h:
            j = h[v1]
            if i <= j:
                continue

            pair = [v0, v1]
            pair.sort()

            if pair not in out:
                out.append(pair)
    return out


