#
# https://leetcode.com/problems/valid-mountain-array/
#
# Given an array of integers arr, return true if and only if it is a valid mountain array.
#
# Recall that arr is a mountain array if and only if:
#
#       - arr.length >= 3
#       - There exists some i with 0 < i < arr.length - 1 such that:
#           - arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
#           - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
#
# Example 1:
#       Input: arr = [2, 1]
#       Output: false
#
# Example 2: 
#       Input: arr = [3, 5, 5]
#       Output: false
#
# Example 3:
#       Input: arr = [0, 3, 2, 1]
#       Output: true
#
# Constraints
#       1 <= arr.length <= 10^4
#       0 <= arr[i] <= 10^4
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/1",
    "design": 0,
    "coding": 0,
    "runtime": "529 ms",
    "fasterThan": "13%",
    "memory": "15.5 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    '''
        [6, 7, 7, 8, 6]
         init
            up
               flat
                  up
                     down 
        [0, 3, 2, 1]
         init 
            up 
               down
                  down
    '''
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        assert n >= 1

        if n == 1:
            return False

        s = 'init'
        for i in range(1, n):
            if s == 'init':
                if arr[i-1] < arr[i]:
                    s = 'up'
                else:
                    return False 
            elif s == 'up':
                if arr[i-1] < arr[i]:
                    s = 'up'
                elif arr[i-1] > arr[i]:
                    s = 'down'
                else:
                    return False 
            elif s == 'down':
                if arr[i-1] > arr[i]:
                    s = 'down'
                else:
                    return False 
            else:
                return False

        if s != 'down':
            return False

        return True




