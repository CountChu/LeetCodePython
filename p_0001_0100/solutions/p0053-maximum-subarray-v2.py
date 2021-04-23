from typing import List
import pdb

#
# 2021/4/19: Time Limit Exceeded
#

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        debug = False

        #
        # if i > 1,  sum(i, j) = sum(0, j) - sum(0, i - 1)
        # if i == 0, sum(0, j) = sum(0, j-1) + [j]
        # if i == 0 and j == 0, sum(0, 0) = [0]
        #   

        sum = {} # sum[(i, j)] = sum(nums, i, j)
        def dp(i, j):

            assert (i, j) not in sum

            if i == 0 and j == 0:
                sum[(0, 0)] = nums[0]
            elif i == 0 and j >= 1:
                sum[(0, j)] = sum[(0, j - 1)] + nums[j]
            elif i >= 1 and j >= 1:
                sum[(i, j)] = sum[(0, j)] - sum[(0, i - 1)]
            else:
                assert False

            return sum[(i, j)]

        max_sum = None

        n = len(nums)
        for i in range(n):
            for j in range(i, n):
                    
                the_sum = dp(i, j)
                if debug:
                    print(i, j, the_sum)
                
                if max_sum == None:
                    max_sum = the_sum
                elif max_sum < the_sum:
                    max_sum = the_sum

        if debug:
            print('max_sum = %d' % max_sum)

        return max_sum





