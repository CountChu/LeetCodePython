
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
