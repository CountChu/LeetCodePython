#
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer 
# range [-2**31, 2**31 - 1], then return 0.
#

import pdb

solution_json = {
    "date": "2021/4/11",
    "coding": 8,
    "runtime": "24 ms",
    "memory": "14.1 MB"
}   

class Solution:
    def reverse(self, x: int) -> int:
    
        sign = False
        if x < 0:
            sign = True
            x = -x
            
        v2 = 0
        while True:
            v1 = x % 10
            v2 = v2 * 10 + v1
            x = x // 10
            #print(x, v1, v2)
            if x == 0:
                break
            
        if sign:
            v2 = -v2
            
        if not ((-2)**31 <= v2 <= 2**31 - 1):
            v2 = 0
            
        return v2
