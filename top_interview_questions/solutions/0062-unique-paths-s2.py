solution_json = {
    "date": "2023/12/15",
    "design": 0,
    "coding": 13,
    "runtime": "46 ms",
    "fasterThan": "13%",
    "memory": "16.23 MB"
}

#
# https://leetcode.com/problems/unique-paths/
#
# There is a robot on an m x n grid. The robot is initially located 
# at the top-left corner (i.e., grid[0][0]). The robot tries to move 
# to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only 
# move either down or right at any point in time.
#
# Given the two integers m and n, return the number of possible unique paths 
# that the robot can take to reach the bottom-right corner.
#
# The test cases are generated so that the answer will be less than or equal 
# to 2 * 109.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
         1 2 3 4 5 6 7        
     
     1   . . . . . . .
     2   . . . . . . .
     3   . . . . . . .
        
    r r r r r r t t
    t t r r r r r r

    C(8, 2) = C(8, 6)

    8 * 7 / 2 * 1

'''

def C(a, b):
    aa = 1
    bb = 1
    for i in range(b):
        aa = aa * (a - i)
        bb = bb * (b - i)

    return aa // bb

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def uniquePaths(self, m: int, n: int) -> int:
        a = m - 1
        b = n - 1
        c = a + b
        a = min(a, b)
        out = C(c, a)
        return out    
