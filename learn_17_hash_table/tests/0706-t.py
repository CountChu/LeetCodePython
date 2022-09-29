
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

        if op == 'MyHashMap':
            obj = module.MyHashMap()
        elif op == 'put':
            obj.put(data[0], data[1])
        elif op == 'get':
            out = obj.get(data[0])
            assert out == answer
        elif op == 'remove':
            out = obj.remove(data[0])
            assert out == answer 
        else :
            assert False, op        

        obj.dump()

    return obj

def run(sln):
    if True:
        obj = test_module(
            sln.module,
            [
                ('MyHashMap',   [],     None),
                ('put',         [1, 1], None),
                ('put',         [2, 2], None),
                ('get',         [1],    1),
                ('get',         [3],    -1),
                ('put',         [2, 1], None),
                ('get',         [2],    1),
                ('remove',      [2],    None),
                ('get',         [2],    -1),
            ]
        )
