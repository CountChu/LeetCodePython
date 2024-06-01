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
    "date": "2023/12/5",
    "design": 0,
    "coding": 0,
    "runtime": "644 ms",
    "fasterThan": "6%",
    "memory": "39.89 MB" 
}

'''
    aab
    p0: [a] [a] [b]
    p1: [aa] [b]

    0 1 2
    e f e

    p0: e | f | e
        ef | e
        e | fe
    p1: efe

    |  |
    0  0
    0  1
    1  0
    1  1

    0 1 2
    e f e

'''

lg = print

def gen(n):
    out = []
    for i in range(n):
        s = bin(n+i)
        #lg(s)
        out.append(s[3:])

    return out

def split(s, b):
    out = ''
    n = len(s)
    for i in range(n):
        out += s[i]
        if i <= n - 2:
            if b[i] == '1':
                out += '|'
    out_ls = out.split('|')
    return out_ls

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


def is_pali_ls(ls, h):
    for s in ls:
        if s in h:
            if not h[s]:
                return False

        else:
            f = is_pali(s)
            #lg(s, f)
            h[s] = f
            if not f:
                return False 

    return True

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        bin_ls = gen(2**(n - 1))
        #lg(bin_ls)

        out = []
        h = {}
        for b in bin_ls:
            ls = split(s, b)
            #lg('ls = %s' % ls)
            if is_pali_ls(ls, h):
                out.append(ls)

        return out




