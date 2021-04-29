from typing import List
import pdb

#
# 2021/4/29: 0 min, 5 mins, 364 ms, 25.2 MB
#

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        d = False
        out = []
        v = nums
        n = len(v)

        hash = {}
        for i in range(n):
            if v[i] not in hash:
                hash[v[i]] = True

        ls = [i for i in range(1, n+1)]

        if d:
            print('ls = %s' % ls)

        for i in range(n):
            if ls[i] not in hash:
                out.append(ls[i])

        #pdb.set_trace()
        return out