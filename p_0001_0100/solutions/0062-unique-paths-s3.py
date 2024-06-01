solution_json = {
    "date": "2023/12/30",
    "design": 0,
    "coding": 2,
    "runtime": "65 ms",
    "fasterThan": "5%",
    "memory": "17.26 MB"
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
    Input: m = 3, n = 7
    Output: 28

        d d  r r r r r r 

        2d 6r

        c(8, 2) = 8 * 7 / 2! = 28        

'''

def c(a, b):
    aa = 1
    bb = 1
    for i in range(b):
        #lg(a - i, b - i)
        aa = aa * (a - i)
        bb = bb * (b - i)
        #lg(aa, bb)

    return aa // bb

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def uniquePaths(self, m: int, n: int) -> int:
        a = m - 1
        b = n - 1
        out = c(a + b, min(a, b))
        return out    
