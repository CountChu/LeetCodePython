solution_json = {
    "date": "2023/12/25",
    "design": 0,
    "coding": 5,
    "runtime": "33 ms",
    "fasterThan": "94%",
    "memory": "17 MB"
}

#
# https://leetcode.com/problems/happy-number/
#
# Write an algorithm to determine if a number n is happy.
#
# A happy number is a number defined by the following process:
#
#       Starting with any positive integer, replace the number by the sum 
#       of the squares of its digits.
# 
#       Repeat the process until the number equals 1 (where it will stay), 
#       or it loops endlessly in a cycle which does not include 1.
#
#       Those numbers for which this process ends in 1 are happy.
#
# Return true if n is a happy number, and false if not.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    19
    1**2 + 9**2 = 82
    8**2 + 2**2 = 68
    6**2 + 8**2 = 100
    1**2 + 0**2 + 0**2 = 1
'''

def split(n):
    out = []
    while True:
        if n == 0:
            break
        r = n % 10
        out.append(r)
        n = n // 10
    return out

def sqr_sum(ls):
    out = 0
    for v in ls:
        out += v**2
    return out

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isHappy(self, n: int) -> bool:
        
        vis = set()
        while True:
            if n == 1:
                return True

            if n in vis:
                return False

            vis.add(n)
            ls = split(n) 
            n = sqr_sum(ls)

        return False
     
