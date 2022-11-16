#
# https://leetcode.com/problems/reverse-integer/
#
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer 
# range [-2**31, 2**31 - 1], then return 0.
#

import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/5",
    "design": 0,    
    "coding": 10,
    "runtime": "32 ms",
    "fasterThan": "96%",    
    "memory": "13.8 MB"
}

class Solution:
    def reverse(self, x: int) -> int:        
        s = +1
        if x < 0:
            s = -1
            x = -x

        out = 0
        while True:
            r = x % 10 
            out += r
            #print(out)

            x = x // 10
            if x == 0:
                break

            out = out * 10

        out = s * out

        if not ((-2)**31 <= out <= 2**31 - 1):
            out = 0

        return out

