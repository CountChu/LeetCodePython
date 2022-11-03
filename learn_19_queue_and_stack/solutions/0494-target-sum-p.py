#
# https://leetcode.com/problems/target-sum/
#
# You are given an integer array nums and an integer target.
#
# You want to build an expression out of nums by adding one of the symbols '+' 
# and '-' before each integer in nums and then concatenate all the integers.
# 
# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 
# and concatenate them to build the expression "+2-1".
#
# Return the number of different expressions that you can build, which evaluates
# to target.
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/28",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB",
    "bug": "Time Limit Exceeded" 
}

'''
     0  1  2  3  4
    [1, 1, 1, 1, 1]  3    
     +  +  +  +  -
     +  +  +  -  +
     +  +  -  +  +
     +  -  +  +  +
     -  +  +  +  +

    sum(0-4) = 3
        +1, sum(1-4) = 2 
            +1, sum(2-4) = 1
                +1, sum(3-4) = 0
                    +1, sum(4) = -1 -------
                    -1, sum(4) = 1 --------
                -1, sum(3-4) = 2
                    +1 +1 -----------------
            -1, sum(2-4) = 3
                +1, sum(3-4) = 2
                    +1 +1 -----------------
                -1, sum(3-4) = 4   (x)  
        -1, sum(1-4) = 4
            +1, sum(2-4) = 3
                +1, sum(3-4) = 2
                    +1, +1 ----------------
                -1, sum(3-4) = 4  (x)
            -1, sum(2-4) = 4      (x)
'''


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        ctx = {}
        ctx['out'] = 0
        f(nums, target, ctx)
        return ctx['out']
        

    def __init__(self):
        self.module = sys.modules[__name__]


def f(nums, target, ctx):

    if nums == []:
        return

    #print(nums, target)

    v0 = nums[0]
    if len(nums) == 1:
        if v0 == target:
            #print('v')
            ctx['out'] += 1

        if v0 == -target:
            #print('v')
            ctx['out'] += 1

    f(nums[1:], target - v0, ctx)
    f(nums[1:], target + v0, ctx)





