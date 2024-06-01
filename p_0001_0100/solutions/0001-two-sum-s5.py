from typing import List
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/8/27",
    "again": ["2022/10/31"],
    "coding": -1,
    "runtime": "59 ms",
    "fasterThan": "97%",
    "memory": "15.1 MB"
}

'''
     0  1  2  3
    [2, 5, 5, 11], 10

    h[2] = 0
    h[5] = 2 
    h[11] = 3


'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, v in enumerate(nums):
            h[v] = i
        
        for idx0, v0 in enumerate(nums):
            v1 = target - v0
            if v1 in h:
                idx1 = h[v1]
                if idx0 == idx1:
                    continue

                return [idx0, idx1]

        return []
