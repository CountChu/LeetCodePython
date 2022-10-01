#
# https://leetcode.com/problems/check-if-n-and-its-double-exist/
#
# Given an array arr of integers, check if there exists two integers N and M 
# such that N is the double of M ( i.e. N = 2 * M).
#
# Example 1:
#       Input: arr = [10, 2, 5, 3]
#       Output: true
#
# Example 2:
#       Input: arr = [7, 1, 14, 11]
#       Output: true
#
# Example 3:
#       Input: arr = [3, 1, 7, 11]
#       Output: false
#

from typing import List
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/1",
    "design": 0,
    "coding": 0,
    "runtime": "66 ms",
    "fasterThan": "85%",
    "memory": "13.9 MB" 
}

class Solution:

    """
          0  1  2  3  : idx
        [10, 2, 5, 3] = arr
        
          0
        [10] -> 20
             1
            [2] -> 4  
                2
               [5] -> 10
                   3
                   [3] -> 6 

    """
    def checkIfExist(self, arr: List[int]) -> bool:
        h = {}
        for i, v in enumerate(arr):
            if v == 0:
                if v in h:
                    return True
                h[v] = i
                continue

            if v not in h:
                h[v] = i  

            if v*2 in h: 
                return True
            
            if v % 2 == 0 and v // 2 in h:
                return True 
        
        return False





