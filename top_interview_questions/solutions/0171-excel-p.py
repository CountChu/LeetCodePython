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
    "date": "2022/11/2",
    "design": 0,
    "coding": 8,
    "runtime": "68 ms",
    "fasterThan": "31%",
    "memory": "14 MB" 
}

'''
         A      B 
    AB = 1*26 + 2
    
         Z       Y
    ZY = 26*26 + 25


         out = 26
         out = out * 26 + 25

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def titleToNumber(self, columnTitle: str) -> int:
        h = build_table()
        c = columnTitle[0]
        out = h[c]
        for i in range(1, len(columnTitle)):
            out = out * 26 + h[columnTitle[i]]

        return out

def build_table():
    h = {}
    for i in range(26):
        c = chr(65+i)
        h[c] = i + 1
        #print(c)
    
    return h
      
