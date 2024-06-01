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
    "date": "2022/11/2",
    "design": 0,
    "coding": 8,
    "runtime": "34 ms",
    "fasterThan": "95%",
    "memory": "13.9 MB" 
}

'''
    19 
    19 % 10 = 9
    19 // 10 = 1
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isHappy(self, n: int) -> bool:
        seen = set()
        while True:
            if n == 1:
                return True

            d_ls = split_num(n)
            n = sum_square(d_ls)
            if n in seen:
                return False

            seen.add(n)
            #print(n)
        
        return False

def split_num(n): 
    d_ls = []
    while True:
        if n == 0:
            break
        d = n % 10
        d_ls.append(d)
        n = n // 10 
    
    return d_ls

def sum_square(d_ls):
    out = 0
    for d in d_ls:
        out += d * d 
    return out




     
