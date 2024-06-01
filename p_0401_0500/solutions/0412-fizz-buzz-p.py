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

solution_json = {
    "date": "2022/11/3",
    "design": 0,
    "coding": 4,
    "runtime": "85 ms",
    "fasterThan": "51%",
    "memory": "15.2 MB" 
}

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def fizzBuzz(self, n: int) -> List[str]:
        out = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                out.append('FizzBuzz')
            
            elif i % 3 == 0:
                out.append('Fizz')
            
            elif i % 5 == 0:
                out.append('Buzz')

            else:
                out.append('%d' % i)

        return out








