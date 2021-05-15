from data_structure import *
import pdb

def test(sln, module, op_ls, data_ls, answer_ls):
    print('op_ls = %s, data_ls = %s, answer_ls = %s' % (op_ls, data_ls, answer_ls))

    for op, data, answer in zip(op_ls, data_ls, answer_ls):
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

def run(sln, module):
	test(
		sln,
		module,
		["MinStack","push","push","push","getMin","pop","top","getMin"],
		[[],[-2],[0],[-3],[],[],[],[]],
		[None,None,None,None,-3,None,0,-2]
		)

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