#
# https://leetcode.com/problems/decode-string/
#
# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string 
# inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.
# 
# You may assume that the input string is always valid; there are no extra 
# white spaces, square brackets are well-formed, etc. Furthermore, 
# you may assume that the original data does not contain any digits 
# and that digits are only for those repeat numbers, k. For example, 
# there will not be input like 3a or 2[4].
#
# The test cases are generated so that the length of the output 
# will never exceed 10^5.
#

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/29",
    "design": 0,
    "coding": 0,
    "runtime": "58 ms",
    "fasterThan": "38%",
    "memory": "14 MB" 
}

'''
    3[ab2[c]d] ---> abccdabccdabccd

    3, [, ab, 2, [, c, ], d, ]

    3, [, ab, 2, [, c  <- ]
    3, [, ab, cc       <- d
    3, [, ab, cc, d    <- ] 
    abccdabccdabccd
'''

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def decodeString(self, s: str) -> str:
        token_ls = tokenize(s)


        t = None                        # n, [, s, ]

        stack = []                      # stack = [(c, t)]
        for c, t in token_ls:
            #print(c, t, stack)
            if t in ['n', '[']:
                stack.append((c, t))
            elif t == 's':
                new_c = c
                if stack != [] and stack[-1][1] == 's':
                    top = stack.pop()
                    new_c = top[0] + new_c
                stack.append((new_c, t)) 
            elif t == ']':
                top0_c, top0_t = stack.pop()
                if top0_t == 's':
                    top1_c, top1_t = stack.pop()
                    if top1_t == '[':
                        top2_c, top2_t = stack.pop()
                        if top2_t == 'n':
                            new_c = top0_c * int(top2_c)
                            if stack != [] and stack[-1][1] == 's':
                                top = stack.pop()
                                new_c = top[0] + new_c
                            stack.append((new_c, 's'))
                        else:
                            assert False
                    else:
                        br()
                        assert False, top1_t
                else:
                    assert False

        if stack == []:
            return ''
        elif len(stack) == 1:
            return stack[0][0]
        else:
            assert False, stack

def tokenize(s):
    out = []
    state = 'init'                      # init, [, ], n, s
    new_n = ''
    new_s = ''
    for i in range(len(s)):
        c = s[i]
        if state == 'init':
            if c == '[':
                assert False 
            elif c == ']':
                assert False 
            elif c.isnumeric():
                state = 'n'
            else:
                state = 's'

        elif state == 'n':
            if c == '[':
                state = '['
            elif c == ']':
                assert False 
            elif c.isnumeric():
                state = 'n'
            else:
                assert False

        elif state == '[':
            if c == '[':
                assert False 
            elif c == ']':
                assert False 
            elif c.isnumeric():
                state = 'n'
            else:
                state = 's'

        elif state == 's':
            if c == '[':
                assert False 
            elif c == ']':
                state = ']'
            elif c.isnumeric():
                state = 'n'
            else:
                state = 's'

        elif state == ']':
            if c == '[':
                assert False 
            elif c == ']':
                state = ']'
            elif c.isnumeric():
                state = 'n' 
            else:
                state = 's'

        else:
            assert False

        #print(c, state)            

        if state == 'n':
            new_n += c
            if new_s != '':
                out.append((new_s, 's'))
                new_s = ''

        elif state == 's':
            new_s += c

        elif state == '[':
            if new_n != '':
                out.append((new_n, 'n'))
                new_n = ''
            out.append((c, state))

        elif state == ']':
            if new_s != '':
                out.append((new_s, 's'))
                new_s = ''
            out.append((c, state))

        else:
            assert False
    
    if new_s != '':
        out.append((new_s, 's'))

    return out


def pop_to_number(stack):
    s = ''
    state == 'init'
    while True: 
        if stack == []:
            break
        top_c, top_t = stack.pop()
        if top_t == 's':
            assert state in ['init', 's']
            state = 's'
            s += 's'

        elif top_t == '[':
            assert state == 's'
            state = '['

        elif top_t == 'n':
            pass







