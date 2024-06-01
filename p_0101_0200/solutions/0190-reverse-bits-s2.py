solution_json = {
    "date": "2023/12/24",
    "design": 0,
    "coding": 9,
    "runtime": "33 ms",
    "fasterThan": "90%",
    "memory": "17.27 MB"
}

#
# https://leetcode.com/problems/reverse-bits/
#
# Reverse bits of a given 32 bits unsigned integer.
#
# Note:
# ...
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    Input: n = 00000010100101000001111010011100
    Output:    964176192 (00111001011110000010100101000000)
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def reverseBits(self, n: int) -> int:
        #lg(n)
        ls = [0] * 32
        i = 0
        while True:
            if n == 0:
                break

            r = n % 2
            ls[i] = r
            i += 1
            n = n // 2

        out = 0
        j = 0
        for i in reversed(range(len(ls))):
            if ls[i] == 1:
                out += 2**j
            j += 1

        return out
  