from typing import List
import pdb

solution_json = {
    "date": "2021/4/21",
    "coding": 9,
    "runtime": "32 ms",
    "memory": "15.7 MB"
}    

class Solution:
    def isValid(self, s: str) -> bool:
        d = False

        out = True

        ls0 = ['(', '[', '{']
        ls1 = [')', ']', '}']
        h = {
            '(': ')', 
            '[': ']',
            '{': '}',
        }

        stack = []
        n = len(s)
        for i in range(n):
            c = s[i]

            if c in ls0:
                stack.append(c)
            elif c in ls1:
                if len(stack) == 0:
                    out = False
                    break
                c2 = stack.pop()
                if c != h[c2]:
                    out = False
                    break
            else:
                out = False
                break        

            if d:
                print(i, c, stack)

        if d:
            print(i, c, stack)

        if stack != []:
            out = False

        #pdb.set_trace()
        return out
