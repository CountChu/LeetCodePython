from data_structure import *
import pdb

def test(module, script_ls):
    for script in script_ls:
        print(script)
        op, data, answer = script

        if op == 'MinStack':
            obj = module.MinStack()
        elif op == 'push':
            obj.push(data[0])
        elif op == 'pop':
            obj.pop()
        elif op == 'top':
            out = obj.top()
            assert out == answer
        elif op == 'getMin':
            out = obj.getMin()
            assert out == answer

    return obj

def run(sln):
    obj = test(
        sln.module,
        [
            ('MinStack', [],   None), 
            ('push',     [-2], None), 
            ('push',     [0],  None), 
            ('push',     [-3], None), 
            ('getMin',   [],   -3), 
            ('pop',      [],   None), 
            ('top',      [],   0), 
            ('getMin',   [],   -2), 
        ]
    )
    print(obj)

'''
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
       
    def push(self, val: int) -> None:
        pass

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass

#
# Your MinStack object will be instantiated and called as such:
#

obj = MinStack()
obj.push(val)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
'''