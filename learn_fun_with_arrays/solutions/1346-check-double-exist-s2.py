#
# https://leetcode.com/problems/check-if-n-and-its-double-exist/
#
# Given an array arr of integers, check if there exists two integers N and M 
# such that N is the double of M ( i.e. N = 2 * M).
#
# Example 1:
#       Input: arr = [10,2,5,3]
#       Output: true
#
# Example 2:
#       Input: arr = [7,1,14,11]
#       Output: true
#
# Example 3:
#       Input: arr = [3,1,7,11]
#       Output: false
#

from typing import List
import pdb

solution_json = {
    "date": "2022/9/1",
    "design": 0,
    "coding": 0,
    "runtime": "97 ms",
    "fasterThan": "38%",
    "memory": "14 MB" 
}

br = pdb.set_trace

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        h = {}
        for i, v in enumerate(arr):
            if v == 0:
                if v in h:
                    return True

            if v not in h:
                h[v] = True

            if v != 0:
                v2 = 2 * v
                if v2 in h:
                    #br()
                    return True    

                if v % 2 == 0:
                    v3 = v // 2
                    if v3 in h:
                        #br()
                        return True 

        return False
