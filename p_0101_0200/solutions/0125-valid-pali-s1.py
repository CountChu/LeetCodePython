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

solution_json = {
    "date": "2023/12/4",
    "design": 0,
    "coding": 0,
    "runtime": "59 ms",
    "fasterThan": "21%",
    "memory": "17.16 MB" 
}

'''
    "A man, a plan, a canal: Panama"

    0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20     
    a m a n a p l a n a  c  a  n  a  l  p  a  n  a  m  a

    0 1 2 3 4 5 6 7
    r a c e a c a r

'''

def build_pali(s):
    out = ''
    for i in range(len(s)):
        if not s[i].isalnum():
            continue 

        out += s[i].lower()

    return out

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def isPalindrome(self, s: str) -> bool:
        pali = build_pali(s)
        #lg(pali)

        n = len(pali)
        i = 0
        j = n - 1

        while True:
            #lg(i, j)
            if i > j:
                break

            if pali[i] != pali[j]:
                return False 
            i += 1
            j -= 1

        return True