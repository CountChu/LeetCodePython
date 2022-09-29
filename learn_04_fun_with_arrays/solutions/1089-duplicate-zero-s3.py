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
    "date": "2022/9/1",
    "design": 0,
    "coding": 0,
    "runtime": "86 ms",
    "fasterThan": "80.43%",
    "memory": "16.7 MB" 
}

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        size = len(arr)
        h = {}
        idx = 0
        zero_idx_ls = []
        for i in range(size):
            if arr[i] == 0:
                zero_idx_ls.append(idx)
                idx += 1
                if idx >= size:
                    break                
                zero_idx_ls.append(idx)
            

            if arr[i] != 0:
                h[i] = idx 

            idx += 1
            if idx >= size:
                break

        for i, j in reversed(h.items()):
            arr[j] = arr[i]

        for i in zero_idx_ls:   
            arr[i] = 0      
