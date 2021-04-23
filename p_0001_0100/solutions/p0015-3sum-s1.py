from typing import List
import pdb

#
# 2021/4/17: Runtime: 920 ms, Memory: 17.3 MB
#

class Solution:

    #
    # Runtime: 960
    #

    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        ans = []

        for first in range(n):
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            third = n - 1
            target = -nums[first]
            self.twoSum(nums, first, third, target, ans)


        return ans    

    def twoSum(self, nums, first, third, target, ans):
        for second in range(first + 1, len(nums)):
            if second > first + 1 and nums[second] == nums[second - 1]:
                continue
            while second < third and nums[second] + nums[third] > target:
                third -= 1
            if second == third:
                break
            if nums[second] + nums[third] == target:
                ans.append([nums[first], nums[second], nums[third]])    
    
    #
    # Runtime: 920
    #

    def threeSum__(self, nums):
    	n = len(nums)
    	nums.sort()
    	ans = []

    	for first in range(n):
    		if first > 0 and nums[first] == nums[first - 1]:
    			continue
    		third = n - 1
    		target = -nums[first]
    		for second in range(first + 1, n):
    			if second > first + 1 and nums[second] == nums[second - 1]:
    				continue
    			while second < third and nums[second] + nums[third] > target:
    				third -= 1
    			if second == third:
    				break
    			if nums[second] + nums[third] == target:
    				ans.append([nums[first], nums[second], nums[third]])	

    	return ans