#
# https://leetcode.com/problems/k-th-symbol-in-grammar/
#
# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. 
# Now in every subsequent row, we look at the previous row 
# and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.
#
# 0 -> 01
# 1 -> 10
#
# n = 3      1 2 3 4   
#   row 1:   0
#   row 2:   0 1
#   row 3:   0 1 1 0  
#
# Example 1:
#       Input: n = 1, k = 1
#       Output: 0
#
# Example 2: 
#       Input: n = 2, k = 1
#       Output: 0
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/?/??",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def kthGrammar(self, n: int, k: int) -> int:
        pass
