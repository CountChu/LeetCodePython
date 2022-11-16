#
# https://leetcode.com/problems/generate-parentheses/
#
# Given n pairs of parentheses, write a function to generate all combinations 
# of well-formed parentheses.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/6",
    "design": 0,
    "coding": 17,
    "runtime": "40 ms",
    "fasterThan": "88%",
    "memory": "14.3 MB" 
}

'''
    n = 1:   ()
    n = 2:   ()()   (())     ()()
    n = 3:  
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def generateParenthesis(self, n: int) -> List[str]:
        dp = {}
        dp[1] = ['()']
        for i in range(1, n):
            #print(i+1, i)
            dp[i+1] = gen(dp[i])

        return dp[n]

def gen(ls):
    out = set()
    for s in ls:
        s_ls = list(s)
        s_ls = gen_one(s_ls)
        for s1 in s_ls:
            out.add(s1)
    return list(out)

def gen_one(s_ls):
    out = set()
    n = len(s_ls)
    for i in range(0, n+1):
        new_s_ls = s_ls.copy()
        new_s_ls.insert(i, '()')
        s = ''.join(new_s_ls)
        out.add(s)

    return out




