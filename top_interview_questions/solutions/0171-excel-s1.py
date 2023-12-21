#
# https://leetcode.com/problems/excel-sheet-column-number/
#
# Given a string columnTitle that represents the column title as appears 
# in an Excel sheet, return its corresponding column number.
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2023/12/7",
    "design": 0,
    "coding": 0,
    "runtime": "41 ms",
    "fasterThan": "50%",
    "memory": "16.38 MB" 
}

'''
    out = 0
    0  1
    A  B   
    out *= 26
    out += 1
       out *= 26
       out += 2
'''

def get_num(C):
    return ord(C) - ord('A') + 1

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def titleToNumber(self, columnTitle: str) -> int:
        t = columnTitle
        out = 0
        n = len(t)
        for i in range(n):
            out *= 26
            out += get_num(t[i])

        return out
      
