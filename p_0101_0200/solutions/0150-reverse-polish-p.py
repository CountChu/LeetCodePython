#
# https://leetcode.com/problems/evaluate-reverse-polish-notation/
#
# Evaluate the value of an arithmetic expression in Reverse Polish Notation.
#
# Valid operators are +, -, *, and /. Each operand may be an integer 
# or another expression.
#
# Note that division between two integers should truncate toward zero.
#
# It is guaranteed that the given RPN expression is always valid. 
# That means the expression would always evaluate to a result, 
# and there will not be any division by zero operation.
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

solution_json = {
    "date": "2022/10/22",
    "design": 0,
    "coding": 0,
    "runtime": "71 ms",
    "fasterThan": "91.87",
    "memory": "14.6 MB" 
}

'''
    2:  push 2 
        [2]
    1:  push 1 
        [2, 1]
    +:  pop 1, pop 2, 3 = 1 + 2, push 3
        [3]
    3:  push 3 
        [3, 3]
    *:  pop 3, pop 3, 9 = 3 * 3, push 9
        [9]     

'''
class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                v1 = int(stack.pop())
                v0 = int(stack.pop())
                v2 = op(t, v0, v1)
                stack.append(str(v2))
            else:
                stack.append(t) 
            #print(t, stack)

        out = stack[-1]
        out = int(out)
        return out

def op(t, v0, v1):
    if t == '+':
        v2 = v0 + v1 
    elif t == '-':
        v2 = v0 - v1 
    elif t == '*':
        v2 = v0 * v1 
    elif t == '/':
        v2 = int(v0 / v1) 

    else:
        assert False
    return v2




