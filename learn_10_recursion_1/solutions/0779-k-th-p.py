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
    "date": "2022/10/6",
    "design": 0,
    "coding": 0,
    "runtime": "44 ms",
    "fasterThan": "69.8",
    "memory": "13.9 MB" 
}

'''
                    1 2 3 4 5 6 7 8
                    0 1 2 3 4 5 6 7
        row 1   1   0
        row 2   2   0 1
        row 3   4   0 1 1 0
        row 4   8   0 1 1 0 1 0 0 1

    n = 4 -> 8, k = 6 -> 5
             4           5 % 4 = 2

             8, k = 7 -> 6
             4           6 % 4 = 2
             2           2 % 2 = 0 
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def kthGrammar(self, n: int, k: int) -> int:
        if k == 1:
            return 0

        k_set = set()
        k -= 1
        w = 2**(n-1)
        print(w, k)
        k_set.add(k)

        while True:
            w = w // 2
            k = k % w
            print(w, k)
            k_set.add(k)
            if k == 0:
                break
        
        out = 1
        if len(k_set) % 2 == 1:
            out = 0    

        return out





