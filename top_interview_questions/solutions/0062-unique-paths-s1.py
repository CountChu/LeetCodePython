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
    "date": "2023/11/28",
    "design": 0,
    "coding": 0,
    "runtime": "38 ms",
    "fasterThan": "62%",
    "memory": "16.38 MB" 
}

'''

       0 1 2 3 4 5 6

    0  s . . . . . .
    1  . . . . . . .
    2  . . . . . . f

    m = 3, n = 7

    2 x 6

    r r r r r r d d

    8! / (2! * 6!)     

    C(8, 6) ---> C(8, 2)
    C(8, 2) ---> 8 * 7 / 2!


'''

def C(a, b):
    out = a
    for i in range(1, b):
        out = out * (a - i)
        #print(out)
    #print('...')

    for i in range(b):
        out = out // (b - i)
        #print(out)

    #br()

    return out


class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def uniquePaths(self, m: int, n: int) -> int:
        a = m - 1 
        b = n - 1

        if a == 0 and b == 0:
            return 1
        
        if a == 0 and b >= 1:
            return 1

        if b == 0 and a >= 1:
            return 1

        out = C(a + b, a)
        return out
    
