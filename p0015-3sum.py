# 
# Given an integer array nums, 
# return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
# 

from typing import List
import pdb

#
# 2021/4/13: 18 + 8 mins 
#

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        hash = {}  # hash[num] = idx_ls
        
        n = len(nums)
        for i in range(n):
            num = nums[i]
            if num not in hash:
                hash[num] = []
            hash[num].append(i)
        #print(hash)
        #pdb.set_trace()
        
        out_ls = []
        pair_ls = []
        for i in range(0, n-1):
            for j in range(i + 1, n):
                pair = [nums[i], nums[j]]
                pair.sort()
                if pair in pair_ls:
                    continue
                pair_ls.append(pair)    
                sum = nums[i] + nums[j]
                find_num = -sum
                if find_num in hash:
                    idx_ls = hash[find_num]
                    idx_ls2 = idx_ls.copy()
                    if i in idx_ls2:
                        idx_ls2.remove(i)
                    if j in idx_ls2:
                        idx_ls2.remove(j)
                    if len(idx_ls2) >= 1:    
                        out = [nums[i], nums[j], find_num]

                        out.sort()
                        if out not in out_ls:
                            out_ls.append(out)
                #print(i, j, nums[i], nums[j])

        #pdb.set_trace()
        return out_ls
