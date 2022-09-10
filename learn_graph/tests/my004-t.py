
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

        if op == 'UnionFind':
            obj = module.UnionFind(data[0])
        elif op == 'init':
            obj.init(data)
        elif op == 'union':
            obj.union(data[0], data[1])
        elif op == 'connected':
            out = obj.connected(data[0], data[1])
            assert out == answer 
        elif op == 'str':
            out = str(obj)
            assert out == answer
        else :
            assert False, op        

        obj.dump()

    return obj

def run(sln):
    if False:
        obj = test_module(
            sln.module,
            [
                ('UnionFind',  [7],  None),
                # [0, 1, 2, 3, 4, 5, 6]
                #  0, 1, 2, 3, 4, 5, 6

                ('union',      [0, 1],  None),
                # [0, 0, 2, 3, 4, 5, 6]
                #  0, 1, 2, 3, 4, 5, 6

                ('union',      [1, 2],  None),
                # [0, 0, 0, 3, 4, 5, 6]
                #  0, 1, 2, 3, 4, 5, 6

                ('union',      [1, 3],  None),
                # [0, 0, 0, 0, 4, 5, 6]
                #  0, 1, 2, 3, 4, 5, 6

                ('union',      [4, 5],  None),
                # [0, 0, 0, 0, 4, 4, 6]
                #  0, 1, 2, 3, 4, 5, 6

                ('union',      [4, 6],  None),
                # [0, 0, 0, 0, 4, 4, 4]
                #  0, 1, 2, 3, 4, 5, 6
                ('str',        [], '[0, 0, 0, 0, 4, 4, 4]'),

                ('union',      [1, 5],  None),
                # [0, 0, 0, 0, 0, 4, 4]
                #  0, 1, 2, 3, 4, 5, 6

                ('str',        [], '[0, 0, 0, 0, 0, 4, 4]'),
            ]
        )

    if False:
        obj = test_module(
            sln.module,
            [
                ('UnionFind',  [10],  None),
                # 0 1-2-5-6-7 3-8-9 4
                ('union',      [1, 2],  None),
                ('union',      [2, 5],  None),
                ('union',      [5, 6],  None),
                ('union',      [6, 7],  None),
                ('union',      [3, 8],  None),
                ('union',      [8, 9],  None),
                ('connected',  [1, 5],  True),
                ('connected',  [5, 7],  True),
                ('connected',  [4, 9],  False),
                ## 0 1-2-5-6-7 3-8-9-4
                ('union',      [9, 4],  None),
                ('connected',  [4, 9],  True),
                ('str',        [], '[0, 1, 1, 3, 3, 1, 1, 1, 3, 3]'),
            ]
        )

    if True:
        obj = test_module(
            sln.module,
            [
                ('UnionFind',  [6],  None),
                ('union',      [1, 0],  None),
                ('union',      [2, 0],  None),
                ('union',      [3, 0],  None),
                ('union',      [4, 0],  None),
                ('union',      [5, 0],  None),
                ('str',        [], '[1, 2, 3, 4, 5, 5]'),
            ]
        )        

 
