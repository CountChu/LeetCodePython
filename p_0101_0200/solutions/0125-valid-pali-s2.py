solution_json = {
    "date": "2023/12/20",
    "design": 0,
    "coding": 7,
    "runtime": "50 ms",
    "fasterThan": "40%",
    "memory": "17.91 MB"
}

#
# https://leetcode.com/problems/valid-palindrome/
#
# A phrase is a palindrome if, after converting all uppercase letters 
# into lowercase letters and removing all non-alphanumeric characters, 
# it reads the same forward and backward. Alphanumeric characters 
# include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
    s = "A man, a plan, a canal: Panama"

        0 1 2 3                                 n-1
    -> 'a m a n a p l a n a c a n a l p a n a m a'
        i                                       j

'''

def trans(s):
    n = len(s)
    out = ''
    for i in range(n):
        c = s[i]
        if not c.isalnum():
            continue 

        c = c.lower()
        out += c

    return out

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isPalindrome(self, s: str) -> bool:
        s = trans(s)        
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
        