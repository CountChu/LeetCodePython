from typing import List
import pdb

#
# 2021/4/22: 11 mins, runtime: 36 ms, memory: 14.3 MB
#

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
    	d = False

    	n = len(nums)
    	i = 0
    	while True:
    		if i == n:
    			break

    		num = nums[i]

    		if d:
    			print(i, num)

    		if num == val:
    			for j in range(i+1, n):
    				nums[j-1] = nums[j]
    			n -= 1	
    			if d:
    				print(nums)
    		else:
    			i += 1
    		
    	return n