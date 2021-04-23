from typing import List
import pdb

#
# 2021/4/17: 11 mins. Runtime: 4432 ms, Memory 14.4 MB
#

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        debug = False
        nums.sort()
        if debug:
            print('nums = %s' % nums)

        n = len(nums)
        min_diff = None
        out = None
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    s = nums[i] + nums[j] + nums[k]
                    if min_diff == None:
                        min_diff = abs(s - target)
                        out = s
                    else:
                        if min_diff > abs(s - target):
                            min_diff =  abs(s - target)
                            out = s
                    if debug:
                        print(i, j, k, min_diff, out)
                    if min_diff == 0:
                        return out

        return out
