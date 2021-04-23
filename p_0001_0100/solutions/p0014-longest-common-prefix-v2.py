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
# 2021/4/13: 23 mins.
#

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_n = None
        for str in strs:
            if min_n == None:
                min_n = len(str)
            elif min_n > len(str):
                min_n = len(str)
                
        if min_n == None:
            return ''

        out = ''
        same = True
        for i in range(min_n):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    same = False
                    break
            if same:
                out += strs[0][i]
            else:
                break
        
        return out