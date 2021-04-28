from typing import List
import pdb

#
# 2021/4/28: 9 mins, 6 mins, 400 ms, 15.2 MB
#

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        d = False

        v = nums
        n = len(v)
        count = 0
        i = 0
        j = 1
        while True:
            if i == n - count:
                break

            if v[i] == 0:
                for j in range(i+1, n-count):
                    v[j-1] = v[j]
                count += 1
            else:
                i += 1

        for i in range(n - count, n):
            v[i] = 0

        #pdb.set_trace()




