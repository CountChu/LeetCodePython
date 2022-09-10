# 
# Given a non-negative integer x, compute and return the square root of x.
# 
# Since the return type is an integer, the decimal digits are truncated, 
# and only the integer part of the result is returned.
# 

from typing import List
import pdb

solution_json = {
    "date": "2021/3/26",
    "runtime": "9692 ms",
    "memory": "14.2 MB"
}

class Solution:
    def mySqrt(self, x: int) -> int: 
        #print('x = %d' % x)
        if x == 0:
            return 0
    
        elif x == 1:
            return 1
            
        y = 0
        for i in range(1, x+1):
            line = ''
            line += 'i = %d, i * i = %d' % (i, i * i)
            #print(line)    
            
            if i * i == x:
                y = i
                break
            elif i * i > x:
                y = i - 1
                break
                
        return y
        
def test(sln, x, target):
    out = sln.mySqrt(x)
    print('x = %d, out = %d' % (x, out))
    assert out == target
        
"""        
sln = Solution() 
test(sln, 2, 1)
test(sln, 1, 1)     
test(sln, 4, 2)
test(sln, 8, 2)
test(sln, 100, 10)
"""
