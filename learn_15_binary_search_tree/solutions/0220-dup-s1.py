from typing import List
import sys
import pdb

solution_json = {
    "date": "2021/5/8",
    "bug": "Time Limit Exceeded"    
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        d = False        
        v = nums
        n = len(v)


        out = False
        for i in range(n - 1):
            for j in range(i + 1, n):
                if d:
                    print(i, j)
                if abs(v[i] - v[j]) <= t and abs(i - j) <= k:
                    out = True
                    break
            if out == True:
                break
                    
        return out
