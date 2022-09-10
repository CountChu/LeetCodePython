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

solution_json = {
    "date": "2022/8/31",
    "design": 0,
    "coding": 0,
    "runtime": "112 ms",
    "fasterThan": "55%",
    "memory": "16.4 MB" 
}

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:

        tmp = []
        i = 0
        while True:
            if arr[i] == 0:
                tmp += [0, 0]
            else:
                tmp.append(arr[i])
            if len(tmp) >= len(arr):
                break
            i += 1

        for i in range(len(arr)):
            arr[i] = tmp[i]
