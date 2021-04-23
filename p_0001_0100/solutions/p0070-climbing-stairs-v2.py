# 
# You are climbing a staircase. It takes n steps to reach the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 

from typing import List
import pdb

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 1
    
        f = [0] * (n + 1)
        f[0] = 1
        f[1] = 1
        for i in range(2, n + 1):
            f[i] = f[i-1] + f[i-2]
        return f[i]
                 
