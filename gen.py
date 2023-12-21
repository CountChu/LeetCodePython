import sys
import datetime

import pdb
br = pdb.set_trace

g_lines = []

def _(s):
    g_lines.append('%s\n' % s)

def problem():
    content = """#
# https://leetcode.com/problems/...
#
# Given an array...
#
# Example 1:
#       Input:
#       Output:
#
# Example 2: 
#       Input:
#       Output: 
# 

from typing import List
import sys
import pdb
br = pdb.set_trace

class Solution:
    def __init__(self):
        self.module = sys.modules[__name__]

    def findNumbers(self, nums: List[int]) -> int:
        return 0

class MyClass:
    def __init__(self):
        pass

    def __str__(self):
        return ''

    def dump(self):
        print(str(self))        
"""
    return content


def test():
    content = """
from data_structure import *
import pdb
br = pdb.set_trace

def test_solution(sln, s, target):
    print("s = %s, target = %s" % (s, target))
    out = sln.func(s)
    print("out = %s" % out)
    print('')

    assert out == target

def test_module(module, script_ls):
    for script in script_ls:
        print(script)
        op, data, answer = script

        if op == 'MinHeap':
            obj = module.MinHeap(data[0])
        elif op == 'add':
            obj.add(data[0])
        elif op == 'peek':
            out = obj.peek()
            assert out == answer
        elif op == 'pop':
            out = obj.pop()
            assert out == answer 
        elif op == 'size':
            out = obj.size()
            assert out == size 
        elif op == 'str':
            out = str(obj) 
            assert out == answer 
        else :
            assert False, op        

        obj.dump()

    return obj

def run(sln):
    test_solution(sln, [12, 9, 10, 6, 4, 5, 3], [3, 4, 5, 6, 9, 10, 12])

    if True:
        obj = test_module(
            sln.module,
            [
                ('MinHeap',  [5],  None),
                ('add',      [3],  None),
                ('add',      [1],  None),
                ('add',      [2],  None),
                ('__str__',  [], '[1, 3, 2]'),
                ('peek',     [],  1),
                ('pop',      [],  1),
                ('pop',      [],  2),
                ('pop',      [],  3),
                ('add',      [4],  None),
                ('add',      [5],  None),
                ('__str__',  [], '[4, 5]'),
            ]
        )
"""
    return content  

def solution_0():
    br()

def solution(problem_fn, solution_fn):

    f = open(problem_fn)
    lines = f.readlines()
    f.close()

    today = datetime.datetime.now().strftime('%Y/%-m/%-d')

    content = f"""solution_json = {{
    "date": "{today}",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "??%",
    "memory": "?? MB"
}}

"""
    lines.insert(0, content)
    
    f = open(solution_fn, 'w')
    f.writelines(lines)
    f.close()



