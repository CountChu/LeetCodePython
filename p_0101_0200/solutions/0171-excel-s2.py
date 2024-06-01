solution_json = {
    "date": "2023/12/24",
    "design": 0,
    "coding": 5,
    "runtime": "43 ms",
    "fasterThan": "38%",
    "memory": "17.16 MB"
}

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
lg = print

'''
    Input: columnTitle = "ZY"
    Output: 701

        Z -> 26
        Y -> 25
        26 * 26 + 25

        0 1
        Z Y

i=0     26
i=1     26 * 26 + 25 

'''

def build_table():
    h = {}
    for i in range(65, 65+26):
        #lg(chr(i))
        h[chr(i)] = i - 64

    return h

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def titleToNumber(self, columnTitle: str) -> int:
        h = build_table()
        s = columnTitle 
        n = len(s)
        out = 0
        for i in range(n):
            c = s[i]
            out = out * 26
            out += h[c]
        return out