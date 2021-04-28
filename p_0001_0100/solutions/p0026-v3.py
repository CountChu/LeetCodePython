from typing import List
import pdb

#
# 2021/4/25: 19 mins, 15 mins, 80 ms, 17.3 MB
#

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = False

        v = nums
        n = len(v)
        j = 0
        if d:
            print('i, j, flag, v[:j+1]  --->  v, j')
        for i in range(n):
            if d:
                print(i, j, v[i] == v[j], v[:j+1])

            if v[i] != v[j]:
                j += 1
                v[j] = v[i]
                if d:
                    print('        ', v, j)

        return j + 1