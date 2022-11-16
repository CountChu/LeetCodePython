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

solution_json = {
    "date": "2022/11/12",
    "design": 0,
    "coding": 12,
    "runtime": "59 ms",
    "fasterThan": "49%",
    "memory": "13.9 MB" 
}

'''
    s .
    . .
    . f

    r d d
    d d r
    d r d

    s . . . . . .
    . . . . . . .
    . . . . . . f

    m = 3, n = 7   -> (2, 6)

      r r r r r r d d   8 

    s . . .
    . . . .
    . . . .
    . . . f

      r r r d d d
      (6 * 5 * 4) / 3!


'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1:
            return 1

        a = m - 1
        b = n - 1
        #print(a, b)
        c = a + b
        a = min(a, b)
        #print('a = %d' % a)

        out = 1
        aa = 1
        for i in range(a):
            aa = aa * (i + 1)
            #print('i = %d' % i)
            out = out * c 
            #print(i, out)
            c -= 1
        out //= aa

        return out

