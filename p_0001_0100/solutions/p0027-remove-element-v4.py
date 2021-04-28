from typing import List
import pdb

#
# 2021/4/25: 5 mins, 10 mins, 44 ms, 15.4 MB
#

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        d = True

        v = nums
        n = len(v)
        i = 0
        j = 0

        for j in range(n):
            if d:
                print(i, j, v[j])

            if v[j] != val:
                v[i] = v[j]
                if d:
                    print('        ', v)
                i += 1

        return i
        #pdb.set_trace()