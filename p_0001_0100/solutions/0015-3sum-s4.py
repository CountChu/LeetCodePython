# 
# Given an integer array nums, 
# return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 

from typing import List
import pdb

solution_json = {
    "date": "2021/4/17",
    "coding": 64,
    "runtime": "9296 ms",
    "memory": "603.2 MB"
}

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        hash = {}  # h[v][idx] = True
        for i in range(n):
            v = nums[i]
            if v not in hash:
                hash[v] = {}
            if i not in hash[v]:
                hash[v][i] = True

        #print(hash)

        handled = {}
        out_ls = []
        for i in range(n-2):
            v = nums[i]
            del hash[v][i]
            if len(hash[v]) == 0:
                del hash[v]

            v2 = 0 - v
            #print(i, v, v2)
            two_sum_ls = self.twoSum(i+1, hash, nums, v2, handled)
            #print(i, v, v2, two_sum_ls)
            #pdb.set_trace()        
            if two_sum_ls != []:
                for two_sum in two_sum_ls:
                    out = [v] + two_sum
                    out.sort()
                    if out not in out_ls:
                        out_ls.append(out)

        #pdb.set_trace()
        return out_ls

    def twoSum(self, start, hash, nums, target, handled):
        out_ls = []

        n = len(nums)
        seen = {}
        for i in range(start, n):
            v = nums[i]
            if v in seen:
                continue
            seen[v] = i    

            v2 = target - v
            params = [target, v, v2]
            params.sort()
            params = tuple(params)
            if params in handled:
                continue

            handled[params] = True

            if v2 in hash:
                idx_ls = [*hash[v2]]
                if len(idx_ls) >= 2:
                    out = [v, v2]
                    out_ls.append(out)
                elif len(idx_ls) == 1: 
                    if idx_ls[0] != i:
                        out = [v, v2]
                        out.sort()
                        if out not in out_ls:
                            out_ls.append(out)
                else:
                    assert False

            #print(target, v, v2)
            #pdb.set_trace()

        #print(out_ls)
        return out_ls

