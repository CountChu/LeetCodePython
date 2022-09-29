
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

        if op == 'MyLinkedList':
            obj = module.MyLinkedList()
        elif op == 'addAtHead':
            obj.addAtHead(data[0])
        elif op == 'addAtTail':
            out = obj.addAtTail(data[0])
            assert out == answer
        elif op == 'addAtIndex':
            out = obj.addAtIndex(data[0], data[1])
            assert out == answer
        elif op == 'get':
            out = obj.get(data[0])
            assert out == answer 
        elif op == 'deleteAtIndex':
            out = obj.deleteAtIndex(data[0])
        else :
            assert False, op        

        obj.dump()

    return obj

def run(sln):
    if True:
        obj = test_module(
            sln.module,
            [
                ('MyLinkedList',    [],     None),
                ('addAtHead',       [1],    None),
                ('addAtTail',       [3],    None),
                ('addAtIndex',      [1, 2], None),
                ('get',             [1],    2),
                ('deleteAtIndex',   [1],    None),
                ('get',             [1],    3),
            ]
        )

    if True:
        obj = test_module(
            sln.module,
            [
                ('MyLinkedList',    [],     None),
                ('addAtTail',       [1],    None),
                ('get',             [0],    1),
            ]
        )
