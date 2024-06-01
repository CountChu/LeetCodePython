#
# https://leetcode.com/problems/decode-ways/
#
# A message containing letters from A-Z can be encoded into numbers 
# using the following mapping:
#
#       'A' -> "1"
#       'B' -> "2"
#       ...
#       'Z' -> "26"
# 
# To decode an encoded message, all the digits must be grouped then mapped back 
# into letters using the reverse of the mapping above (there may be multiple ways). 
# For example, "11106" can be mapped into:
#
#       "AAJF" with the grouping (1 1 10 6)
#       "KJF" with the grouping (11 10 6)
#
# Note that the grouping (1 11 06) is invalid because "06" cannot be mapped 
# into 'F' since "6" is different from "06".
#
# Given a string s containing only digits, return the number of ways to decode it.
#
# The test cases are generated so that the answer fits in a 32-bit integer.
#


from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

solution_json = {
    "date": "2023/11/30",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB", 
    "bug": "Time Limit Exceeded"
}

'''
    A, B, C, D, E, F, G, H, I,  J,  K,  L,  M,  N,  O,  P,  Q,  R,  S,  T,  U,  V,  W,  X,  Y,  Z    
    1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26

     0 1 2 3
    [2 1 2 6]

    0, '2126'
        1, '126'
            2, '26'
                3, '6'
        2, '26'  x 
'''

def go(nums, s, n, i, ctx):
    lg(i, s[i:])

    if s[i] in nums:

        if i == n - 1:
            ctx['out'] += 1
            return

        lg('call 1')
        go(nums, s, n, i+1, ctx)

    if i <= n - 2 and s[i:i+2] in nums:

        if i == n - 2:
            ctx['out'] += 1
            return

        lg('call 2')
        go(nums, s, n, i+2, ctx)

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def numDecodings(self, s: str) -> int:  
        nums_0 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26}
        nums = set()
        for num in nums_0:
            nums.add(str(num))

        n = len(s)

        i = 0 
        ctx = {'out': 0}
        go(nums, s, n, i, ctx)
 
        return ctx['out']


