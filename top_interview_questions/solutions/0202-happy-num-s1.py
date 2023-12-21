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

solution_json = {
    "date": "2023/12/9",
    "design": 0,
    "coding": 0,
    "runtime": "33 ms",
    "fasterThan": "95%",
    "memory": "16.5 MB" 
}

'''
    19   -> 9, 1

    2 -> 4
    4 -> 1 6 -> 3 7 -> 5 8
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

def cal(ls):
    out = 0
    for v in ls:
        out += v * v
    return out

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isHappy(self, n: int) -> bool:
       
        seen = set()
        while True:
            ls = split(n)
            n = cal(ls)
            if n in seen:
                return False 
            else:
                seen.add(n)

            #print(ls, n)
            if n == 1:
                return True

        pass

     
