# LeetCodePython
The project LeetCodePython provides:
1. A platform to test your Python solutions of the problems in LeetCode with test scripts. 
2. My Python solutions of LeetCode. 

You can use the platform to organize your problems of LeetCode and practicing your Python solutions locally.

All problems, solutions, and test scripts are specified in config.json. Therefor you can run test.py to test your solution of a given problem.

## test.py

For example:
```
python test.py 0001 -s s1
```

The command tests your solution of the problem 0001 with the solution version s1.


## Directories:
```
[learn_binary_search]
    [problems]
    [solutions]
    [tests]
    config.json
[learn_binary_search_tree]
    [problems]
    [solutions]
    [tests]
    config.json
...
[p_0001_01000]
    [problems]
        0001-two-sum.py
        0002-add-two-numbers.py
        ...
    [solutions]
        0001-two-sum-s1.py
        0001-two-sum-s2.py
        ...
        0002-add-two-numbers-s1.py
        0002-add-two-numbers-s2.py
        ...
    [tests]
        0001-t.py
        0002-t.py
        ...
    config.json
```

The first level directories are lessons. E.g., learn_binary_search, learn_binary_search_tree, and p_0001_01000.

Each lesson directory has a config.json and sub directories: problems, solutions, and tests.

## config.json
```
{
    "dirs": {
        "problemDn": "problems",
        "solutionDn": "solutions",
        "testDn": "tests" 
    },
    "problems": [
        {
            "id": "0001",
            "inferId": "two-sum", 
            "name": "1. Two Sum",
            "level": "easy"
        },
        {
            "id": "0002",
            "inferId": "add-two-numbers", 
            "name": "2. Add Two Numbers",
            "level": "medium",
            "testScript": "0002-t.py"
        },
... ...
```
* dirs: It specifies sub directories under the lesosn.
    * problemDn: It specifies the problems directory
    * solutionDn: It specifies the solutions directory
    * testDn: It specifies the test directory
* problems: It specifies the metadata of the problems
    * id: The unique ID of the problem in all lessons.
    * inferId: The inference ID of the problem. It combines with id to build a short file name of the problem. E.g., The file 0001-two-sum.py is under the problems directory. The files 0001-two-sum-s1.py and 0001-two-sum-s2.py are under the solutions directory. The postfix -s1 and -s2 means the solution 1 and solution 2 of the problem. You can specify any postfix for the solution file name.
    * name: The description of the problem.
    * level: The level of the problem. (hard, medium, easy)
    * testScript: The file name of the test script of the problem under the tests directory. If it is not specified, the default is {id}-t.py. E.g., 0002-t.py is a test script file name of the problem ID 0002.  


## The problems directory.

The directory contains templates for all problems.
```
0001-two-sum.py
0002-add-two-numbers.py
...
```

The template of the problem is automatically generated if it doesn't exist. For example, If you firstly enter the command.
```
$ python test 0001 -s p

The problem does not exist.
p_0001_0100/problems/0001-two-sum.py
Do you want to create it? [y/Y]
```

If you enter 'y' or 'Y', it will build a template as below:

0001-two-sum.py
```
#
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

solution_json = {
    "date": "2022/?/??",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "fasterThan": "",
    "memory": "?? MB" 
}

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
```

You can modify it as below.
```
#
# https://leetcode.com/problems/two-sum/
#
# Given an array of integers nums and an integer target, return indices 
# of the two numbers such that they add up to target.  
#

from typing import List
import pdb

solution_json = {
    "date": "2022/?/??",
    "design": 0,
    "coding": 0,
    "runtime": "?? ms",
    "memory": "?? MB"
}

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        return None
```

## The tests directory.

The directory contains test scripts for problems.
```
0001-t.py
0002-t.py
...
```

The test script of the problem is automatically generated if it doesn't exist. For example, if you enter the same command and the script doesn't exists.

```
$ python test.py 0001 -s p
Problem: ...

The testScript does not exist.
p_0001_0100/tests/0001-t.py
Do you want to create it? [y/Y]
```

If you enter 'y' or "Y", it will build a test scripts as below:

0001-t.py
```

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

```

You can clip it for your necessary. For example:
```
def test(sln, nums, target, answer):
    print('nums = %s, target = %d, answer = %s' % (nums, target, answer))
    out = sln.twoSum(nums, target)
    out.sort()
    assert out == answer, out
    print('')

def run(sln):

    test(sln, [1, 6142, 8192, 10239], 18431, [2, 3])
    test(sln, [1, 10239, 6142, 8192], 18431, [1, 3])
    test(sln, [1, 18430, 3, 2], 18431, [0, 1])
    test(sln, [3, 2, 3], 6, [0, 2])
    test(sln, [1, 2, 7, 11, 15], 9, [1, 2])
    test(sln, [2, 7, 11, 15], 9, [0, 1])
    test(sln, [2, 3, 4], 6, [0, 2])
    test(sln, [3, 3], 6, [0, 1])
    test(sln, [2, 5, 5, 11], 10, [1, 2])
    test(sln, [15, 11, 7, 2, 1], 9, [2, 3])
    test(sln, [3, 2, 4], 6, [1, 2])
```


## The solutions directory.

The directory contains solutions of problems. It contains different versions of solutions for a problem.
```
0001-two-sum-s1.py
0001-two-sum-s2.py
...
0002-add-two-numbers-s1.py
0002-add-two-numbers-s2.py
...
```

The solution is automatically generated if it doesn't exist. For example, if you enter the same command the the solution doesn't exists.
```
 % python test.py 0001 -s p
Problem: ...

The solution p is not found.
Do you want to create the solution p for the problem 0001-two-sum? [y/Y]
p_0001_0100/solutions/0001-two-sum-p.py
```  

If you enter 'y' or 'Y', it will build a solution 0001-two-sum-p.py that is copied from 0001-two-sum under the problems directory

The 'p' is a postfix of the solution. You can use any postfix. The 'p' is the abbreviation of 'practice' which means you create the solution is for practicing.

(If you recognize your practicing solution is good for worth being kept, you can modify the postfix to 's1' which means solution 1.) 


## summary.py

```
% python summary.py lesson
% python summary.py p
% python summary.py problem
% python summary.py problem -l p_0001_0100
% python summary.py p --like
```

```
% python summary.py problem -l learn_heap
Liked problems: (4)
     0215,  medium: 215. Kth Largest Element in an Array
     0347,  medium: 347. Top K Frequent Elements
    my001,    easy: Implement min heap
    my002,    easy: Heapify an array

Liked problems(refer): (1)
    0703 @ learn_binary_search_tree, easy: 703. Kth Largest Element in a Stream
```
