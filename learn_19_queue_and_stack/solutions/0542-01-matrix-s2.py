#
# https://leetcode.com/problems/01-matrix/
#
# Given an m x n binary matrix mat, return the distance of the nearest 0 
# for each cell.
#
# The distance between two adjacent cells is 1.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/30",
    "design": 0,
    "coding": 0,
    "runtime": "640 ms",
    "fasterThan": "94%",
    "memory": "17.1 MB" 
}

'''
     0 1 2 3 4

  0  0 0 * * *
  1  0 * * * * 
  2  0 * * * *
  3  0 * * * 0

     0 0 1 2 3
     0 1 2 3 4 
     0 1 2 3 4 
     0 1 2 3 0


        <- 2 1
     0 1 2 1 0

'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        h = len(mat)
        w = len(mat[0])
        dp = [[10000 for x in range(w)] for y in range(h)]

        #
        # (Left, Top) ---> (Right ,Bottom)
        #

        for y in range(h):
            for x in range(w):
                if mat[y][x] == 0:
                    dp[y][x] = 0 
                else:
                    if x >= 1:
                        dp[y][x] = min(dp[y][x], dp[y][x-1] + 1) 
                    if y >= 1:
                        dp[y][x] = min(dp[y][x], dp[y-1][x] + 1)

        #
        # (Right ,Bottom) ---> (Left, Top)
        #

        for y in reversed(range(h)):
            for x in reversed(range(w)):
                if x <= w - 2:
                    dp[y][x] = min(dp[y][x], dp[y][x+1] + 1)
                if y <= h - 2:
                    dp[y][x] = min(dp[y][x], dp[y+1][x] + 1)

        #dump(dp)

        return dp

def dump(mat):
    for y in range(len(mat)):
        print(mat[y])
    print('----')



