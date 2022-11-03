#
# https://leetcode.com/problems/two-sum/
#
# Given an array of integers nums and an integer target, return indices 
# of the two numbers such that they add up to target.  
#

from typing import List
import pdb

solution_json = {
    "date": "2021/3/28",
    "coding": 5,
    "runtime": "56 ms",
    "memory": "14.6 MB"                    
}

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #print('target = %d' % target)
    
        hash = {}
        for i in range(len(nums)):
            num = nums[i]
            if num not in hash:
                hash[num] = []
            hash[num].append(i)
            if len(hash[num]) >= 2:
                if num * 2 == target:
                    return hash[num]
        
        #pdb.set_trace()
        for num in hash:
            num2 = target - num
            if num != num2:
                if num2 in hash:
                    if num + num2 == target:
                        return [hash[num][0], hash[num2][0]] 
        
        return None

