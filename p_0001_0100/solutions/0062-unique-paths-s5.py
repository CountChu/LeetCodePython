solution_json = {
    "date": "2024/1/15",
    "design": 0,
    "coding": 6,
    "runtime": "33 ms",
    "fasterThan": "87%",
    "memory": "17.38 MB"
}

#
# https://leetcode.com/problems/unique-paths/
#
# Medium.
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
#lg = print

'''
    Input: m = 3, n = 7
    Output: 28

        D D R R R R R R
        a = 2, b = 6
        C(a+b, min(a, b)) = C(8, 2) = 8 * 7 / 2 = 28

'''

'''
    C(8, 2)

        i = 0: a = 8, b = 2
        i = 1: a = 7, b = 1

'''

def C(a, b):
    aa = 1
    bb = 1
    for i in range(b):
        #lg(i, a - i, b - i)
        aa = aa * (a - i)
        bb = bb * (b - i)
    
    return aa//bb

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def uniquePaths(self, m: int, n: int) -> int:
        a = m - 1
        b = n - 1
        out = C(a+b, min(a, b))
        return out