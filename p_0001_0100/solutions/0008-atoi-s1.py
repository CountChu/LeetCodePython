#
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer 
# (similar to C/C++'s atoi function).
#

import pdb

solution_json = {
    "date": "2021/4/3",
    "coding": 24,
    "runtime": "112 ms",
    "fasterThan": "5.29%",
    "memory": "13.9 MB"
}

class Solution:
    def myAtoi(self, s: str) -> int:

        def is_num(c):
            return ord(c) in range(ord('0'), ord('9') + 1)
    
        v2 = 0
        
        sign = False
        
        state = 'init'
        #pdb.set_trace()
        for i in range(len(s)):
            c = s[i]
            #print('c = %s' % c)
            if state in ['init', 'number', 'space', 'sign'] and is_num(c):                
                state = 'number'
            elif state in ['init', 'space'] and c in ['-', '+']:
                state = 'sign'
            elif state in ['init', 'space'] and c == ' ':
                state = 'space'
            elif state == 'number' and not is_num(c):
                state = 'end'
            else:
                state = 'word'
                
            if state == 'word':
                return 0
            elif state == 'sign':
                if c == '-':
                    sign = True
            elif state == 'end':
                break

            v1 = 0
            if state == 'number':
                v1 = (ord(c) - ord('0')) 
                v2 = v2 * 10 + v1
            
            #print(i, c, state, v1, v2)

        if sign:
            v2 = -1 * v2

        min_v = (-2)**31
        max_v = 2**31 - 1
        if v2 < min_v:
            v2 = min_v
            return v2
            
        if v2 > max_v:
            v2 = max_v
            return v2
        
        return v2

        