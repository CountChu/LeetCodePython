from data_structure import *
import pdb

def test(sln, module, op_ls, data_ls, answer_ls):
    print('op_ls = %s, data_ls = %s, answer_ls = %s' % (op_ls, data_ls, answer_ls))

    for op, data, answer in zip(op_ls, data_ls, answer_ls):
    	if op == 'MyCircularQueue':
    		obj = module.MyCircularQueue(data[0])
    	
    	elif op == 'enQueue':
    		out = obj.enQueue(data[0])
    		assert out == answer

    	elif op == 'Rear':
    		out = obj.Rear()
    		assert out == answer

    	elif op == 'isFull':
    		out = obj.isFull()
    		assert out == answer

    	elif op == 'deQueue':
    		out = obj.deQueue()
    		assert out == answer

    	elif op == 'isEmpty':
    		out = obj.isEmpty()
    		assert out == answer

    	elif op == 'Front':
    		out = obj.Front()
    		assert out == answer

    	else:
    		assert False, op

def run(sln, module):

	if True:
	    test(
	    	sln, 
	    	module,
	    	[
	    		"MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", 
	    		"Rear", "isFull", "deQueue", "enQueue", "Rear"
	    	],
	    	[[3], [1], [2], [3], [4], [], [], [], [4], []],
	    	[None, True, True, True, False, 3, True, True, True, 4]
	    )

	    test(
	    	sln,
	    	module,
			[
				"MyCircularQueue", "enQueue", "Rear", "Rear", "deQueue",
				"enQueue", "Rear", "deQueue", "Front", "deQueue",
				"deQueue", "deQueue"
			],
			[
				[6], [6], [], [], [],
				[5], [], [], [], [],
				[],[]
			],
			[
				None, True, 6, 6, True,
				True, 5, True, -1, False,
				False, False
			]
		)

	if True:
		test(
			sln, 
			module,
			[
				"MyCircularQueue", "enQueue", "enQueue", "deQueue", "enQueue",
				"deQueue", "enQueue", "deQueue", "enQueue", "deQueue", 
				"Front"
			],
			[
				[2], [1], [2], [], [3],
				[], [3], [], [3], [],
				[]
			],
			[
				None, True, True, True, True,
				True, True, True, True, True,
				3
			]
		)



'''
class MyCircularQueue:

    def __init__(self, k: int):
        pass

    def enQueue(self, value: int) -> bool:
        pass

    def deQueue(self) -> bool:
        pass

    def Front(self) -> int:
        pass

    def Rear(self) -> int:
        pass

    def isEmpty(self) -> bool:
        pass

    def isFull(self) -> bool:
		pass        

obj = MyCircularQueue(k)
param_1 = obj.enQueue(value)
param_2 = obj.deQueue()
param_3 = obj.Front()
param_4 = obj.Rear()
param_5 = obj.isEmpty()
param_6 = obj.isFull()    
'''
