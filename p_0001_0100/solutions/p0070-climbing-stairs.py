# 
# You are climbing a staircase. It takes n steps to reach the top.
# 
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# 

from typing import List
import pdb

class Solution:
    def climbStairs(self, n: int) -> int:
        print('n = %d' % n)
        def f1(n, x, ctx):
            n = n - x
            #line = ''
            #line += 'x = %d, n = %d, ' % (x, n)
            if n == 0:
                #line += 'stop, '
                ctx['total'] += 1
            #print(line)
            if n - 1 >= 0:
                f1(n, 1, ctx)
            if n - 2 >= 0:
                f1(n, 2, ctx)
            
        ctx = {'total': 0}    
        if n - 1 >= 0:    
            f1(n, 1, ctx)
        
        if n - 2 >= 0:
            f1(n, 2, ctx)
            
        return ctx['total']