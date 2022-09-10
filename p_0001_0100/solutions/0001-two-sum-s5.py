from typing import List
import pdb

solution_json = {
    "date": "2022/8/27",
    "coding": -1,
    "runtime": "71 ms",
    "fasterThan": "87%",
    "memory": "15.2 MB"
}

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #print('target =', target)
        h = {}
        for i, num in enumerate(nums):
            h[num] = i

        for i, num in enumerate(nums):
            target2 = target - num
            if target2 in h:
                idx = h[target2]
                if i == idx:
                    continue
                return [i, idx]

        return None
