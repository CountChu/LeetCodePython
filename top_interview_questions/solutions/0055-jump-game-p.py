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

solution_json = {
    "date": "2022/11/11",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB",
    "bug": "Time Limit Exceeded" 
}

'''
         0  1  2  3  4
        [2, 3, 1, 1, 4]
         .  .        .

        jump(0, 2) = [1, 2]
        jump(1, 3) = [2, 3, 4]
        jump(2, 1) = [3]
        jump(3, 1) = [4]


         0  1  2  3  4
        [3, 2, 1, 0, 4]
         .        . 

        jump(0, 3) = [1, 2, 3]
        jump(1, 2) = [2, 3]
        jump(2, 1) = [3]
        jump(3, 0) = []
        jump(4, 4) = []

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        jump = {}                       # jump[(idx, v)] = [next_idx_ls]
        for i, v in enumerate(nums):
            #print(i, v)
            jump[(i, v)] = []
            for j in range(v):
                #print(i + j + 1)
                next_idx = i + j + 1
                if next_idx >= len(nums):
                    continue

                jump[(i, v)].append(next_idx)
        #dump(jump)

        graph = {}
        for (idx, v), next_idx_ls in jump.items():
            if next_idx_ls == []:
                continue

            if idx not in graph:
                graph[idx] = {}
            for next_idx in next_idx_ls:
                graph[idx][next_idx] = 1

        out = go(graph, 0, len(nums) - 1)
        return out

def dump(jump):
    for (idx, v), next_idx_ls in jump.items():
        print('(%d, %d): %s' % (idx, v, next_idx_ls))


def go(graph, v0, vf):
    q = [v0]
    seen = set()
    seen.add(v0)

    while True:
        if q == []:
            break

        #print('q = %s' % q)
        v0 = q.pop(0)
        #print('v0 = %d' % v0)

        if v0 not in graph:
            continue

        for v1 in graph[v0]:
            if v1 in seen:
                continue

            #print('v1 = %d' % v1)
            if v1 == vf:
                return True

            q.append(v1)
            seen.add(v1)

    return False


