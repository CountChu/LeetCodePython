from typing import List
import pdb

solution_json = {
    "date": "2021/4/25",
    "coding": 4,
    "runtime": "416 ms",
    "fasterThan": "28.94%",
    "memory": "17.6 MB"         
}

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        out = []
        for i in range(n):
        	v1 = nums[i]
        	v2 = v1 * v1
        	out.append(v2)

        out.sort()	
        return out
