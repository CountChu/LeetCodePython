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

solution_json = {
    "date": "2022/11/2",
    "design": 0,
    "coding": 13,
    "runtime": "67 ms",
    "fasterThan": "33%",
    "memory": "13.9 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def reverseBits(self, n: int) -> int:
        #print('n = %d' % n)
        b_ls = [0] * 32
        idx = 0
        while True:
            if n == 0:
                break

            b = n % 2
            b_ls[idx] = b
            idx += 1

            #print(b)
            n = n // 2

        v = 0
        for b in b_ls:
            if v == None:
                if b == 1:
                    v = 1
            else:
                v = v * 2 + b

        return v

  