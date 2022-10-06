#
# https://leetcode.com/problems/reverse-string/
#
# Write a function that reverses a string. The input string is given as an array 
# of characters s.
#
# You must do this by modifying the input array in-place with O(1) extra memory.
#
# Example 1:
#       Input: s = ["h","e","l","l","o"]
#       Output: ["o","l","l","e","h"]
#
# Example 2: 
#       Input: s = ["H","a","n","n","a","h"]
#       Output: ["h","a","n","n","a","H"]
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/6",
    "design": 0,
    "coding": 0,
    "runtime": "463 ms",
    "fasterThan": "26%",
    "memory": "42.7 MB" 
}


'''
      0 1 2 3 4
      h e l l o
      0       4
        1   3
          2

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def reverseString(self, s: List[str]) -> None:
        func(s, 0, len(s) - 1)
        #br()

def func(s, i, j):
    if i >= j:
        return

    s[i], s[j] = s[j], s[i]
    i += 1 
    j -= 1
    func(s, i, j)


