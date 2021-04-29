from typing import List
import pdb

#
# 2019/4/29: 0 min, 2 mins, 36 ms, 14.2 MB
#

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        d = False
        v = heights.copy()
        n = len(v)
        v.sort()

        out = 0
        for i in range(n):
            if v[i] != heights[i]:
                out += 1 


        #pdb.set_trace()
        return out
