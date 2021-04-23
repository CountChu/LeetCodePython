#
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer 
# (similar to C/C++'s atoi function).
#

import pdb

#
# 2021/4/11: 31 mins, Runtime: 32ms, Memory: 14.2 MB
#

class Solution:
    def myAtoi(self, s: str) -> int:
    
        num_d = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9
            }
        
        def is_sign(c):
            return c in ['+', '-']
           
        state = 'init'
        v1 = 0
        sign = False
        for i, c in enumerate(s):
            
            if state == 'init':
                if c in num_d:
                    state = 'num'
                elif is_sign(c):
                    state = 'sign'
                elif c == ' ':
                    state = 'space'
                else:    
                    state = 'word'
            elif state == 'num':
                if c in num_d:
                    state = 'num'
                elif is_sign(c):
                    state = 'word'
                else:    
                    state = 'word'
            elif state == 'sign':
                if c in num_d:
                    state = 'num'
                else:
                    state = 'word'
            elif state == 'space':
                if c in num_d:
                    state = 'num'
                elif is_sign(c):
                    state = 'sign'
                elif c == ' ':
                    state = 'space'
                else:
                    state = 'word'
            elif state == 'word':            
                state = 'word'
            else:
                assert False
                
            if state == 'num':
                v1 = (v1 * 10 + num_d[c])
            elif state == 'sign':
                if c == '-':
                    sign = True
                
            #print(i, c, state, v1)
                
        if sign:
            v1 = -v1
            
        min = (-2)**31
        max = 2**31 - 1
            
        if v1 < min:
            v1 = min
        if v1 > max:
            v1 = max
           
            
        #pdb.set_trace() 
        return v1
            
        