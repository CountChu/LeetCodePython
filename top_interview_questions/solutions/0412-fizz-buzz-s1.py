solution_json = {
    "date": "2023/12/11",
    "design": 0,
    "coding": 0,
    "runtime": "43 ms",
    "fasterThan": "84%",
    "memory": "17.44 MB"
}

#
# https://leetcode.com/problems/fizz-buzz/
#
# Given an integer n, return a string array answer (1-indexed) where:
#
#       answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#       answer[i] == "Fizz" if i is divisible by 3.
#       answer[i] == "Buzz" if i is divisible by 5.
#       answer[i] == i (as a string) if none of the above conditions are true.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace
lg = print

'''
   15 

   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
       .   .       .  .              .
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                #lg('FizzBuzz')
                out.append('FizzBuzz')
            elif i % 3 == 0:
                #lg('Fizz')
                out.append('Fizz')
            elif i % 5 == 0:
                #lg('Buzz')
                out.append('Buzz')
            else:
                #lg('%d' % i)
                out.append('%d' % i)

        return out









