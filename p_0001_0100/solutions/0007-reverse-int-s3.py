#
# https://leetcode.com/problems/reverse-integer/
#
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer 
# range [-2**31, 2**31 - 1], then return 0.
#

import pdb

solution_json = {
    "date": "2022/8/28",
    "coding": 0,
    "runtime": "43 ms",
    "fasterThan": "73%",
    "memory": "13.7 MB"
}

class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = -x

        out = 0
        while True:
            r = x % 10
            out += r 
            x = x // 10
            #print(r, x, out)
            if x == 0:
                break
            
            out = out * 10 

        if negative:
            out = -out

        if not ((-2)**31 <= out <= 2**31 - 1):
            out = 0

        return out

