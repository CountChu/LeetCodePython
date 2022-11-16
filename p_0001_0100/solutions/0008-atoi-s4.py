#
# https://leetcode.com/problems/string-to-integer-atoi/
#
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer 
# (similar to C/C++'s atoi function).
#

import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/11/5",
    "design": 0,    
    "coding": 18,
    "runtime": "43 ms",
    "fasterThan": "85%",    
    "memory": "13.9 MB"
}

class Solution:
    def myAtoi(self, s: str) -> int:
        h = {
            '0': 0,
            '1': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
        }


        state = 'init'
        out = 0

        sign = +1
        for i, c in enumerate(s):
            if state == 'init':
                if c == ' ':
                    state = 'init'
                elif c in ['-', '+']:
                    state = 's'
                elif c.isdigit():
                    state = 'n'
                else:
                    return 0

            elif state == 's':
                if c.isdigit():
                    state = 'n'
                else:
                    return 0

            elif state == 'n':
                if c.isdigit():
                    state = 'n'
                else:
                    state = 'final'

            elif state == 'final':
                state = 'final'

            #print(i, c, state)

            if state == 's':
                sign = +1
                if c == '-':
                    sign = -1
            elif state == 'n':
                out = 10*out + h[c]

        out = sign * out
        
        min_v = -2**31
        if out < min_v:
            out = min_v

        max_v = 2**31 - 1
        if out > max_v:
            out = max_v

        return out
            

        