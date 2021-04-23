from typing import List
import pdb

#
# 2021/4/29: 11 mins, Reuntime: 64 ms, Memory: 16.4 MB
#

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        debug = False

        sum0 = None
        sum1 = None
        max_sum = None
        n = len(nums)
        for i in range(n):
        	v = nums[i]

        	if sum1 == None:
        		sum1 = v
        	else:
        		if sum0 < 0:
        			sum1 = v
        		else:
        			sum1 += v 

        	if max_sum == None:
        		max_sum = sum1
        	else:
        		if max_sum < sum1:
        			max_sum = sum1

        	if debug:
        		if sum0 == None:
        			sum0_str = 'None'
        		else:
        			sum0_str = '%d' % sum0
        		print('i = %3d, v = %3d, sum0 = %3s, sum1 = %3d' % (i, v, sum0_str, sum1))


        	sum0 = sum1

        return max_sum
