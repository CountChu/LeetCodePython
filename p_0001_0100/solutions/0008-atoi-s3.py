#
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer 
# (similar to C/C++'s atoi function).
#
# Example 1:
#       Input: s = "42"
#       Output: 42
#
# Example 2:
#       Input: s = "   -42"
#       Output: -42
#

import pdb

solution_json = {
    "date": "2022/8/30",
    "coding": 0,
    "runtime": "55 ms",
    "fasterThan": "51.81%", 
    "memory": "14 MB"
}       

class Solution:

    def __init__(self):
        self.d = {}
        for i in range(10):
            self.d[chr(ord('0')+i)] = i

    def is_number(self, c):
        return c in self.d
    
    def is_space(self, c):
        return c == ' '

    def is_sign(self, c):
        return c in ['-', '+']

    def myAtoi(self, s: str) -> int:
        state = 'init'
        out = 0
        sign = '+'
        for c in s:
            if state == 'init':
                if self.is_number(c):
                    state = 'number'
                elif self.is_space(c):
                    state = 'space'
                elif self.is_sign(c):
                    state = 'sign'
                else:
                    state = 'final'
            elif state == 'number':
                if self.is_number(c):
                    state = 'number'
                else:
                    state = 'final'
            elif state == 'space':
                if self.is_number(c):
                    state = 'number'
                elif self.is_space(c):
                    state = 'space'
                elif self.is_sign(c):
                    state = 'sign'
                else:
                    state = 'final'
            elif state == 'sign':
                if self.is_number(c):
                    state = 'number'
                else:
                    state = 'final'
            else:
                assert False, c+', '+state

            if state == 'final':
                break

            elif state == 'number':
                out = out * 10
                out += self.d[c]

            elif state == 'sign':
                if c == '-':
                    sign = '-'

            #print(c, state)
        if sign == '-':
            out = -out

        if out < -2**31:
            out = -2**31
        elif out > 2**31 - 1:
            out = 2**31 - 1

        #pdb.set_trace()
        return out
            
        