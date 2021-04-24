from typing import List
import pdb

#
# 2021/4/24: 8 mins, runtime: 44 ms, memory: 14.6 MB
#

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = True

        n = len(nums)
        hash = {}
        for i in range(n):
            v = nums[i]
            if d:
                print(i, v)
            hash[v] = i

        if d:
            print('hash = %s' % hash)
            print('i, v, v2')


        for i in range(n):
            v = nums[i]
            v2 = target - v
            if d:
                print('%d, %5d, %5d' % (i, v, v2))
            
            if v2 in hash:
                j = hash[v2]
                if d:
                    print('        j = %d' % j)
                if i != j:
                    return [i, j]

        return [-1, -1]
