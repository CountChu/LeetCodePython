solution_json = {
    "date": "2023/12/29",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "??%",
    "memory": "?? MB"
}

#
# https://leetcode.com/problems/jump-game/
#
# You are given an integer array nums. You are initially positioned 
# at the array's first index, and each element in the array represents 
# your maximum jump length at that position.
#
# Return true if you can reach the last index, or false otherwise.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
#lg = print

'''
    Input: nums = [2,3,1,1,4]
    Output: true
    
         0  1  2  3  4
        [2, 3, 1, 1, 4]
            .  .

        [0] 2
            [1] 3
                [2] 1
                    [3] 1
                        [4] 4
                [3] 1
                    [4] 4
                [4] 4
            [2] 1
                [3] 1
                    [4] 4

    Input: nums = [3,2,1,0,4]
    Output: false

         0  1  2  3  4
        [3, 2, 1, 0, 4]

        [0] 3
            [1] 2 -> x 
                [2] 1 -> x
                    [3] 0 -> x
                [3] 0
            [2] 1
                [3] 0
            [3] 0 -> x
'''

def go(ls, n, idx, level, dp, ctx):
    if ctx['touch']:
        return

    if idx >= n - 1:
        ctx['touch'] = True
        return

    v = ls[idx]
    #lg('%s[%d] %d' % ('    '*level, idx, v))
    count = 0
    for i in range(v):
        idx1 = idx + i + 1
        go(ls, n, idx1, level+1, dp, ctx)
        if idx1 in dp:
            count += 1

    if count == v:
        dp.add(idx)    

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canJump(self, nums: List[int]) -> bool:
        ls = nums
        n = len(ls)
        if n == 1:
            return True

        dp = set()
        ctx = {'touch': False}
        go(ls, n, 0, 0, dp, ctx)
        #lg(dp)
        return ctx['touch']
