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
    "date": "2023/12/7",
    "design": 0,
    "coding": 0,
    "runtime": "56 ms",
    "fasterThan": "5.42",
    "memory": "16.37 MB" 
}

'''
    bin(10) = '0b1010'
    int('1010', 2) = 10
    
        0. 1. 2. 3. 4. 5. 6. 7. ....... 31

        out = 0
    n = 0  1  0  1  0  0  0  0
        out = 0 
           out += 2**1 
                 out += 2**3


'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def reverseBits(self, n: int) -> int:
        b_ls = [0] * 32
        for i in range(32):
            #print(n % 2)
            b_ls[31 - i] = n % 2
            n = n // 2

        out = 0
        for i in range(len(b_ls)):
            if b_ls[i] == 1:
                out += 2**i

        return out