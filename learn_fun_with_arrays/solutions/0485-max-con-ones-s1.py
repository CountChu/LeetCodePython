from typing import List
import pdb

solution_json = {
    "date": "2021/4/25",
    "design": 2,
    "coding": 6,
    "runtime": "390 ms",
    "fasterThan": "80%",
    "memory": "14.2 MB"       
}

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        d = False

        n = len(nums)

        i = 0
        j = 0
        w = []
        out = 0
        while True:
            if nums[j] == 1:
                w.append(1)
                if d:
                    print(i, j, w)
                if out < len(w):
                    out = len(w)
                j += 1
            else:
                w = []
                if d:
                    print(i, j, w)
                i += 1
                j += 1

            if j == n:
                break

        #pdb.set_trace() 
        return out


