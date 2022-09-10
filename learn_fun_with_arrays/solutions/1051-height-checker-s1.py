from typing import List
import pdb

solution_json = {
    "date": "2021/4/29",
    "design": 0,
    "coding": 2,
    "runtime": "36 ms",
    "memory": "14.2 MB"      
}

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
