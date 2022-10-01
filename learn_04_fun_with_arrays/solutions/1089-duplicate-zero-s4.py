#
# https://leetcode.com/problems/duplicate-zeros/
#
# Given a fixed-length integer array arr, duplicate each occurrence of zero, 
# shifting the remaining elements to the right.
#
# Example 1:
#       Input: arr = [1,0,2,3,0,4,5,0]
#       Output: [1,0,0,2,3,0,0,4]
#
# Example 2:
#       Input: arr = [1,2,3]
#       Output: [1,2,3]
#

from typing import List
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/1",
    "design": 0,
    "coding": 0,
    "runtime": "75 ms",
    "fasterThan": "91%",
    "memory": "14.7 MB" 
}

'''
    [1, 0, 2, 3, 0, 4, 5, 0]
    [1, 0, 0, 2, 3, 0, 0, 4]
'''

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        out = []
        n = len(arr)
        acc = 0
        for v in arr:
            out.append(v)
            acc += 1
            if acc == n:
                break 
            if v == 0:
                out.append(0)
                acc += 1
                if acc == n:
                    break

        for i in range(n):
            arr[i] = out[i]


