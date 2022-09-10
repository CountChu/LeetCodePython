# 
# Given two binary strings a and b, return their sum as a binary string.
# 

from typing import List
import pdb

solution_json = {
    "date": "2021/3/25",
    "runtime": "64 ms",
    "memory": "14.2 MB"
}

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add_pad(s, max_len):
            pad = '0'*(max_len - len(s))
            s = pad + s
            return s
        def reverse(s):
            new_s = ''
            for i in reversed(range(len(s))):
                new_s += s[i]
            return new_s    
    
        max_len = len(a)
        if max_len < len(b):
            max_len = len(b)

        a = add_pad(a, max_len)
        b = add_pad(b, max_len)
        print('a = %s, b = %s' % (a, b))
        
        a = reverse(a)
        b = reverse(b)
        print('a = %s, b = %s' % (a, b))

        c = ['0'] * (max_len + 1)
        print('c = %s' % c)
        for i in range(max_len):
            line = ''
            line += 'i = %d, ai = %s, bi = %s, ci = %s, ' % (i, a[i], b[i], c[i])

            if a[i] == '1' and b[i] == '1':
                c[i+1] = '1'

            elif a[i] == '1' and b[i] == '0':
                if c[i] == '0':
                    c[i] = '1'
                elif c[i] == '1':
                    c[i] = '0'
                    c[i+1] = '1'
                    
            elif a[i] == '0' and b[i] == '1':
                if c[i] == '0':
                    c[i] = '1'
                elif c[i] == '1':
                    c[i] = '0'
                    c[i+1] = '1' 

            elif a[i] == '0' and b[i] == '0':
                pass
                
            line += 'c = %s, ' % c
            
            print(line)
            
        if c[-1] == '0':
            c.pop(-1)
            
        new_c = ''
        for i in range(len(c)):
            new_c += c[i]
        print('new_c = %s' % new_c)    
        c = reverse(new_c)    
        print('c = %s' % c)

        return c


