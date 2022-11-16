#
# https://leetcode.com/problems/container-with-most-water/
#
# You are given an integer array height of length n. There are n vertical lines 
# drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# 
# Find two lines that together with the x-axis form a container, such that 
# the container contains the most water.
#
# Return the maximum amount of water a container can store.
#
# Notice that you may not slant the container.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/5",
    "design": 0,
    "coding": 6,
    "runtime": "2171 ms",
    "fasterThan": "12%",
    "memory": "27.4 MB" 
}

'''
     0  1  2  3  4  5  6  7  8
    [1, 8, 6, 2, 5, 4, 8, 3, 7]
        .                    .

        (8 - 1) * 7

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def maxArea(self, height: List[int]) -> int:
        out = 0

        i = 0
        j = len(height) - 1
        while True:
            if i > j:
                break

            area = get_area(height, i, j)
            #print(i, j, area)
            out = max(out, area)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return out

def get_area(height, i, j):
    out = (j - i) * min(height[i], height[j])
    return out
     
