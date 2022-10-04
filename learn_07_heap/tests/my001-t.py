from data_structure import *
import pdb

def test(module, script_ls):
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
            assert out == answer, out 
        else :
            assert False, op        

        obj.dump()

    return obj

def run(sln):
    if True:
        obj = test(
            sln.module,
            [
                ('MinHeap',  [5],  None), 
                ('add',      [3],  None), 
                ('add',      [1],  None), 
                ('add',      [2],  None),
                ('str',      [], '[1, 3, 2]'),
                ('peek',     [],  1),
                ('pop',      [],  1),
                ('pop',      [],  2),
                ('pop',      [],  3),
                ('add',      [4],  None),
                ('add',      [5],  None),
                ('str',  [], '[4, 5]'),
            ]
        )

    if True:
        obj = test(
            sln.module,
            [
                ('MinHeap',  [10],  None), 
                ('add',      [4],  None),
                ('add',      [5],  None),
                ('add',      [6],  None),
                ('add',      [7],  None),
                ('add',      [8],  None),
                ('add',      [9],  None),
                ('add',      [10],  None),
                ('str',      [], '[4, 5, 6, 7, 8, 9, 10]'),
                ('pop',      [],  4),
                ('str',      [], '[5, 7, 6, 10, 8, 9]'),                
            ]
        )

    if True:
        obj = test(
            sln.module,
            [
                ('MinHeap',  [5],  None), 
                ('add',      [3],  None), 
                ('add',      [1],  None), 
                ('add',      [2],  None),
                ('str',      [], '[1, 3, 2]'),
                ('peek',     [],  1),
                ('pop',      [],  1),
                ('pop',      [],  2),
                ('pop',      [],  3),
                ('add',      [4],  None),
                ('add',      [5],  None),
                ('str',      [], '[4, 5]'),
                ('add',      [6],  None),           
                ('str',      [], '[4, 5, 6]'), 
                ('pop',      [],  4),
                ('str',      [], '[5, 6]'),             
            ]
        )