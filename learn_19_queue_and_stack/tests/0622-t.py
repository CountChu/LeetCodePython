from data_structure import *
import pdb

def test(module, script_ls):

    obj = None
    for script in script_ls:
    	print(script)
    	op, data, answer = script

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

    	print(obj)
    return obj

def run(sln):
	if True:
	    obj = test(
	    	sln.module,
	    	[
	    		('MyCircularQueue', [3], None), 
	    		('enQueue', 		[1], True),
	    		('enQueue', 		[2], True),
	    		('enQueue', 		[3], True),
	    		('enQueue', 		[4], False),
	    		('Rear', 			[],  3), 
	    		('isFull', 			[],  True), 
	    		('deQueue', 		[],  True), 
	    		('enQueue', 		[4], True), 
	    		('Rear', 			[],  4), 
	    	]
	    )

	if True:
	    obj = test(
	    	sln.module,
	    	[
	    		('MyCircularQueue', [6], None),
	    		('enQueue', 		[6], True),
	    		('Rear', 			[],  6),
	    		('Rear', 			[],  6),
	    		('deQueue', 		[],  True),
	    		('enQueue', 		[5], True),
	    		('Rear', 			[],  5),
	    		('deQueue', 		[],  True),
	    		('Front', 			[],  -1),
	    		('deQueue', 		[],  False),
	    		('deQueue', 		[],  False),
	    		('deQueue', 		[],  False),
	    	]
		)

	if True:
		obj = test(
	    	sln.module,
			[
				('MyCircularQueue', [2], None),
				('enQueue', 		[1], True),
				('enQueue', 		[2], True),
				('deQueue', 		[],  True),
				('enQueue', 		[3], True),
				('deQueue', 		[],  True),
				('enQueue', 		[3], True),
				('deQueue', 		[],  True),
				('enQueue', 		[3], True),
				('deQueue', 		[],  True),
				('Front', 			[],  3),
			]

		)

	if True:
		obj = test(
	    	sln.module,
			[
				('MyCircularQueue', [2], None),
				('enQueue', 		[4], True),
				('Rear', 			[],  4),
				('enQueue', 		[9], True),
				('deQueue', 		[],  True),
				('Front', 			[],  9),
				('deQueue', 		[],  True),
				('deQueue', 		[],  False),
				('isEmpty', 		[],  True),
				('deQueue', 		[],  False),
				('enQueue', 		[6], True),
				('enQueue', 		[4], True),
			]
		)

	if True:
		obj = test(
	    	sln.module,
			[
				('MyCircularQueue', [3], None),
				('enQueue', 		[7], True),
				('deQueue', 		[],  True),
				('Front', 			[],  -1),
				('deQueue', 		[],  False),
				('Front', 			[],  -1),
				('Rear', 			[],  -1),
				('enQueue', 		[0], True),
				('isFull', 			[],  False),
				('deQueue', 		[],  True),
				('Rear', 			[],  -1),
				('enQueue', 		[3], True),
			]
		)
