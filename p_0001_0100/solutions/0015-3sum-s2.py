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
    "coding": 22,
    "runtime": "6812 ms",
    "memory": "18 MB"
}

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        out_ls = []
        for i in range(0, n-2):
            v = nums[i]
            
            v2 = 0 - v
            two_sum_ls = self.twoSum(nums[i+1:], v2)
            if two_sum_ls == []:
                continue

            for two_sum in two_sum_ls:
                out = [v] + two_sum
                out.sort()
                if out not in out_ls:
                    out_ls.append(out)

            #print(i, v, v2)
        return out_ls

    def twoSum(self, nums, target):
        print(target)
        n = len(nums)   
        hash = {}
        out_ls = [] 
        for i in range(n):
            v = nums[i]
            v2 = target - v
            if v2 in hash:
                out_ls.append([v, v2])
            else:
                hash[v] = i    
            #print(i, v)
        #pdb.set_trace()    
        return out_ls    