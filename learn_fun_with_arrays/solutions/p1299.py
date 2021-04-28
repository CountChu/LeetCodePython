from typing import List
import pdb

#
# 2021/4/28: 7 min, 11 min, Time Limit Exceeded
#

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        d = False
        out = []

        v = arr
        n = len(v)
        for i in range(n):
            max = -1
            for j in range(i+1, n):
                if max < v[j]:
                    max = v[j]
            out.append(max)

        #pdb.set_trace()
        return out

