#
# Given an integer n, return the number of prime numbers that are strictly 
# less than n.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/8",
    "design": 0,
    "coding": 18,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB",
    "bug": "Time Limit Exceeded" 
}

'''
        n = 15
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
         x  x
x = 2          v     x     x     x     x       x       x
x = 3             v        x        x          x         
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def countPrimes(self, n: int) -> int:
        if n == 0:
            return 0
        
        if n == 1:
            return 0

        if n == 2:
            return 0

        p_ls = [True] * (n)
        p_ls[0] = False
        p_ls[1] = False
        p_ls[2] = True
        
        x = 2
        while True:
            if x*x > n:
                break

            if not p_ls[x]:
                x += 1                
                continue

            mark(p_ls, x)
            print('x = %d' % x)
            x += 1

        out = 0
        for p in p_ls:
            if p:
                out += 1

        return out

def mark(p_ls, x):
    acc_x = x
    while True:
        acc_x += x
        #print('acc_x = %d' % acc_x)
        if acc_x >= len(p_ls):
            break

        p_ls[acc_x] = False

