#
# https://leetcode.com/problems/palindrome-partitioning/
#
# Given a string s, partition s such that every substring of the partition 
# is a palindrome. Return all possible palindrome partitioning of s.
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/16",
    "design": 0,
    "coding": 0,
    "runtime": "685 ms",
    "fasterThan": "92",
    "memory": "32.4 MB" 
}

'''
    a a b
    

    [a]
        [a, a]
            [a, a, b]
            [a, ab]
        [aa]  
            [aa, b]
            [aab]


    e f e
    
    e
        e, f
            e, f, e
            e, fe
        ef
            ef, e
            efe
'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        ls_ls = []
        for i in range(n):
            ls_ls = go(s, i, ls_ls)
            #print(ls_ls)
        
        return ls_ls

def go(s, idx, ls_ls):
    c = s[idx]
    out = []

    if ls_ls == []:
        out = [[c]]
    else:
        for ls in ls_ls:
            new_ls = ls.copy()
            if is_pali(new_ls[-1]):
                new_ls.append(c)
                out.append(new_ls)

            new_ls = ls.copy()
            s2 = new_ls[-1] + c
            if idx == len(s) - 1:
                if is_pali(s2):
                    new_ls[-1] = s2
                    out.append(new_ls)
            else:
                new_ls[-1] = s2
                out.append(new_ls)

    return out

def is_pali(s):
    i = 0
    j = len(s) - 1
    while True:
        if i >= j:
            break

        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    return True



