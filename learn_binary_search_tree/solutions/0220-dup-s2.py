from typing import List
import pdb

#
# 2021/5/8: 3, 7, 140 ms, 18.2 MB
#

solution_json = {
    "date": "2021/5/8",
    "design": 3,
    "coding": 7,
    "runtime": "140 ms",
    "memory": "18.2 MB"
}  

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        d = False        
        pair_ls = []
        for i in range(len(nums)):
            pair = (nums[i], i)
            pair_ls.append(pair)

        pair_ls.sort(key = lambda x: x[0])
        if d:
            for pair in pair_ls:
                print(pair)

        out = False
        n = len(pair_ls)
        for i in range(n - 1):
            v_i, idx_i = pair_ls[i]
            for j in range(i + 1, n):
                if d:
                    print(i, j)
                v_j, idx_j = pair_ls[j]
                if abs(v_i - v_j) <= t:
                    if abs(idx_i - idx_j) <= k:
                        out = True
                        break
                else:
                    break
            if out == True:
                break

        return out