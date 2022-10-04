
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
            assert out == answer, out
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

    if True:
        obj = test_module(
            sln.module,
            [
                ('MyLinkedList',    [],     None),
                ('addAtTail',       [1],    None),
                ('deleteAtIndex',   [0],    None),
            ]
        )        

    if True:
        obj = test_module(
            sln.module,
            [
                ('MyLinkedList',    [],      None),
                ('addAtIndex',      [0, 10], None),
                ('addAtIndex',      [0, 20], None),
                ('addAtIndex',      [0, 30], None),
                ('get',             [0],     30),
            ]
        )        

    if True:
        obj = test_module(
            sln.module,
            [
                ('MyLinkedList',    [],  None),
                ('addAtHead',       [2], None),
                ('deleteAtIndex',   [1], None),
                ('addAtHead',       [2], None),
                ('addAtHead',       [7], None),

                ('addAtHead',       [3], None),
                ('addAtHead',       [2], None),
                ('addAtHead',       [5], None),
                ('addAtTail',       [5], None),
                ('get',             [5], 2),

                ('deleteAtIndex',   [6], None),
                ('deleteAtIndex',   [4], None),

            ]
        )        

    if True:
        obj = test_module(
            sln.module,
            [
                ('MyLinkedList',    [],  None),
                ('addAtHead',       [4], None),
                ('get',             [1], -1),
                ('addAtHead',       [1], None),
                ('addAtHead',       [5], None),

                ('deleteAtIndex',   [3], None),
                ('addAtHead',       [7], None),
                ('get',             [3], 4),
                ('get',             [3], 4),
                ('get',             [3], 4),

                ('addAtHead',       [1], None),
                ('deleteAtIndex',   [4], None),

            ]
        )  

    if True:
        obj = test_module(
            sln.module,
            [
                ('MyLinkedList',    [],  None),
                ('addAtHead',       [2], None),
                ('addAtIndex',      [0, 1], None),
                ('get',             [1], 2),
            ]
        )  

    if True:
        obj = test_module(
            sln.module,
            [
                ('MyLinkedList',    [],  None),
                ('addAtHead',       [1], None),
                ('addAtTail',       [3], None),
                ('addAtIndex',      [1, 2], None),
                ('get',             [1], 2),

                ('deleteAtIndex',   [1], None),
                ('get',             [1], 3),
                ('get',             [3], -1),
                ('deleteAtIndex',   [3], None),
                ('deleteAtIndex',   [0], None),

                ('get',             [0], 3),
                ('deleteAtIndex',   [0], None),
                ('get',             [0], -1),

            ]
        ) 

    if True:
        obj = test_module(
            sln.module,
            [
                ('MyLinkedList',    [],  None),
                ('addAtHead',       [1], None),
                ('addAtTail',       [3], None),
                ('addAtIndex',      [3, 2], None),
            ]
        ) 
