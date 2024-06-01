solution_json = {
    "date": "2023/12/21",
    "design": 0,
    "coding": 42,
    "runtime": "511 ms",
    "fasterThan": "98%",
    "memory": "32.49 MB"
}

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
lg = print

'''
    aab:
        aab
        a, ab
            a, a, b
        aa, b

    ('aab')
        aab
        1, a, ab
        ('ab')
            ab
            1, a, b
        2, aa, b

'''

def go(s, level, path, ls_ls):
    #lg('%s%s, %s' % ('    '*level, s, path))
    n = len(s)
    for i in range(1, n):
        s0 = s[:i]
        s1 = s[i:]
        #lg('%s%s, %s' % ('    '*level, s0, s1))
        path.append(s0)
        ls_ls.append(path+[s1])
        go(s1, level+1, path, ls_ls)
        path.pop()

def is_pali(s):
    n = len(s)
    i = 0
    j = n - 1
    while True:
        if i > j:
            break 
        if s[i] != s[j]:
            return False 
        i += 1
        j -= 1
    return True

def all_pali(ls):
    for s in ls:
        if not is_pali(s):
            return False
    return True

def filter(ls_ls):
    out = []
    for ls in ls_ls:
        if all_pali(ls):
            out.append(ls)
    return out

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def partition(self, s: str) -> List[List[str]]:
        path = []
        ls_ls = [[s]]
        go(s, 0, path, ls_ls)
        out = filter(ls_ls)
        return out




